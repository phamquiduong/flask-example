from http import HTTPStatus

from flask import jsonify
from pydantic import BaseModel


def response_jsonify(status_code: HTTPStatus | int = HTTPStatus.OK):
    def inner(func):
        def wrapper(*args, **kwargs):
            response = func(*args, **kwargs)
            if isinstance(response, BaseModel):
                return jsonify(response.model_dump()), status_code
            return jsonify(response), status_code
        return wrapper
    return inner
