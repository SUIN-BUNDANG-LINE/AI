from app.error.business_exception import business_exception
from app.error.error_code import ErrorCode
from pydantic import BaseModel, validator
from app.core.util.file_manager import FileManager

supported_extensions = [".pdf", ".txt"]
USER_PROMPT_TEXT_LIMIT = 1000

class SurveyGeneratetWithFileUrlRequest(BaseModel):
    job: str
    group_name: str
    file_url: str
    user_prompt: str

    @validator('file_url')
    def validate_file_url(cls, value):
        extension = FileManager.get_file_extension_from_url(value)
        if extension not in supported_extensions:
            raise business_exception(ErrorCode.FILE_EXTENSION_NOT_SUPPORTED)

    @validator('user_prompt')
    def validate_user_prompt(cls, value):
        if len(value) > USER_PROMPT_TEXT_LIMIT:
            raise business_exception(ErrorCode.TEXT_TOO_LONG) 
        return value
