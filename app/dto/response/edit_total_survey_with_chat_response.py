from pydantic import Field

from app.dto.model.survey import Survey


class EditTotalSurveyWithChatResponse(Survey):
    reason: str = Field(description="Explanation for your edit")
