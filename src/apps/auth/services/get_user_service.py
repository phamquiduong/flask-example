import os

import boto3

from apps.auth.schemas.get_user_schema import GetUserRequest, GetUserResponse

AWS_REGION = os.getenv('AWS_REGION')
USER_POOL_ID = os.getenv('USER_POOL_ID')
CLIENT_ID = os.getenv('CLIENT_ID')


def get_user_service(request: GetUserRequest):
    access_token = request.access_token

    client = boto3.client('cognito-idp', region_name=AWS_REGION)

    response = client.get_user(
        AccessToken=access_token
    )

    user_attributes = {user_attr['Name']: user_attr['Value'] for user_attr in response['UserAttributes']}

    return GetUserResponse(**user_attributes)
