from typing import Dict, Any
from pydantic import BaseModel
from app.dto.model.survey_data_type import SurveyDataType


class EditWithChatRequest(BaseModel):
    session_id: str
    survey_data: Dict[str, Any]
    survey_data_type: SurveyDataType
    user_prompt: str
