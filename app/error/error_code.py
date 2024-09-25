from enum import Enum
from http import HTTPStatus


class ErrorCode(Enum):
    def __new__(cls, status_code, detail):
        obj = object.__new__(cls)
        obj._value_ = detail
        obj.status_code = status_code
        obj.detail = detail
        return obj
    
    TEXT_TOO_LONG = (HTTPStatus.BAD_REQUEST, {"code":"PY0002", "message":"텍스트의 길이가 너무 깁니다"})
    FILE_EXTENSION_NOT_SUPPORTED = (HTTPStatus.BAD_REQUEST, {"code":"PY0003", "message":"지원하지 않는 파일 확장자입니다"})
