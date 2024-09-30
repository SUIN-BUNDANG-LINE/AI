from app.dto.request.edit_with_chat_request import EditWithChatRequest
from app.dto.model.survey_data_type import SurveyDataType
from app.core.util.ai_manager import AIManager
from app.core.util.document_manager import DocumentManager
from langchain.output_parsers import PydanticOutputParser
from app.dto.model.section import Section
from app.core.prompt.edit.edit_total_survey_prompt import edit_total_survey_prompt
from app.core.prompt.edit.edit_section_prompt import edit_section_prompt
from app.core.prompt.edit.edit_question_prompt import edit_question_prompt
from app.error.error_code import ErrorCode
from app.error.business_exception import business_exception

class EditWithChatService:
    def __init__(self):
        self.ai_manager =  AIManager()
        self.document_manger = DocumentManager()
        self.edit_total_survey_prompt = edit_total_survey_prompt
        self.edit_section_prompt = edit_section_prompt
        self.edit_question_prompt = edit_question_prompt

    def edit_survey(self, edit_with_chat_request:EditWithChatRequest):
        survey_data_type = edit_with_chat_request.survey_data_type
        edit_propmt = self.__get_edit_prompt(survey_data_type)
        parser = PydanticOutputParser(pydantic_object=Section)
        editted_result = self.ai_manager.chat_with_history_and_parser(
            edit_propmt.format(user_prompt=edit_with_chat_request.user_prompt, 
            user_survey_data=edit_with_chat_request.survey_data), 
            edit_with_chat_request.thread_id,
            is_save=False,
            parser=parser
        )
        parsed_result = parser.parse(editted_result)
        return parsed_result


    def __get_edit_prompt(self, survey_data_tpye: SurveyDataType):
        match survey_data_tpye:
            case SurveyDataType.TOTAL_SURVEY:
                return self.edit_total_survey_prompt
            case SurveyDataType.SECTION:
                return self.edit_section_prompt
            case SurveyDataType.QUESTION:
                return self.edit_question_prompt
            case _:
                raise business_exception(ErrorCode.FILE_EXTENSION_NOT_SUPPORTED)