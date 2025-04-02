from pydantic import Field

from app.dto.model.question import Question


class EditQuestionWithChatResponse(Question):
    reason: str = Field(
        default="",
        description="Explanation in detail how the user prompt was implemented.",
    )
