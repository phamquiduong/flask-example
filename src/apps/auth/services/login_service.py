import os

import boto3

from apps.auth.schemas.login_schema import LoginRequest, LoginResponse

AWS_REGION = os.getenv('AWS_REGION')
USER_POOL_ID = os.getenv('USER_POOL_ID')
CLIENT_ID = os.getenv('CLIENT_ID')


def login_service(request: LoginRequest):
    username = request.email
    password = request.password

    client = boto3.client('cognito-idp', region_name=AWS_REGION)

    response = client.admin_initiate_auth(
        UserPoolId=USER_POOL_ID,
        ClientId=CLIENT_ID,
        AuthFlow='ADMIN_NO_SRP_AUTH',
        AuthParameters={
            'USERNAME': username,
            'PASSWORD': password
        }
    )

    access_token = response['AuthenticationResult']['AccessToken']

    return LoginResponse(access_token=access_token)
