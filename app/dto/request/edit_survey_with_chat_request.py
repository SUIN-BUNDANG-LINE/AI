from app.dto.model.survey import Survey
from pydantic import BaseModel


class EditSurveyWithChatRequest(BaseModel):
    session_id: str
    survey_data: Survey
    user_prompt: str
