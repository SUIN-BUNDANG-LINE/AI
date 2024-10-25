from typing import Optional
from typing import List
from uuid import UUID
from pydantic import BaseModel, Field

from app.dto.model.question_type import QuestionType


class Question(BaseModel):
    id: Optional[UUID] = Field(
        default=None, description="""Unique identifier or null(not "null")"""
    )
    question_type: QuestionType = Field(
        description="Type of the question: SINGLE_CHOICE, MULTIPLE_CHOICE, TEXT_RESPONSE"
    )
    title: str = Field(default="", description="Title of the question")
    description: str = Field(default="", description="Description of the question")
    is_required: bool = Field(
        description="Indicates whether answering the question is mandatory or not"
    )
    choices: Optional[List[str]] = Field(
        default=None,
        description="Options for choice question",
    )
    is_allow_other: bool = Field(
        description="Indicates whether allow users to input their own answers directly, even for questions where they select from given options or not"
    )
