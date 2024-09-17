from typing import Literal
from app.model.section import Section
from pydantic import BaseModel, Field

class Survey(BaseModel):
    id: Literal[None] = Field(
        default=None
    )
    title: str = Field(
        description="Title of the survey"
    )
    description: str = Field(
        description="Greeting message at the start of the survey"
    )
    finishMessage: str = Field(
        description="Message displayed upon completion of the survey"
    )
    sections: list[Section] = Field(
        description="Sections of the survey"
    )