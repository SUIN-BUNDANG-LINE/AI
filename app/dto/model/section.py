from typing import Optional

from pydantic.v1 import root_validator

from app.dto.model.question import Question
from pydantic import BaseModel, Field
from uuid import UUID


class Section(BaseModel):
    id: Optional[UUID] = Field(default=None)
    title: str = Field(default="")
    description: str = Field(default="")
    questions: Optional[list[Question]] = Field(default_factory=list)
