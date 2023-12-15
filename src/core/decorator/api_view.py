from pydantic import ValidationError

from core.api_exception import BadRequestException


def api_view(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValidationError as valid_error:
            error_fields = {str(error["loc"][0]): error["msg"] for error in valid_error.errors()}
            return BadRequestException(error_fields=error_fields).dump_response()
    return wrapper
