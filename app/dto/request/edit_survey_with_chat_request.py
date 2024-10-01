from typing import Dict, Any
from app.dto.model.survey import Survey
from pydantic import BaseModel
from app.dto.model.survey_data_type import SurveyDataType


class EditSurveyWithChatRequest(BaseModel):
    session_id: str
    survey_data: Survey
    survey_data_type: SurveyDataType
    user_prompt: str
