import requests
from langchain.docstore.document import Document
from langchain_community.document_loaders import PyMuPDFLoader
from app.core.config.text_spliiter import text_splitter

class DocumentManager:
    def __init__(self):
        self.pdf_loader = PyMuPDFLoader

    def documents_to_text(self, documents):
        documents_text = ""
        for document in documents:
            documents_text += f"""
        ----------------------------
        {document.page_content}
        """
        return documents_text
    
    def text_from_pdf_file_url(self, file_url: str):
        documents = self.pdf_loader(f"{file_url}").load()
        return self.documents_to_text(documents)
    
    def text_from_txt_file_url(self, file_url: str):
        response = requests.get(file_url)
        response.encoding = 'utf-8'
        text_content = response.text

        documents = [Document(page_content=text_content)]
        return self.documents_to_text(documents)