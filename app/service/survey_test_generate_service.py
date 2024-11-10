from langchain.output_parsers import PydanticOutputParser
from app.core.prompt.document_summation_prompt import (
    document_summation_prompt,
)
from app.core.util.ai_manager import AIManager
from app.core.util.document_manager import DocumentManager
from app.core.prompt.survey_creation_prompt import survey_creation_prompt
from app.dto.request.survey_generate_request import (
    SurveyGenerateRequest,
)
from app.core.util.function_execution_time_measurer import FunctionExecutionTimeMeasurer
from app.dto.model.survey import Survey
from app.core.util.parallel_requestor import parallel_requestor


class SurveyTestGenerateService:
    def __init__(self):
        self.ai_manager = None
        self.document_manager = DocumentManager()
        self.survey_creation_prompt = survey_creation_prompt
        self.document_summation_prompt = document_summation_prompt
        self.parser_to_survey = PydanticOutputParser(pydantic_object=Survey)

    async def generate_test_survey(
        self, survey_generate_request: SurveyGenerateRequest
    ):
        chat_session_id = survey_generate_request.chat_session_id
        self.ai_manager = AIManager(chat_session_id)

        text_document = (
            self.document_manager.text_from_file_url(survey_generate_request.file_url)
            if survey_generate_request.file_url is not None
            else ""
        )

        await FunctionExecutionTimeMeasurer.run_async_function(
            "설문 비동기로 여러개 생성하는 태스크",
            parallel_requestor,
            self.ai_manager,
            survey_creation_prompt.format(
                reference_materials=text_document,
                target=survey_generate_request.target,
                group_name=survey_generate_request.group_name,
                user_prompt=survey_generate_request.user_prompt,
            ),
            100,
        )

        return
