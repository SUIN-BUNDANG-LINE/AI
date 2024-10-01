from typing import Dict, Any
from app.dto.model.section import Section
from pydantic import BaseModel
from app.dto.model.survey_data_type import SurveyDataType


class EditSectionWithChatRequest(BaseModel):
    session_id: str
    survey_data: Section
    survey_data_type: SurveyDataType
    user_prompt: str
