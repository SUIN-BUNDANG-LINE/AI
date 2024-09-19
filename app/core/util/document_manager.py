import requests
from langchain.docstore.document import Document
from langchain_community.document_loaders import PyMuPDFLoader

class DocumentManager:
    def __init__(self):
        self.pdf_loader = PyMuPDFLoader
    
    def documents_to_text(self, documents):
        DOCUMENTS_TEXT_LIMIT = 10000

        documents_text = ""
        for document in documents:
            if(len(documents_text) > DOCUMENTS_TEXT_LIMIT):
                raise Exception("Document text is too long")
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