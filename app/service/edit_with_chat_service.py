import os
from urllib.parse import urlparse
from app.core.util.ai_manager import AIManager
from app.core.util.document_manager import DocumentManager
from app.core.prompt.survey_generate_prompt import *
from app.dto.response.survey_generate_response import * 
from langchain.output_parsers import PydanticOutputParser
from app.core.prompt.survey_guide_prompt import survey_guide_prompt
from app.error.error_code import ErrorCode
from app.error.business_exception import business_exception


class EditWithChatService:
    def __init__(self):
        self.ai_manager =  AIManager()
        self.document_manger = DocumentManager()
        self.summation_prompt = summation_prompt
        self.instruct_prompt = instruct_prompt

    def edit_survey():
        pass