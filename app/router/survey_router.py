from app.dto.request.survey_generate_request import SurveyGenerateRequest
from fastapi import APIRouter, Depends
from app.service.survey_serivce import GenerateService

router = APIRouter()

def get_generate_serivce():
    return GenerateService()

@router.post("/generate/survey")
def create_item(request: SurveyGenerateRequest, generate_service = Depends(get_generate_serivce)):
    return generate_service.generate_survey(request.who.to_string(), request.group_name, request.file_url)