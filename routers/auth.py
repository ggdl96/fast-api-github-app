from fastapi import APIRouter, HTTPException
from services.auth import oauth_access_token
from services.user import get_github_user_data

auth_router = APIRouter()

@auth_router.post("/github/auth")
async def github_auth(code: str):    
    try:
        response = await oauth_access_token(code)

        if (response.error):
            raise (HTTPException(status_code=400, detail=response.model_dump()))

        await get_github_user_data(response.access_token)
        return response
    except HTTPException as http_exc:
        raise HTTPException(status_code=http_exc.status_code, detail= http_exc.detail) from  http_exc
    except Exception as exc:
        raise HTTPException(status_code=500, detail='Unknown error')
