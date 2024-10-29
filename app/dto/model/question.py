from typing import Optional
from typing import List
from uuid import UUID
from pydantic import BaseModel, Field

from app.dto.model.question_type import QuestionType


class Question(BaseModel):
    id: Optional[UUID] = Field(default=None)
    question_type: QuestionType
    title: str = Field(default="")
    description: str = Field(default="")
    is_required: bool
    choices: Optional[List[str]] = Field(
        default=None,
    )
    is_allow_other: bool
