from pydantic import Field

from app.dto.model.question import Question


class EditQuestionWithChatResponse(Question):
    reason: str = Field(description="Explanation for your edit")
