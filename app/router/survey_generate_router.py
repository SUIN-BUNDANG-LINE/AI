from app.dto.request.survey_generate_request import SurveyGenerateRequest
from fastapi import APIRouter, Depends
from app.service.survey_generate_serivce import SurveyGenerateService

router = APIRouter()

def get_survey_generate_serivce():
    return SurveyGenerateService()

@router.post("/generate/survey")
def generate_survey(request: SurveyGenerateRequest, generate_service = Depends(get_survey_generate_serivce)):
    return generate_service.generate_survey(request.who.to_string(), request.group_name, request.file_url)