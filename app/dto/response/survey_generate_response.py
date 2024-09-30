from uuid import UUID
from pydantic import BaseModel
from app.dto.model.survey import Survey

class SurveyGenerateResponse(BaseModel):
    chat_session_id: UUID
    generated_survey: Survey