from uuid import UUID
from app.dto.model.survey import Survey
from pydantic import BaseModel


class EditSurveyWithChatRequest(BaseModel):
    chat_session_id: UUID
    survey: Survey
    user_prompt: str
