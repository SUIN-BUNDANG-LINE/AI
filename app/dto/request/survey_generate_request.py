from typing import Optional
from uuid import UUID
from app.core.error.business_exception import business_exception
from app.core.error.error_code import ErrorCode
from pydantic import BaseModel, field_validator
from app.core.util.file_manager import FileManager

SUPPORTED_EXTENSIONS = [".pdf", ".txt", ".docx", ".pptx"]
USER_PROMPT_TEXT_LIMIT = 20000


class SurveyGenerateRequest(BaseModel):
    chat_session_id: Optional[UUID]
    target: str
    group_name: str
    keyword: str
    file_url: Optional[str]
    user_prompt: str

    @field_validator("file_url")
    def validate_file_url(cls, value):
        if value is None:
            return value
        extension = FileManager.get_file_extension_from_url(value)
        if extension not in SUPPORTED_EXTENSIONS:
            raise business_exception(ErrorCode.FILE_EXTENSION_NOT_SUPPORTED)
        return value

    @field_validator("user_prompt")
    def validate_user_prompt(cls, value):
        if len(value) > USER_PROMPT_TEXT_LIMIT:
            raise business_exception(ErrorCode.TEXT_TOO_LONG)
        return value
