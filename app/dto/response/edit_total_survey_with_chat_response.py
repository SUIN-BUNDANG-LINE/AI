from pydantic import Field

from app.dto.model.survey import Survey


class EditTotalSurveyWithChatResponse(Survey):
    reason: str = Field(
        default="",
        description="Explanation in detail how the user prompt was implemented.",
    )
