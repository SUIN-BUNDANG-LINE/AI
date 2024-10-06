from uuid import UUID
from app.dto.model.question import Question
from pydantic import BaseModel


class EditQuestionWithChatRequest(BaseModel):
    chat_session_id: UUID
    question: Question
    user_prompt: str
