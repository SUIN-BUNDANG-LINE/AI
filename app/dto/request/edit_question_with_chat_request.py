from app.dto.model.question import Question
from pydantic import BaseModel


class EditQuestionWithChatRequest(BaseModel):
    session_id: str
    question: Question
    user_prompt: str
