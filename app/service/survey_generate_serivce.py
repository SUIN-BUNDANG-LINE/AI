from app.core.util.ai_manager import AIManager
from app.core.util.document_manager import DocumentManager
from app.core.prompt.survey_generate_prompt import *
from app.model.survey import Survey
from langchain.output_parsers import PydanticOutputParser
from app.core.prompt.survey_guide_prompt import survey_guide_prompt

class SurveyGenerateService:
    def __init__(self):
        self.ai_manager =  AIManager()
        self.document_manger = DocumentManager()
        self.summation_prompt = summation_prompt
        self.instruct_prompt = instruct_prompt
    
    def generate_survey(self, job: str, group:str, file_url: str):
        text_documents = self.document_manger.text_from_pdf_file_url(file_url)

        formmatted_summation_prompt = self.summation_prompt.format(document=text_documents)
        summation = self.ai_manager.chat(formmatted_summation_prompt)

        formatted_instruct_prompt = self.instruct_prompt.format(who=job, guide=survey_guide_prompt, group=group, summation=summation)
        parser = PydanticOutputParser(pydantic_object=Survey)

        generated_reuslt = self.ai_manager.chat_with_parser(formatted_instruct_prompt, parser)
        parsed_result = parser.parse(generated_reuslt)
        return parsed_result