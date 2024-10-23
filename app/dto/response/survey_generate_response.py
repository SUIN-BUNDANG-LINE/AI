from pydantic import BaseModel
from app.dto.model.survey import Survey


class SurveyGenerateResponse(BaseModel):
    survey: Survey
