from fastapi import HTTPException
import httpx
from core.constants.base_config import settings

async def oauth_access_token(code: str):
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
        
        # TODO SEE HOW TO IMPROVE  THIS
        if response.status_code != 200:
            # TODO You might want to inspect response.json() for detailed error info
            raise HTTPException(status_code=response.status_code,
                                detail="Error Logging In")
        
        return response
