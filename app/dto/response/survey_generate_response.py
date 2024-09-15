from pydantic import BaseModel

# Response DTO 정의
class SurveyGenerateResponse(BaseModel):
    survey_id: int
    title: str
    description: str
    created_at: str 