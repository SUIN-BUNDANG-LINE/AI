from click import edit
from app.dto.request.edit_with_chat_request import EditWithChatRequest
from app.dto.model.survey_data_type import SurveyDataType
from app.core.util.ai_manager import AIManager
from app.core.util.document_manager import DocumentManager
from langchain.output_parsers import PydanticOutputParser
from app.dto.model.survey import Survey
from app.dto.model.section import Section
from app.dto.model.question import Question
from app.core.prompt.edit.edit_total_survey_prompt import edit_total_survey_prompt
from app.core.prompt.edit.edit_section_prompt import edit_section_prompt
from app.core.prompt.edit.edit_question_prompt import edit_question_prompt
from app.error.error_code import ErrorCode
from app.error.business_exception import business_exception
from langchain.prompts import PromptTemplate

class EditWithChatService:
    def __init__(self):
        self.ai_manager =  AIManager()
        self.document_manger = DocumentManager()
        self.edit_total_survey_prompt = edit_total_survey_prompt
        self.edit_section_prompt = edit_section_prompt
        self.edit_question_prompt = edit_question_prompt

    def edit_survey(self, request:EditWithChatRequest):
        edit_content = self.__get_edit_prompt(request.survey_data_type)
        
        parser = edit_content.parser

        editted_result = self.ai_manager.chat_with_history_and_parser(
            prompt=edit_content.edit_prompt.format(user_prompt=request.user_prompt, 
            user_survey_data=request.survey_data), 
            session_id=request.session_id,
            is_save=False,
            parser=parser
        )
        parsed_result = parser.parse(editted_result)
        return parsed_result

    # private
    class _EditContent:
        def __init__(self, edit_prompt: PromptTemplate, parser: PydanticOutputParser):
            self.edit_prompt = edit_prompt
            self.parser = parser
    
    def __get_edit_prompt(self, survey_data_type: SurveyDataType):
        match survey_data_type:
            case SurveyDataType.TOTAL_SURVEY:
                return self._EditContent(self.edit_total_survey_prompt, PydanticOutputParser(pydantic_object=Survey))
            case SurveyDataType.SECTION:
                return self._EditContent(self.edit_total_survey_prompt, PydanticOutputParser(pydantic_object=Section))
            case SurveyDataType.QUESTION:
                return self._EditContent(self.edit_total_survey_prompt, PydanticOutputParser(pydantic_object=Question))
            case _:
                raise business_exception(ErrorCode.INVALID_SURVEY_DATA_TYPE)