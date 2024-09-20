from pydantic import BaseModel

class SurveyGenerateRequest(BaseModel):
    job: str
    group_name: str
    file_url : str