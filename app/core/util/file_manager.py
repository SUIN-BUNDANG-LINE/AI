import os


class FileManager:
    @staticmethod
    def get_file_extension_from_url(file_url: str) -> str:
        path = file_url.split('/')[-1]
        filename, file_extension = os.path.splitext(path)
        return file_extension
