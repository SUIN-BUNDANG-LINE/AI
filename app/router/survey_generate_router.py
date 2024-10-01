from app.dto.request.survey_generate_with_file_url_request import SurveyGeneratetWithFileUrlRequest
from app.dto.request.survey_generate_with_text_document_request import SurveyGenerateWithTextDocumentRequest
from fastapi import APIRouter, Depends
from app.service.survey_generate_serivce import SurveyGenerateService

router = APIRouter()


def get_survey_generate_serivce():
    return SurveyGenerateService()


@router.post("/generate/survey/file-url")
def generate_survey(request: SurveyGeneratetWithFileUrlRequest,
                    generate_service=Depends(get_survey_generate_serivce)):
    return generate_service.generate_survey_with_file_url(request)


@router.post("/generate/survey/text-document")
def generate_survey(request: SurveyGenerateWithTextDocumentRequest,
                    generate_service=Depends(get_survey_generate_serivce)):
    return generate_service.generate_survey_with_text_document(request)
