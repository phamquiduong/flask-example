import os

import boto3

from apps.auth.schemas.get_user_schema import GetUserRequest, GetUserResponse
from core.api_exception import UnauthorizedException

AWS_REGION = os.getenv('AWS_REGION')


def get_user_service(request: GetUserRequest):
    access_token = request.access_token

    client = boto3.client('cognito-idp', region_name=AWS_REGION)

    try:
        response = client.get_user(AccessToken=access_token)
    except client.exceptions.NotAuthorizedException as not_auth_exc:
        raise UnauthorizedException(message=str(not_auth_exc), error_code=1) from not_auth_exc

    user_attributes = {user_attr['Name']: user_attr['Value'] for user_attr in response['UserAttributes']}

    return GetUserResponse(**user_attributes)
