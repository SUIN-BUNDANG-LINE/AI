from typing import Optional
from app.dto.model.question import Question
from pydantic import BaseModel, Field
from uuid import UUID


class Section(BaseModel):
    id: Optional[UUID] = Field(
        default=None, description="""Unique identifier or null(not "null")"""
    )
    title: str = Field(default="", description="Title of the section")
    description: str = Field(default="", description="Description of the section")
    questions: Optional[list[Question]] = Field(
        default_factory=list, description="Questions included in the section"
    )
