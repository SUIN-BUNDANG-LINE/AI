from pydantic import BaseModel

class SurveyGenerateRequestWithFileUrl(BaseModel):
    job: str
    group_name: str
    file_url : str

class SurveyGenerateRequestWithTextDocument(BaseModel):
    job: str
    group_name: str
    text_document : str
