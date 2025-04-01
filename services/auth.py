from fastapi import HTTPException, Header
import httpx
from core.constants.base_config import settings
from typing import Annotated, Any, Optional

import time

import jwt

from crud.user import product_user_by_name
from models.auth import OauthResponseError
from utils.repos import build_bearer_for_request


def verify_action_jwt_token(authorization: Annotated[Optional[str], Header()]) -> dict:
    """Verifies the JWT generated from github action to restrict access

    Args:
        authorization (Annotated[Optional[str], Header): The Content of Authorization

    Raises:
        HTTPException: Raise exception if not valid JWT

    Returns:
        dict: The decoded JWT
    """
    try:
        token = authorization.replace('Bearer ', '')
        detail="Invalid authentication token"
        decoded_token = jwt.decode(token,algorithms=["RS256"], options={"verify_signature": False})
        user = product_user_by_name(decoded_token['actor'])

        if (decoded_token['aud'] == settings.AUD_JWT and decoded_token['iss'] == settings.GTHUB_ISS_JWT and user.provider_user_id == decoded_token['actor_id']):
            print('data ok')
            # must search then in PRODUCT IF EXISTS
            # IF EXISTS THEN START DOING STUFF
        else:
            raise HTTPException(status_code=401, detail=detail)

        return decoded_token
    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=401,
            detail=detail
        )
    except Exception:
        raise HTTPException(
            status_code=400,
            detail="Bad request"
        )

async def oauth_access_token(code: str) -> Any:
    """Get Access tokens after login with github credentials

    Args:
        code (str): Code parameter that is given after successfuly loging in with github credentials

    Raises:
        HTTPException: _description_

    Returns:
        _type_: Response obtained after successfuly requesting oauth access token
    """
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "https://github.com/login/oauth/access_token",
            headers={"Accept": "application/json"},
            json={
                "client_id": settings.GITHUB_CLIENT_ID,
                "client_secret": settings.GITHUB_CLIENT_SECRET,
                "code": code
            }
        )

        json = response.json()

        return OauthResponseError(
            error=json["error"],
            error_description=json["error_description"],
            error_uri=json["error_uri"]
        )

async def generate_jwt():
    return gen_jwt()

def gen_jwt():
    with open(settings.GITHUB_PRIVATE_KEY, 'rb') as pem_file:
        signing_key = pem_file.read()

        payload = {
            # Issued at time
            'iat': int(time.time()),
            # JWT expiration time (10 minutes maximum)
            'exp': int(time.time()) + 500,
            # GitHub App's client ID
            'iss': settings.APP_ID,
        }

        encoded_jwt = jwt.encode(payload, signing_key, algorithm='RS256')
        
        return encoded_jwt

async def get_github_data(bearer_token: str):
    """Retrieve github user data

    Args:
        bearer_token (str): the token that authorizes the request

    Raises:
        HTTPException: The exception coming from requesting the user data

    Returns:
        Any: response json of user request 
    """
    async with httpx.AsyncClient() as client:
        url = f"{settings.GITHUB_API_URL}/user"
        response = await client.get(url, headers=build_bearer_for_request(bearer_token))
        
        if response.status_code != 201:
            # TODO You might want to inspect response.json() for detailed error info
            raise HTTPException(status_code=response.status_code,
                                detail="")
        return response.json()
