from pydantic import ValidationError

from core.api_exception import BadRequestException


def request_validation(api_code: int = 0, error_code: int = 1):
    def inner(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except ValidationError as valid_error:
                error_fields = {str(error["loc"][0]): error["msg"] for error in valid_error.errors()}
                return BadRequestException(api_code=api_code,
                                           error_code=error_code,
                                           error_fields=error_fields,
                                           message='Invalid request data').dump_response()
        wrapper.__name__ = func.__name__
        return wrapper
    return inner
