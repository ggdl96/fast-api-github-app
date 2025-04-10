from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
import httpx
from core.constants.base_config import settings
from typing import Annotated

import jwt

from crud.user import product_user_by_name
from models.auth import OauthResponseError,OauthResponseSuccess
from models.github import GithubActionJWTDecoded
from models.product import DecodedGithubJWT
from utils.auth import github_jwt_validation

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def verify_action_jwt_token(authorization: Annotated[str, Depends(oauth2_scheme)]) -> DecodedGithubJWT:
    """Verifies the JWT generated from github action to restrict access

    Args:
        authorization (Annotated[str, Depends): The Content of Authorization

    Raises:
        HTTPException: Invalid JWT
        HTTPException: Bad Request

    Returns:
        dict: The decoded JWT
    """
    try:
        token = authorization.replace('Bearer ', '')
        detail="Invalid authentication token"
        decoded_token = jwt.decode(token, algorithms=["RS256"], options={"verify_signature": False})
        parsed_token = GithubActionJWTDecoded(**decoded_token)
        user = product_user_by_name(parsed_token.actor)

        if (github_jwt_validation(decoded_token=parsed_token) and parsed_token.actor_id == user.provider_user_id):
            print('data ok')
        else:
            raise HTTPException(status_code=401, detail=detail)

        return DecodedGithubJWT(decoded=parsed_token)
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

async def oauth_access_token(code: str) -> OauthResponseSuccess:
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

        json = response.json()

        if (json.get("error")):
            raise HTTPException(status_code=400, detail=OauthResponseError(
               **json
            ).model_dump())
    
        return OauthResponseSuccess(**json)
