from fastapi import APIRouter, HTTPException
import httpx
from core.constants.base_config import settings
from services.auth import oauth_access_token

auth_router = APIRouter()

@auth_router.get("/github/callback")
async def github_callback(code):
    print('code: ', code)
    response = await oauth_access_token(code)
    
    print('response after access tok', response)
    
    return response.text
