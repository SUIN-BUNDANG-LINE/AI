import requests
from http import HTTPStatus
from langchain.docstore.document import Document
from langchain_community.document_loaders import PyMuPDFLoader
from app.core.error.error_code import ErrorCode
from app.core.error.business_exception import business_exception


class DocumentManager:
    def __init__(self):
        self.pdf_loader = PyMuPDFLoader

    def text_from_pdf_file_url(self, file_url: str):
        documents = self.pdf_loader(f"{file_url}").load()
        return DocumentManager.__documents_to_text(documents)

    @staticmethod
    def text_from_txt_file_url(file_url: str):
        response = requests.get(file_url)
        if response.status_code != HTTPStatus.OK:
            raise business_exception(ErrorCode.FILE_NOT_FOUND)
        response.encoding = "utf-8"
        text_content = response.text

        documents = [Document(page_content=text_content)]
        return DocumentManager.__documents_to_text(documents)

    def __documents_to_text(documents: list[Document]):
        documents_text = ""
        for document in documents:
            documents_text += f"""
            ----------------------------
            {document.page_content}
            """

        return documents_text
