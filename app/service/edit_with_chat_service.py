from operator import ge
from sqlalchemy import null
from app.core.util.ai_manager import AIManager
from app.core.util.document_manager import DocumentManager
from app.dto.model.survey_data_type import SurveyDataType
from app.dto.request.edit_with_chat_request import EditWitchChatRequest
from app.dto.response.survey_generate_response import * 
from app.core.prompt.generate.survey_parsing_prompt import survey_parsing_prompt
from app.core.prompt.generate.survey_creation_prompt import survey_creation_prompt
from app.core.prompt.edit.edit_total_survey_prompt import edit_total_survey_prompt
from app.core.prompt.edit.edit_section_prompt import edit_section_prompt
from app.core.prompt.edit.edit_question_prompt import edit_question_prompt

class EditWithChatService:
    def __init__(self):
        self.ai_manager =  AIManager()
        self.document_manger = DocumentManager()
        self.survey_creation_prompt = survey_creation_prompt
        self.survey_parsing_prompt = survey_parsing_prompt
        self.edit_total_survey_prompt = edit_total_survey_prompt
        self.edit_section_prompt = edit_section_prompt
        self.edit_question_prompt = edit_question_prompt

    def edit_survey(self, edit_with_chat_request:EditWitchChatRequest):
        survey_data_tpye = edit_with_chat_request.survey_data_type
        edit_propmt = self.__get_edit_prompt(survey_data_tpye)
        editted_survey = self.ai_manager.chat(edit_propmt.format(survey_data=edit_with_chat_request.survey_data))
        return editted_survey

    def __get_edit_prompt(self, survey_data_tpye: SurveyDataType):
        match survey_data_tpye:
            case SurveyDataType.TOTAL_SURVEY:
                return self.edit_total_survey_prompt
            case SurveyDataType.SECTION:
                return self.edit_section_prompt
            case SurveyDataType.QUESTION:
                return self.edit_question_prompt
            case _:
                raise business_exception(ErrorCode.INVALID_SURVEY_DATA_TYPE)