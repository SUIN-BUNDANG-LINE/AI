from typing import Optional

from app.dto.model.section import Section
from pydantic import BaseModel, Field
from uuid import UUID


class Survey(BaseModel):
    id: Optional[UUID] = Field(
        default=None, description="""Unique identifier or null(not "null")"""
    )
    title: str = Field(description="Title of the survey")
    description: str = Field(description="Greeting message at the start of the survey")
    finish_message: str = Field(
        description="Message displayed upon completion of the survey"
    )
    sections: Optional[list[Section]] = Field(
        default_factory=list, description="Sections of the survey"
    )
