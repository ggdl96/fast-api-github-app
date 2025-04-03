from fastapi import Depends, HTTPException, Header
from fastapi.security import OAuth2PasswordBearer
import httpx
from core.constants.base_config import settings
from typing import Annotated

import jwt

from crud.user import product_user_by_name
from models.auth import OauthResponse, OauthResponseError,OauthResponseSuccess
from utils.repos import build_bearer_for_request

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def verify_action_jwt_token(authorization: Annotated[str, Depends(oauth2_scheme)]) -> dict:
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
        print('decoded_token: ', decoded_token)
        if (decoded_token['aud'] == settings.AUD_JWT and decoded_token['iss'] == settings.GTHUB_ISS_JWT and user.provider_user_id == decoded_token['actor_id']):
            print('data ok')
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

async def oauth_access_token(code: str) -> OauthResponse:
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
            f"{settings.GITHUB_URL}/login/oauth/access_token",
            headers={"Accept": "application/json"},
            json={
                "client_id": settings.GITHUB_CLIENT_ID,
                "client_secret": settings.GITHUB_CLIENT_SECRET,
                "code": code
            }
        )
        
        print("response.json()", response.json())

        json = response.json()

        if (json["error"]):
            return OauthResponseError(
               **json
            )
    
        return OauthResponseSuccess(**json)

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
