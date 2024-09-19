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


class SurveyGenerateService:
    def __init__(self):
        self.ai_manager =  AIManager()
        self.document_manger = DocumentManager()
        self.summation_prompt = summation_prompt
        self.instruct_prompt = instruct_prompt

    def get_file_extension_from_url(self, file_url):
        parsed_url = urlparse(file_url)
        path = parsed_url.path
        filename, file_extension = os.path.splitext(path)
        return file_extension

    def generate_survey(self, job: str, group:str, file_url: str):
        extension = self.get_file_extension_from_url(file_url)

        text_document = ""
        match extension:
            case ".pdf":
                text_document = self.document_manger.text_from_pdf_file_url(file_url)
            case ".txt":
                text_document = self.document_manger.text_from_txt_file_url(file_url)
            case _:
                raise business_exception(ErrorCode.FILE_EXTENSION_NOT_SUPPORTED)

        formmatted_summation_prompt = self.summation_prompt.format(document=text_document)
        summation = self.ai_manager.chat(formmatted_summation_prompt)
        formatted_instruct_prompt = self.instruct_prompt.format(who=job, guide=survey_guide_prompt, group=group, summation=summation)

        parser = PydanticOutputParser(pydantic_object=SurveyGenerateResponse)
        generated_reuslt = self.ai_manager.chat_with_parser(formatted_instruct_prompt, parser)
        parsed_result = parser.parse(generated_reuslt)
        return parsed_result