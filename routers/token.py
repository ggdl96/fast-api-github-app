from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated
from fastapi.security import OAuth2PasswordRequestForm
from crud.user import product_user_by_name
from models.auth import JWT_Token
from core.constants.base_config import settings
from utils.auth import create_access_token


token_router = APIRouter(tags=["token"])

@token_router.post("/token")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> JWT_Token:
    if (form_data.username != settings.ADMIN_USER and form_data.password !=  settings.ADMIN_PASSWORD):
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
        
    user = product_user_by_name(form_data.username)
    access_token = create_access_token(data={"actor": settings.ADMIN_USER, "actor_id": user.provider_user_id})
    return JWT_Token(access_token=access_token, token_type="bearer")
