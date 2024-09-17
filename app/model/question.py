from typing import Literal
from typing import List
from pydantic import BaseModel, Field
from app.model.question_type import QuestionType

class Question(BaseModel):
    id: Literal[None] = Field(
        default=None
    )
    questionType: QuestionType = Field(
        description="Type of the question: SINGLE_CHOICE for single choice, MULTIPLE_CHOICE for multiple choices, TEXT_RESPONSE for text response"
    )
    title: str = Field(
        description="Content of the question"
    )
    description: str = Field(
        description="Description of the question"
    )
    isRequired: bool = Field(
        description="Indicates whether answering the question is mandatory"
    )
    choices: List[str] = Field(
        description="Options for multiple-choice questions"
    )
    isAllowedOther: bool = Field(       
        description="Indicates whether to allow an 'Other' response for multiple-choice questions"
    )