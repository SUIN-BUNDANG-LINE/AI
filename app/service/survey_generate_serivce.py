import os
from urllib.parse import urlparse
from app.core.util.ai_manager import AIManager
from app.core.util.document_manager import DocumentManager
from app.core.prompt.survey_generation_prompt import survey_generation_prompt
from app.core.prompt.question_suggestion_prompt import question_suggestion_prompt
from app.dto.model import question
from app.dto.response.survey_generate_response import * 
from langchain.output_parsers import PydanticOutputParser
from app.core.prompt.survey_guide_prompt import survey_guide_prompt
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

        formmatted_question_suggestion_prompt = self.question_suggestion_prompt.format(document=text_document)
        suggested_question = self.ai_manager.chat(formmatted_question_suggestion_prompt)

        print(suggested_question)

        formatted_survey_generation_prompt = self.survey_generation_prompt.format(job=job, user_prompt=user_prompt, guide=survey_guide_prompt, group=group, suggested_question=suggested_question)

        parser = PydanticOutputParser(pydantic_object=SurveyGenerateResponse)
        generated_reuslt = self.ai_manager.chat_with_parser(formatted_survey_generation_prompt, parser)
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