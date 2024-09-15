from app.core.util.ai_manager import AIManager
from app.core.util.document_manager import DocumentManager
from app.core.prompt.survey_generate_prompt import *

class GenerateService:
    def __init__(self):
        self.ai_manager =  AIManager()
        self.document_manger = DocumentManager()
        self.reference_prompt = reference_prompt
        self.instruct_prompt = instruct_prompt
    
    def generate_survey(self, who: str, group:str, file_url: str):
        text_documents = self.document_manger.text_from_pdf_file_url(file_url)
        reference = self.ai_manager.chat(self.reference_prompt.format(document=text_documents))
        generated_reuslt = self.ai_manager.chat(self.instruct_prompt.format(who=who, group=group, reference=reference))

        return generated_reuslt