import asyncio
from langchain.output_parsers import PydanticOutputParser
from app.core.prompt.document_summation_prompt import (
    document_summation_prompt,
)
from app.core.util.ai_manager import AIManager
from app.core.util.document_manager import DocumentManager
from app.core.prompt.prompt_resolve_prompt import prompt_resolve_prompt
from app.core.prompt.survey_creation_prompt import survey_creation_prompt
from app.dto.response.survey_generate_response import SurveyGenerateResponse
from app.dto.request.survey_generate_request import (
    SurveyGenerateRequest,
)
from app.core.util.function_execution_time_measurer import FunctionExecutionTimeMeasurer
from app.dto.model.survey import Survey
from app.core.util.allowed_other_manager import AllowedOtherManager


class SurveyGenerateService:
    def __init__(self):
        self.ai_manager = None
        self.survey_generate_content = None
        self.document_manger = DocumentManager()
        self.prompt_resolver_prompt = prompt_resolve_prompt
        self.survey_creation_prompt = survey_creation_prompt
        self.document_summation_prompt = document_summation_prompt
        self.parser_to_survey = PydanticOutputParser(pydantic_object=Survey)

    async def generate_survey(self, request: SurveyGenerateRequest):
        chat_session_id = request.chat_session_id

        print("chat_session_id", chat_session_id)
        self.ai_manager = AIManager(chat_session_id)
        text_document = ""
        if request.file_url is not None:
            text_document = self.document_manger.text_from_file_url(request.file_url)

        target = request.target
        group_name = request.group_name
        user_prompt = request.user_prompt

        document_summation_task = (
            asyncio.create_task(self.__summarize_document(text_document + user_prompt))
            if chat_session_id is not None
            else None
        )

        survey_generation_task = asyncio.create_task(
            self.__generate_survey(
                user_prompt,
                target,
                group_name,
                text_document,
            )
        )

        if document_summation_task:
            parsed_generated_survey, document_summation = await asyncio.gather(
                survey_generation_task, document_summation_task
            )
        else:
            parsed_generated_survey = await survey_generation_task

        return SurveyGenerateResponse(survey=parsed_generated_survey)

    async def __generate_survey(
        self,
        user_prompt,
        target,
        group_name,
        text_document,
    ):
        generated_survey = await FunctionExecutionTimeMeasurer.run_async_function(
            "설문 생성 태스크",
            self.ai_manager.async_chat,
            self.survey_creation_prompt.format(
                user_prompt=user_prompt,
                target=target,
                group_name=group_name,
                document=text_document,
            ),
            self.parser_to_survey,
        )

        parsed_survey = self.parser_to_survey.parse(generated_survey)

        return AllowedOtherManager.remove_last_choice_in_survey(parsed_survey)

    async def __summarize_document(self, text_document_and_user_prompt):
        return await FunctionExecutionTimeMeasurer.run_async_function(
            "문서 요약 태스크",
            self.ai_manager.async_chat_with_history,
            document_summation_prompt.format(
                user_document=text_document_and_user_prompt
            ),
            is_new_chat_save=True,
        )
