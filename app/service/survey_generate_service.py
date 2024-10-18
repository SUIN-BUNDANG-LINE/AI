import asyncio
from langchain.output_parsers import PydanticOutputParser
from app.core.prompt.summation.document_summation_prompt import (
    document_summation_prompt,
)
from app.core.util.ai_manager import AIManager
from app.core.util.document_manager import DocumentManager
from app.core.prompt.generate.survey_parsing_prompt import survey_parsing_prompt
from app.core.prompt.generate.survey_creation_prompt import survey_creation_prompt
from app.dto.response.survey_generate_response import SurveyGenerateResponse
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
        self.ai_manager = None
        self.survey_generate_content = None
        self.document_manger = DocumentManager()
        self.survey_parsing_prompt = survey_parsing_prompt
        self.survey_creation_prompt = survey_creation_prompt
        self.document_summation_prompt = document_summation_prompt
        self.parser_to_survey = PydanticOutputParser(pydantic_object=Survey)

    class _SurveyGenerateContent:
        def __init__(
            self,
            target: str,
            group_name: str,
            text_document: str,
            user_prompt: str,
        ):
            self.target = target
            self.group_name = group_name
            self.text_document = text_document
            self.user_prompt = user_prompt

    async def generate_survey_with_file_url(
        self, request: SurveyGenerateWithFileUrlRequest
    ):
        self.ai_manager = AIManager(request.chat_session_id)
        text_document = self.document_manger.text_from_file_url(request.file_url)

        self.survey_generate_content = self._SurveyGenerateContent(
            target=request.target,
            group_name=request.group_name,
            text_document=text_document,
            user_prompt=request.user_prompt,
        )

        return await self.__generate_survey_and_summarize_document()

    async def generate_survey_with_text_document(
        self, request: SurveyGenerateWithTextDocumentRequest
    ):
        self.ai_manager = AIManager(request.chat_session_id)

        self.survey_generate_content = self._SurveyGenerateContent(
            target=request.target,
            group_name=request.group_name,
            text_document=request.text_document,
            user_prompt=request.user_prompt,
        )

        return await self.__generate_survey_and_summarize_document()

    async def __generate_survey_and_summarize_document(self):
        target = self.survey_generate_content.target
        group_name = self.survey_generate_content.group_name
        text_document = self.survey_generate_content.text_document
        user_prompt = self.survey_generate_content.user_prompt

        user_prompt_with_basic_prompt = user_prompt

        if target != "":
            user_prompt_with_basic_prompt = (
                f" {target}을 대상으로 하는 설문조사를 생성해주세요" + user_prompt
            )

        if group_name != "":
            user_prompt_with_basic_prompt = (
                f" 인사말에는 {group_name} 팀임을 밝히는 말을 포함해주세요" + user_prompt
            )

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

        return SurveyGenerateResponse(survey=parsed_generated_survey)

    async def __generate_survey(
        self,
        user_prompt_with_basic_prompt,
        text_document,
    ):
        prototype_survey = await self.__generate_prototype_survey(
            user_prompt_with_basic_prompt, text_document
        )

        return self.parser_to_survey.parse(prototype_survey)

    async def __generate_prototype_survey(
        self, user_prompt_with_basic_prompt, text_document
    ):
        return await FunctionExecutionTimeMeasurer.run_async_function(
            "설문 프로토타입 생성 태스크",
            self.ai_manager.async_chat,
            self.survey_creation_prompt.format(
                user_prompt=user_prompt_with_basic_prompt,
                document=text_document,
            ),
        )

    async def __summarize_document(self, text_document):
        document_summation = await FunctionExecutionTimeMeasurer.run_async_function(
            "문서 요약 태스크",
            self.ai_manager.async_chat_with_history,
            document_summation_prompt.format(user_document=text_document),
            is_new_chat_save=True,
        )
        return document_summation
