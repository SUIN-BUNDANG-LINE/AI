from app.dto.model.section import Section
from pydantic import BaseModel


class EditSectionWithChatRequest(BaseModel):
    session_id: str
    section: Section
    user_prompt: str
