from typing import Optional

from app.dto.model.section import Section
from pydantic import BaseModel, Field, UUID4


class Survey(BaseModel):
    id: Optional[UUID4] = Field(default=None, description="Unique identifier or null")
    title: str = Field(description="Title of the survey")
    description: str = Field(description="Greeting message at the start of the survey")
    finish_message: str = Field(
        description="Message displayed upon completion of the survey"
    )
    sections: list[Section] = Field(description="Sections of the survey")
