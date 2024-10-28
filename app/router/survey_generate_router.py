from app.dto.request.survey_generate_request import (
    SurveyGenerateRequest,
)
from fastapi import APIRouter, Depends
from app.service.survey_generate_service import SurveyGenerateService

router = APIRouter()


def get_survey_generate_service():
    return SurveyGenerateService()


@router.post("/generate/survey")
async def generate_survey(
    request: SurveyGenerateRequest,
    generate_service=Depends(get_survey_generate_service),
):
    return await generate_service.generate_survey_with_document_summation(request)
