from enum import Enum
from http import HTTPStatus


class ErrorCode(Enum):
    def __new__(cls, status_code, detail):
        obj = object.__new__(cls)
        obj._value_ = detail
        obj.status_code = status_code
        obj.detail = detail
        return obj
    
    TEXT_TOO_LONG = (HTTPStatus.BAD_REQUEST, "파일 길이가 너무 깁니다.")
