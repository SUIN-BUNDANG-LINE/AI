import os
from urllib.parse import urlparse
from app.core.util.ai_manager import AIManager
from app.core.util.document_manager import DocumentManager
from app.dto.response.survey_generate_response import * 
from app.core.prompt.survey_parsing_prompt import survey_parsing_prompt
from app.core.prompt.survey_creation_prompt import survey_creation_prompt

class EditWithChatService:
    def __init__(self):
        self.ai_manager =  AIManager()
        self.document_manger = DocumentManager()
        self.survey_creation_prompt = survey_creation_prompt
        self.survey_parsing_prompt = survey_parsing_prompt
    def edit_survey():
        pass