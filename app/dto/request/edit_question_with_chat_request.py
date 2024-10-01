from typing import Dict, Any
from app.dto.model.question import Question
from pydantic import BaseModel
from app.dto.model.survey_data_type import SurveyDataType


class EditQuestionWithChatRequest(BaseModel):
    session_id: str
    survey_data: Question
    survey_data_type: SurveyDataType
    user_prompt: str
