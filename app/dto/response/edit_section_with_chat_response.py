from app.dto.model import question
from app.dto.model.question import Question
from app.dto.model.section import Section
from pydantic import BaseModel


class EditSectionWithChatResponse(BaseModel):
    title: str
    description: str
    questions: list[Question]