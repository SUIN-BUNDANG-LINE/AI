from app.error.business_exception import business_exception
from app.error.error_code import ErrorCode
from pydantic import BaseModel, validator

DOCUMENTS_TEXT_LIMIT = 12000
USER_PROMPT_TEXT_LIMIT = 1000


class SurveyGenerateWithTextDocumentRequest(BaseModel):
    job: str
    group_name: str
    text_document: str
    user_prompt: str

    @validator('text_document')
    def validate_text_document(cls, value):
        if len(value) > DOCUMENTS_TEXT_LIMIT:
            raise business_exception(ErrorCode.TEXT_TOO_LONG)
        return value

    @validator('user_prompt')
    def validate_user_prompt(cls, value):
        if len(value) > USER_PROMPT_TEXT_LIMIT:
            raise business_exception(ErrorCode.TEXT_TOO_LONG)
        return value
