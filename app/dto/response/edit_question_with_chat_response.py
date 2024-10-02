from typing import Optional
from typing import List
from pydantic import BaseModel
from app.dto.model.question import Question
from app.dto.model.question_type import QuestionType


class EditQuestionWithChatResponse(BaseModel):
    questionType: QuestionType
    title: str
    isRequired: bool
    choices: Optional[List[str]]
    isAllowOther: bool
