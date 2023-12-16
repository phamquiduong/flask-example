from flask import Blueprint, request

from apps.auth.schemas.login_schema import LoginRequest
from apps.auth.services.login_service import login_service
from core.decorator import request_validation, response_jsonify
from core.utils.parse_request import parse_request

auth_route = Blueprint('auth', __name__)


@auth_route.post('/login')  # type: ignore
@response_jsonify()
@request_validation(api_code=1)
def login():
    request_data = LoginRequest(**parse_request(request))
    return login_service(request_data)
