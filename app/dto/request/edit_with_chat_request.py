from sqlalchemy import JSON
from pydantic import BaseModel
from app.dto.model.survey_data_type import SurveyDataType

class EditWithChatRequest(BaseModel):
    thread_id: str
    survey_data: str
    survey_data_type: SurveyDataType
    user_prompt: str