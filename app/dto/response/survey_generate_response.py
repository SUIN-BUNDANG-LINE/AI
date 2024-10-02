from uuid import UUID
from pydantic import BaseModel
from app.dto.model.survey import Survey


class SurveyGenerateResponse(BaseModel):
    chatSessionId: UUID
    surveyGeneratedByAI: Survey
