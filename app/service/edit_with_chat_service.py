from app.dto.request.edit_survey_with_chat_request import EditSurveyWithChatRequest
from app.dto.request.edit_section_with_chat_request import EditSectionWithChatRequest
from app.dto.request.edit_question_with_chat_request import EditQuestionWithChatRequest
from app.core.util.ai_manager import AIManager
from app.dto.response.edit_total_survey_with_chat_response import (
    EditTotalSurveyWithChatResponse,
)
from app.dto.response.edit_section_with_chat_response import EditSectionWithChatResponse
from app.dto.response.edit_question_with_chat_response import (
    EditQuestionWithChatResponse,
)
from langchain.output_parsers import PydanticOutputParser
from app.core.prompt.edit.edit_survey_prompt import edit_survey_prompt
from app.core.prompt.edit.edit_section_prompt import edit_section_prompt
from app.core.prompt.edit.edit_question_prompt import edit_question_prompt
from app.core.prompt.generate.survey_parsing_prompt import survey_parsing_prompt


class EditWithChatService:
    def __init__(self):
        self.ai_manager = None
        self.edit_survey_prompt = edit_survey_prompt
        self.edit_section_prompt = edit_section_prompt
        self.edit_question_prompt = edit_question_prompt
        self.survey_parsing_prompt = survey_parsing_prompt
        self.parser_to_survey = PydanticOutputParser(
            pydantic_object=EditTotalSurveyWithChatResponse
        )
        self.parser_to_section = PydanticOutputParser(
            pydantic_object=EditSectionWithChatResponse
        )
        self.parser_to_question = PydanticOutputParser(
            pydantic_object=EditQuestionWithChatResponse
        )

    def edit_total_survey(self, request: EditSurveyWithChatRequest):
        self.ai_manager = AIManager(request.chat_session_id)

        formatted_edit_prompt = self.edit_survey_prompt.format(
            user_prompt=request.user_prompt,
            user_survey=request.survey.model_dump_json(),
        )

        return self.__edit_survey_data(formatted_edit_prompt)

    def edit_section(self, request: EditSectionWithChatRequest):
        self.ai_manager = AIManager(request.chat_session_id)

        formatted_edit_prompt = self.edit_survey_prompt.format(
            user_prompt=request.user_prompt,
            user_survey=request.section.model_dump_json(),
        )

        return self.__edit_survey_data(formatted_edit_prompt)

    def edit_question(self, request: EditQuestionWithChatRequest):
        self.ai_manager = AIManager(request.chat_session_id)

        formatted_edit_prompt = self.edit_survey_prompt.format(
            user_prompt=request.user_prompt,
            user_survey=request.question.model_dump_json(),
        )

        return self.__edit_survey_data(formatted_edit_prompt)

    def __edit_survey_data(self, formatted_edit_prompt):
        edited_survey = self.ai_manager.chat_with_history(
            prompt=formatted_edit_prompt, is_new_chat_save=False
        )

        edited_survey_has_parsing_format = self.ai_manager.chat_with_parser(
            prompt=self.survey_parsing_prompt.format(prototype_survey=edited_survey),
            parser=self.parser_to_survey,
        )

        return self.parser_to_survey.parse(edited_survey_has_parsing_format)
