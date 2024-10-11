from typing import Optional
from typing import List
from uuid import UUID
from pydantic import BaseModel, Field

from app.dto.model.question_type import QuestionType


class Question(BaseModel):
    id: Optional[UUID] = Field(default=None, description="Unique identifier or null")
    question_type: QuestionType = Field(
        description="Type of the question: SINGLE_CHOICE, MULTIPLE_CHOICE, TEXT_RESPONSE"
    )
    title: str = Field(description="Title of the question")
    is_required: bool = Field(
        description="Indicates whether answering the question is mandatory"
    )
    choices: Optional[List[str]] = Field(
        default=None, description="Options for multiple-choice questions (can be null)"
    )
    is_allow_other: bool = Field(
        description="Indicates whether to allow an 'Other' response for multiple-choice questions"
    )
