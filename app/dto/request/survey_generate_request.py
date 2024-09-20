from pydantic import BaseModel

class SurveyGenerateRequestWithFileUrl(BaseModel):
    job: str
    group_name: str
    file_url : str
    user_prompt: str

class SurveyGenerateRequestWithTextDocument(BaseModel):
    job: str
    group_name: str
    text : str
    user_prompt: str