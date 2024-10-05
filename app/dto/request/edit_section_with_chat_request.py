from uuid import UUID
from app.dto.model.section import Section
from pydantic import BaseModel


class EditSectionWithChatRequest(BaseModel):
    chat_session_id: UUID
    section: Section
    user_prompt: str
