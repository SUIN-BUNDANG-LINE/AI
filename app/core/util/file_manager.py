import os
from urllib.parse import urlparse

class FileManager:
    @staticmethod
    def get_file_extension_from_url(file_url: str) -> str:
        parsed_url = urlparse(file_url)
        path = parsed_url.path
        filename, file_extension = os.path.splitext(path)
        return file_extension