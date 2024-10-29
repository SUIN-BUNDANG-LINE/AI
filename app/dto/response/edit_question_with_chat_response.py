from pydantic import Field

from app.dto.model.question import Question


class EditQuestionWithChatResponse(Question):
    reason: str
