from app.dto.request.survey_generate_with_file_url_request import (
    SurveyGenerateWithFileUrlRequest,
)
from app.dto.request.survey_generate_with_text_document_request import (
    SurveyGenerateWithTextDocumentRequest,
)
from fastapi import APIRouter, Depends
from app.service.survey_generate_service import SurveyGenerateService

router = APIRouter()


def get_survey_generate_service():
    return SurveyGenerateService()


@router.post("/generate/survey/file-url")
async def generate_survey(
    request: SurveyGenerateWithFileUrlRequest,
    generate_service=Depends(get_survey_generate_service),
):
    return await generate_service.generate_survey_with_file_url(request)


@router.post("/generate/survey/text-document")
async def generate_survey(
    request: SurveyGenerateWithTextDocumentRequest,
    generate_service=Depends(get_survey_generate_service),
):
    return await generate_service.generate_survey_with_text_document(request)
