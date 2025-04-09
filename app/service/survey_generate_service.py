import asyncio

from langchain.output_parsers import PydanticOutputParser

from app.core.prompt.document_summation_prompt import (
    document_summation_prompt,
)
from app.core.prompt.survey_creation_prompt import survey_creation_prompt
from app.core.util.ai_manager import AIManager
from app.core.util.allowed_other_manager import AllowedOtherManager
from app.core.util.document_manager import DocumentManager
from app.core.util.function_execution_time_measurer import FunctionExecutionTimeMeasurer
from app.core.util.improve_user_prompt_with_search_chat import (
    get_user_prompt_with_searched_result,
)
from app.dto.model.survey import Survey
from app.dto.request.survey_generate_request import (
    SurveyGenerateRequest,
)
from app.dto.response.survey_generate_response import SurveyGenerateResponse


class SurveyGenerateService:
    def __init__(self):
        self.ai_manager = None
        self.document_manager = DocumentManager()
        self.survey_creation_prompt = survey_creation_prompt
        self.document_summation_prompt = document_summation_prompt
        self.parser_to_survey = PydanticOutputParser(pydantic_object=Survey)

    async def generate_survey_with_document_summation(
        self, survey_generate_request: SurveyGenerateRequest
    ):
        chat_session_id = survey_generate_request.chat_session_id
        self.ai_manager = AIManager(chat_session_id)

        user_prompt = get_user_prompt_with_searched_result(
            ai_manager=self.ai_manager, user_prompt=survey_generate_request.user_prompt
        )

        text_document = (
            self.document_manager.text_from_file_url(survey_generate_request.file_url)
            if survey_generate_request.file_url is not None
            else ""
        )

        document_summation_task = (
            asyncio.create_task(self.__summarize_document(text_document + user_prompt))
            if chat_session_id is not None
            else None
        )

        survey_generation_task = asyncio.create_task(
            self.__generate_survey(
                survey_generate_request.target,
                survey_generate_request.group_name,
                text_document,
                user_prompt,
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
        target,
        group_name,
        text_document,
        user_prompt,
    ):
        generated_survey = await FunctionExecutionTimeMeasurer.run_async_function(
            "설문 생성 태스크",
            self.ai_manager.async_chat,
            self.survey_creation_prompt.format(
                reference_materials=text_document + user_prompt,
                user_prompt=user_prompt,
                target=target,
                group_name=group_name,
            ),
            self.parser_to_survey,
        )

        parsed_survey = self.parser_to_survey.parse(generated_survey)
        print(parsed_survey.reason)

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
