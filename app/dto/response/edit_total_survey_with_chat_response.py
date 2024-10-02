from app.dto.model.section import Section
from app.dto.model.survey import Survey
from pydantic import BaseModel, Field


class EditTotalSurveyWithChatResponse(BaseModel):
    title: str
    description: str
    finishMessage: str
    sections: list[Section]