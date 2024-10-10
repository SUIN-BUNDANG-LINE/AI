from math import e
from app.dto.request.edit_survey_with_chat_request import EditSurveyWithChatRequest
from app.dto.request.edit_section_with_chat_request import EditSectionWithChatRequest
from app.dto.request.edit_question_with_chat_request import EditQuestionWithChatRequest
from app.core.util.ai_manager import AIManager
from app.core.util.document_manager import DocumentManager
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
        self.ai_manager = AIManager()
        self.document_manger = DocumentManager()
        self.edit_survey_prompt = edit_survey_prompt
        self.edit_section_prompt = edit_section_prompt
        self.edit_question_prompt = edit_question_prompt
        self.survey_parsing_prompt = survey_parsing_prompt

    def edit_total_survey(self, request: EditSurveyWithChatRequest):
        formatted_edit_prompt = self.edit_survey_prompt.format(
            user_prompt=request.user_prompt,
            user_survey=request.survey.model_dump_json(),
        )

        edited_survey = self.__chat_ai_for_edit_survey_data(
            prompt=formatted_edit_prompt, session_id=request.chat_session_id
        )

        parser_to_survey = PydanticOutputParser(
            pydantic_object=EditTotalSurveyWithChatResponse
        )

        edited_survey_has_parsing_format = self.__chat_ai_for_parsing(
            prompt=self.survey_parsing_prompt.format(prototype_survey=edited_survey),
            parser=parser_to_survey,
        )

        parsed_edited_survey = parser_to_survey.parse(edited_survey_has_parsing_format)

        return parsed_edited_survey

    def edit_section(self, request: EditSectionWithChatRequest):
        formatted_edit_prompt = self.edit_section_prompt.format(
            user_prompt=request.user_prompt,
            user_section=request.model_dump_json(),
        )

        edited_section = self.__chat_ai_for_edit_survey_data(
            prompt=formatted_edit_prompt, session_id=request.chat_session_id
        )

        parser_to_section = PydanticOutputParser(
            pydantic_object=EditSectionWithChatResponse
        )

        edited_section_has_parsing_format = self.__chat_ai_for_parsing(
            prompt=self.survey_parsing_prompt.format(prototype_survey=edited_section),
            parser=parser_to_section,
        )

        parsed_edited_section = parser_to_section.parse(
            edited_section_has_parsing_format
        )
        return parsed_edited_section

    def edit_question(self, request: EditQuestionWithChatRequest):
        formatted_edit_prompt = self.edit_question_prompt.format(
            user_prompt=request.user_prompt,
            user_question=request.question.model_dump_json(),
        )

        edited_question = self.__chat_ai_for_edit_survey_data(
            prompt=formatted_edit_prompt, session_id=request.chat_session_id
        )

        parser_to_question = PydanticOutputParser(
            pydantic_object=EditQuestionWithChatResponse
        )

        edited_question_has_parsing_format = self.__chat_ai_for_parsing(
            prompt=self.survey_parsing_prompt.format(prototype_survey=edited_question),
            parser=parser_to_question,
        )

        parsed_edited_question = parser_to_question.parse(
            edited_question_has_parsing_format
        )
        return parsed_edited_question

    def __chat_ai_for_edit_survey_data(self, prompt, session_id):
        edited_result = self.ai_manager.chat_with_history(
            prompt=prompt, session_id=session_id, is_new_chat_save=False
        )

        return edited_result

    def __chat_ai_for_parsing(self, prompt, parser):
        edited_result = self.ai_manager.chat_with_parser(prompt=prompt, parser=parser)

        return edited_result
