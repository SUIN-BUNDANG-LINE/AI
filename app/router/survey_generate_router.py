from app.dto.request.survey_generate_request import *
from fastapi import APIRouter, Depends
from app.service.survey_generate_serivce import SurveyGenerateService

router = APIRouter()

def get_survey_generate_serivce():
    return SurveyGenerateService()

@router.post("/generate/survey/file-url")
def generate_survey(request: SurveyGenerateRequestWithFileUrl, generate_service = Depends(get_survey_generate_serivce)):
    return generate_service.generate_survey_with_file_url(request.job, request.group_name, request.file_url, request.user_prompt)

@router.post("/generate/survey/text-document")
def generate_survey(request: SurveyGenerateRequestWithTextDocument, generate_service = Depends(get_survey_generate_serivce)):
    return generate_service.generate_survey_with_text_document(request.job, request.group_name, request.text_document, request.user_prompt)