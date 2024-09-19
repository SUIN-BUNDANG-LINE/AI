from fastapi import HTTPException

from app.error.error_code import ErrorCode

def business_exception(error_code:ErrorCode):
    return HTTPException(status_code=error_code.status_code, detail=error_code.detail)