
from typing import Literal
from uuid import UUID
from app.model.question import Question
from pydantic import BaseModel, Field

class Section(BaseModel):
    id: Literal[None] = Field(
        default=None
    )
    title: str = Field(
        description="Title of the section"
    )
    description: str = Field(
        description="Description of the section"
    )
    questions: list[Question] = Field(
        description="Questions included in the section"
    )
    routeDetails: Literal[None] = Field(
        default=None
    )