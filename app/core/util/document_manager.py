from langchain.document_loaders import PyMuPDFLoader
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
        splitted_documents = text_splitter.split_documents(documents)
        return self.documents_to_text(splitted_documents)