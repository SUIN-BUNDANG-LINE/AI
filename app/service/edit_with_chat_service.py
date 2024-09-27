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
        survey_data_tpye = edit_with_chat_request.survey_data_type
        edit_propmt = self.__get_edit_prompt(survey_data_tpye)
        parser = PydanticOutputParser(pydantic_object=Section)
        editted_result = self.ai_manager.chat_with_parser(edit_propmt.format(user_prompt=edit_with_chat_request.user_prompt, user_survey_data=edit_with_chat_request.survey_data, prototype_survey_data="""
    1. **section: JSP 사용 현황 섹션**
    - questionType: SINGLE_CHOICE
    - question: JSP를 사용하고 있습니까?
    - choices: 
        - 예
        - 아니오
    - isAllowOtherChoice: False
    - isRequired: True

    2. **section: JSP 사용 이유 섹션**
    - questionType: MULTIPLE_CHOICE
    - question: JSP를 사용하는 주된 이유는 무엇인가요? (복수 선택 가능)
    - choices: 
        - Java와의 호환성
        - 기업용 시스템 구축에 적합
        - 다양한 Java 라이브러리 사용 가능
        - JSP 컨테이너의 안정성
        - 기타 (구체적으로 기재)
    - isAllowOtherChoice: True
    - isRequired: True

    3. **section: JSP 사용 경험 섹션**
    - questionType: SINGLE_CHOICE
    - question: JSP를 사용한 경험이 얼마나 되십니까?
    - choices: 
        - 1년 미만
        - 1년 이상 3년 미만
        - 3년 이상 5년 미만
        - 5년 이상
    - isAllowOtherChoice: False
    - isRequired: True

    4. **section: JSP의 장단점 섹션**
    - questionType: TEXT_RESPONSE
    - question: JSP의 장점과 단점을 각각 한 가지씩 적어주세요.
    - isAllowOtherChoice: False
    - isRequired: True

    5. **section: JSP 대체 기술 섹션**
    - questionType: SINGLE_CHOICE
    - question: JSP 대신 사용하고 있는 다른 기술이 있습니까?
    - choices: 
        - 예
        - 아니오
    - isAllowOtherChoice: False
    - isRequired: True

    6. **section: JSP 사용 의향 섹션**
    - questionType: SINGLE_CHOICE
    - question: 앞으로 JSP를 계속 사용할 의향이 있으신가요?
    - choices: 
        - 매우 그렇다
        - 그렇다
        - 보통이다
        - 그렇지 않다
        - 전혀 그렇지 않다
    - isAllowOtherChoice: False
    - isRequired: True

    7. **section: 개인 정보 섹션**
    - questionType: SINGLE_CHOICE
    - question: 귀하의 직업군은 무엇인가요?
    - choices: 
        - 개발자
        - 시스템 관리자
        - 기획자
        - 기타
    - isAllowOtherChoice: True
    - isRequired: False

    8. **section: 개인 정보 섹션**
    - questionType: TEXT_RESPONSE
    - question: 귀하의 연령대를 적어주세요.
    - isAllowOtherChoice: False
    - isRequired: False"""), parser)
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