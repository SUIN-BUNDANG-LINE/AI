from app.dto.model.survey import Survey
from pydantic import BaseModel


class EditSurveyWithChatRequest(BaseModel):
    session_id: str
    survey: Survey
    user_prompt: str
