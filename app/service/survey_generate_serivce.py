import time
import os
from urllib.parse import urlparse
from langchain.output_parsers import PydanticOutputParser

from app.core.util.ai_manager import AIManager
from app.core.util.document_manager import DocumentManager
from app.core.prompt.survey_creation_guide_prompt import survey_creation_guide_prompt
from app.core.prompt.survey_generation_prompt import survey_generation_prompt
from app.core.prompt.question_suggestion_prompt import question_suggestion_prompt
from app.dto.response.survey_generate_response import *
from app.error.error_code import ErrorCode
from app.error.business_exception import business_exception

class SurveyGenerateService:
    def __init__(self):
        self.ai_manager =  AIManager()
        self.document_manger = DocumentManager()
        self.question_suggestion_prompt = question_suggestion_prompt
        self.survey_generation_prompt = survey_generation_prompt

    def generate_survey_with_file_url(self, job: str, group:str, file_url: str, user_prompt: str):
        text_document = self.__get_text_document_with_validation_file_url(file_url)

        return self.__generate_survey(job, group, text_document, user_prompt)
    
    def generate_survey_with_text_document(self, job: str, group:str, text_document: str, user_prompt: str):
        self.document_manger.validate_text_length(text_document)

        return self.__generate_survey(job, group, text_document, user_prompt)

    # private methods
    def __generate_survey(self, job: str, group:str, text_document: str, user_prompt: str):
        self.document_manger.validate_text_length(text_document)

        # 제 1번 호출
        start_time = time.time() 
        suggested_question = self.ai_manager.chat(self.question_suggestion_prompt.format(user_prompt=user_prompt, document=text_document, guide=survey_creation_guide_prompt))
        print(suggested_question)
        end_time = time.time()
        execution_time = end_time - start_time  # 실행 시간 계산
        print(f"제 1번 호출 : {execution_time:.4f} seconds")

        # 제 2번 호출
        start_time = time.time() 
        parser = PydanticOutputParser(pydantic_object=SurveyGenerateResponse)
        generated_reuslt = self.ai_manager.chat_with_parser(survey_generation_prompt.format(job=job, suggested_question=suggested_question), parser)
        end_time = time.time()
        execution_time = end_time - start_time  # 실행 시간 계산
        print(f"제 2번 호출 : {execution_time:.4f} seconds")

        parsed_result = parser.parse(generated_reuslt)
        return parsed_result
    
    def __get_text_document_with_validation_file_url(self, file_url: str):
        extension = self.__get_file_extension_from_url(file_url)
        text_document = ""
        match extension:
            case ".pdf":
                text_document = self.document_manger.text_from_pdf_file_url(file_url)
            case ".txt":
                text_document = self.document_manger.text_from_txt_file_url(file_url)
            case _:
                raise business_exception(ErrorCode.FILE_EXTENSION_NOT_SUPPORTED)
        return text_document

    def __get_file_extension_from_url(self, file_url):
        parsed_url = urlparse(file_url)
        path = parsed_url.path
        filename, file_extension = os.path.splitext(path)
        return file_extension