from flask import Blueprint, request

from apps.auth.schemas.login_schema import LoginRequest, LoginResponse
from apps.auth.services.login_service import login_service
from core.decorator.api_view import api_view

auth_route = Blueprint('auth', __name__)


@auth_route.post('/login')
@api_view
def login():
    response: LoginResponse = login_service(LoginRequest(**request.args))
    return response.model_dump_json()
