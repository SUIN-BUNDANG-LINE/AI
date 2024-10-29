from pydantic import Field

from app.dto.model.section import Section


class EditSectionWithChatResponse(Section):
    reason: str = Field(
        description="Explanation in detail how the user prompt was implemented."
    )
