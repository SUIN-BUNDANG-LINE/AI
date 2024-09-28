from typing import Dict, Any
from pydantic import BaseModel
from app.dto.model.survey_data_type import SurveyDataType

class EditWithChatRequest(BaseModel):
    thread_id: str
    survey_data: Dict[str, Any]  # JSON 데이터를 딕셔너리 형태로 받을 수 있습니다.
    survey_data_type: SurveyDataType
    user_prompt: str