from email.policy import HTTP
import requests
from http import HTTPStatus
from langchain.docstore.document import Document
from langchain_community.document_loaders import PyMuPDFLoader
from app.error.error_code import ErrorCode
from app.error.business_exception import business_exception


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
        if response.status_code != HTTPStatus.OK:
            raise business_exception(ErrorCode.FILE_NOT_FOUND)
        response.encoding = "utf-8"
        text_content = response.text

        documents = [Document(page_content=text_content)]
        return self.documents_to_text(documents)
