import asyncio

from langchain.output_parsers import PydanticOutputParser

from app.core.prompt.summation.document_summation_prompt import (
    document_summation_prompt,
)
from app.core.util.ai_manager import AIManager
from app.core.util.document_manager import DocumentManager
from app.core.util.file_manager import FileManager
from app.core.prompt.generate.survey_creation_guide_prompt import (
    survey_creation_guide_prompt,
)
from app.core.prompt.generate.survey_parsing_prompt import survey_parsing_prompt
from app.core.prompt.generate.survey_creation_prompt import survey_creation_prompt
from app.dto.response.survey_generate_response import SurveyGenerateResponse
from app.error.error_code import ErrorCode
from app.error.business_exception import business_exception
from app.dto.request.survey_generate_with_file_url_request import (
    SurveyGenerateWithFileUrlRequest,
)
from app.dto.request.survey_generate_with_text_document_request import (
    SurveyGenerateWithTextDocumentRequest,
)
from app.core.util.function_execution_time_measurer import FunctionExecutionTimeMeasurer
from app.dto.model.survey import Survey


class SurveyGenerateService:
    def __init__(self):
        self.ai_manager = AIManager()
        self.document_manger = DocumentManager()
        self.survey_creation_prompt = survey_creation_prompt
        self.survey_parsing_prompt = survey_parsing_prompt
        self.document_summation_prompt = document_summation_prompt

    async def generate_survey_with_file_url(
        self, request: SurveyGenerateWithFileUrlRequest
    ):
        text_document = self.__get_text_document_from_file_url(request.file_url)

        survey_generate_content = self._SurveyGenerateContent(
            job=request.job,
            group=request.group_name,
            text_document=text_document,
            user_prompt=request.user_prompt,
        )

        return await self.__generate_survey_with_document_summation(
            survey_generate_content
        )

    async def generate_survey_with_text_document(
        self, request: SurveyGenerateWithTextDocumentRequest
    ):
        survey_generate_content = self._SurveyGenerateContent(
            job=request.job,
            group=request.group_name,
            text_document=request.text_document,
            user_prompt=request.user_prompt,
        )

        return await self.__generate_survey_with_document_summation(
            survey_generate_content
        )

    # private
    class _SurveyGenerateContent:
        def __init__(self, job: str, group: str, text_document: str, user_prompt: str):
            self.job = job
            self.group = group
            self.text_document = text_document
            self.user_prompt = user_prompt

    async def __generate_survey_with_document_summation(
        self, survey_generate_content: _SurveyGenerateContent
    ):
        job = survey_generate_content.job
        group = survey_generate_content.group
        text_document = survey_generate_content.text_document
        user_prompt = survey_generate_content.user_prompt

        user_prompt_with_basic_prompt = user_prompt
        if job != "":
            user_prompt_with_basic_prompt += f" {job}을 위한 설문조사를 생성해주세요."

        if group != "":
            user_prompt_with_basic_prompt += f" 인사말에는 {group} 소속임을 밝히는 말을 포함해주세요."

        document_summation_task = asyncio.create_task(
            self.__summarize_document(text_document)
        )

        survey_generation_task = asyncio.create_task(
            self.__generate_survey(
                user_prompt_with_basic_prompt,
                text_document,
            )
        )

        (document_summation, parsed_generated_survey) = await asyncio.gather(
            document_summation_task, survey_generation_task
        )

        return SurveyGenerateResponse(
            chat_session_id=self.ai_manager.session_id,
            survey=parsed_generated_survey,
        )

    async def __summarize_document(self, text_document):
        document_summation = await FunctionExecutionTimeMeasurer.run_async_function(
            "문서 요약 태스크",
            self.ai_manager.async_chat_with_history,
            document_summation_prompt.format(user_document=text_document),
            self.ai_manager.session_id,
            is_new_chat_save=True,
        )
        return document_summation

    async def __generate_survey(
        self,
        user_prompt_with_basic_prompt,
        text_document,
    ):
        # 제 1번 호출
        prototype_survey = await FunctionExecutionTimeMeasurer.run_async_function(
            "설문 프로토타입 생성 태스크",
            self.ai_manager.async_chat,
            self.survey_creation_prompt.format(
                user_prompt=user_prompt_with_basic_prompt,
                document=text_document,
                guide=survey_creation_guide_prompt,
            ),
        )

        # 제 2번 호출
        parser_to_survey = PydanticOutputParser(pydantic_object=Survey)
        generated_survey_has_parsing_format = (
            await FunctionExecutionTimeMeasurer.run_async_function(
                "설문 파싱 태스크",
                self.ai_manager.async_chat_with_parser,
                survey_parsing_prompt.format(prototype_survey=prototype_survey),
                parser_to_survey,
            )
        )

        return parser_to_survey.parse(generated_survey_has_parsing_format)

    def __get_text_document_from_file_url(self, file_url: str):
        extension = FileManager.get_file_extension_from_url(file_url)
        match extension:
            case ".pdf":
                return self.document_manger.text_from_pdf_file_url(file_url)
            case ".txt":
                return self.document_manger.text_from_txt_file_url(file_url)
            case _:
                raise business_exception(ErrorCode.FILE_EXTENSION_NOT_SUPPORTED)
