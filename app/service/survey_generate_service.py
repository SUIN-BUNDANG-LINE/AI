import asyncio
from langchain.output_parsers import PydanticOutputParser
from app.core.prompt.document_summation_prompt import (
    document_summation_prompt,
)
from app.core.util.ai_manager import AIManager
from app.core.util.document_manager import DocumentManager
from app.core.prompt.survey_creation_prompt import survey_creation_prompt
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

        targeting_sentence = ""
        indicating_group_sentence = ""

        if target != "":
            targeting_sentence = f"targeting {target}"

        if group_name != "":
            indicating_group_sentence = f"with including a statement indicating that you are part of the {group_name} team."

        document_summation_task = asyncio.create_task(
            self.__summarize_document(text_document)
        )

        survey_generation_task = asyncio.create_task(
            self.__generate_survey(
                user_prompt,
                targeting_sentence,
                indicating_group_sentence,
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
        targeting_sentence,
        indicating_group_sentence,
        text_document,
    ):
        user_prompt = await FunctionExecutionTimeMeasurer.run_async_function(
            "사용자 프롬프트 생성 태스크",
            self.ai_manager.async_chat_normal,
            f"""
            너는 의도가 모호한 사용자 요청을 해석해서 명확한 요청으로 변형시키는 요청 변환 전문가다.
            사용자가 대충 쓴 요청을 정확히 수행하기 위해서, 제공된 요청을 이해하고 복수의 단순한 요청으로 변환해야한다.
            요청이 여러 의도를 담는 복합 요청일 경우, 그 각각의 의도를 담는 단순한 요청으로 변환한다.
            이렇게 하나의 요청은 여러 요청으로 만들어진다.
            생성된 여러 요청은 다시 모델에게 전달하여 요청을 수행하게한다.
            
            요청 : {user_prompt_with_basic_prompt}
            
            하위 요청:
            """,
        )

        print(user_prompt)

        prototype_survey = await FunctionExecutionTimeMeasurer.run_async_function(
            "설문 생성 태스크",
            self.ai_manager.async_chat,
            self.survey_creation_prompt.format(
                user_prompt=user_prompt,
                targeting_sentence=targeting_sentence,
                indicating_group_sentence=indicating_group_sentence,
                document=text_document,
            ),
        )

        return self.parser_to_survey.parse(prototype_survey)

    async def __summarize_document(self, text_document):
        return await FunctionExecutionTimeMeasurer.run_async_function(
            "문서 요약 태스크",
            self.ai_manager.async_chat_with_history,
            document_summation_prompt.format(user_document=text_document),
            is_new_chat_save=True,
        )
