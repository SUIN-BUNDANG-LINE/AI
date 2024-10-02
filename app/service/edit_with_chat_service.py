from math import e
from app.dto.request.edit_survey_with_chat_request import EditSurveyWithChatRequest
from app.dto.request.edit_section_with_chat_request import EditSectionWithChatRequest
from app.dto.request.edit_question_with_chat_request import EditQuestionWithChatRequest
from app.core.util.ai_manager import AIManager
from app.core.util.document_manager import DocumentManager
from app.dto.response.edit_total_survey_with_chat_response import EditTotalSurveyWithChatResponse
from app.dto.response.edit_section_with_chat_response import EditSectionWithChatResponse
from app.dto.response.edit_question_with_chat_response import EditQuestionWithChatResponse
from langchain.output_parsers import PydanticOutputParser
from app.core.prompt.edit.edit_total_survey_prompt import edit_total_survey_prompt
from app.core.prompt.edit.edit_section_prompt import edit_section_prompt
from app.core.prompt.edit.edit_question_prompt import edit_question_prompt


class EditWithChatService:

    def __init__(self):
        self.ai_manager = AIManager()
        self.document_manger = DocumentManager()
        self.edit_total_survey_prompt = edit_total_survey_prompt
        self.edit_section_prompt = edit_section_prompt
        self.edit_question_prompt = edit_question_prompt

    def edit_total_survey(self, request: EditSurveyWithChatRequest):
        parser_to_survey = PydanticOutputParser(
            pydantic_object=EditTotalSurveyWithChatResponse)
        formatted_edit_prompt = edit_total_survey_prompt.format(
            user_prompt=request.user_prompt,
            user_survey_data=request.survey_data.json())

        edit_survey_data_content = self._EditSurveyDataContent(
            formatted_edit_prompt=formatted_edit_prompt,
            session_id=request.session_id,
            parser=parser_to_survey)

        editted_result = self.__chat_ai_for_edit_survey_data(
            edit_survey_data_content)
        parsed_result = parser_to_survey.parse(editted_result)
        return parsed_result

    def edit_section(self, request: EditSectionWithChatRequest):
        parser_to_section = PydanticOutputParser(
            pydantic_object=EditSectionWithChatResponse)
        formatted_edit_prompt = edit_total_survey_prompt.format(
            user_prompt=request.user_prompt,
            user_survey_data=request.survey_data.json())

        edit_survey_data_content = self._EditSurveyDataContent(
            formatted_edit_prompt=formatted_edit_prompt,
            session_id=request.session_id,
            parser=parser_to_section)

        editted_result = self.__chat_ai_for_edit_survey_data(
            edit_survey_data_content)
        parsed_result = parser_to_section.parse(editted_result)
        return parsed_result

    def edit_question(self, request: EditQuestionWithChatRequest):
        parser_to_question = PydanticOutputParser(
            pydantic_object=EditQuestionWithChatResponse)
        formatted_edit_prompt = edit_total_survey_prompt.format(
            user_prompt=request.user_prompt,
            user_survey_data=request.survey_data.json())

        edit_survey_data_content = self._EditSurveyDataContent(
            formatted_edit_prompt=formatted_edit_prompt,
            session_id=request.session_id,
            parser=parser_to_question)

        editted_result = self.__chat_ai_for_edit_survey_data(
            edit_survey_data_content)
        parsed_result = parser_to_question.parse(editted_result)
        return parsed_result

    # private
    class _EditSurveyDataContent:

        def __init__(self, formatted_edit_prompt: str, session_id: str,
                     parser: PydanticOutputParser):
            self.formatted_edit_prompt = formatted_edit_prompt
            self.session_id = session_id
            self.parser = parser

    def __chat_ai_for_edit_survey_data(
            self, edit_survey_data_content: _EditSurveyDataContent):
        editted_result = self.ai_manager.chat_with_history_and_parser(
            prompt=edit_survey_data_content.formatted_edit_prompt,
            session_id=edit_survey_data_content.session_id,
            is_new_chat_save=False,
            parser=edit_survey_data_content.parser)

        return editted_result
