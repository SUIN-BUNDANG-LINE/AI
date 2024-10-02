from app.dto.request.edit_survey_with_chat_request import EditSurveyWithChatRequest
from app.dto.request.edit_section_with_chat_request import EditSectionWithChatRequest
from app.dto.request.edit_question_with_chat_request import EditQuestionWithChatRequest
from fastapi import APIRouter, Depends
from app.service.edit_with_chat_service import EditWithChatService

router = APIRouter()


def get_edit_with_chat_service():
    return EditWithChatService()


@router.post("/chat/edit/survey")
def edit_survey(editWithChatRequest: EditSurveyWithChatRequest,
                edit_with_chat_service=Depends(get_edit_with_chat_service)):
    return edit_with_chat_service.edit_total_survey(editWithChatRequest)


@router.post("/chat/edit/seciton")
def edit_section(editWithChatRequest: EditSectionWithChatRequest,
                 edit_with_chat_service=Depends(get_edit_with_chat_service)):
    return edit_with_chat_service.edit_section(editWithChatRequest)


@router.post("/chat/edit/question")
def edit_question(editWithChatRequest: EditQuestionWithChatRequest,
                  edit_with_chat_service=Depends(get_edit_with_chat_service)):
    return edit_with_chat_service.edit_question(editWithChatRequest)
