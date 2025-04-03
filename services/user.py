import httpx

from fastapi import  HTTPException
from models.github import GitHubUserResponseSucess
from utils.repos import build_bearer_for_request
from core.constants.base_config import settings

async def get_github_user_data(jwt_token: str) -> GitHubUserResponseSucess:
    """Retrieve user info from github

    Args:
        jwt_token (str): the token needed to perform the request

    Raises:
        HTTPException: Error requesting the user's info

    Returns:
        GitHubUserResponse: The user's info
    """
    async with httpx.AsyncClient() as client:
        url = f"{settings.GITHUB_API_URL}/user"

        response = await client.get(url, headers=build_bearer_for_request(jwt_token))

        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code,
                                detail=response.json())
            
        return GitHubUserResponseSucess(**response.json())
