from apps.auth.schemas.login_schema import LoginRequest, LoginResponse


def login_service(request: LoginRequest):
    return LoginResponse(
        access_token='12',
        refresh_token='23'
    )
