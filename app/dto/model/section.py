from typing import Optional
from app.dto.model.question import Question
from pydantic import BaseModel, Field, UUID4


class Section(BaseModel):
    id: Optional[UUID4] = Field(default=None, description="Unique identifier or null")
    title: str = Field(description="Title of the section")
    description: str = Field(description="Description of the section")
    questions: list[Question] = Field(description="Questions included in the section")
