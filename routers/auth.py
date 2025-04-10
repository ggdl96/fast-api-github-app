import logging
from fastapi import APIRouter, HTTPException
from services.auth import oauth_access_token
from services.user import get_github_user_data

auth_router = APIRouter(tags=["auth"])

logger = logging.getLogger("auth_logger")

@auth_router.post("/github/auth")
async def github_auth(code: str):    
    logger.info("starting with github auth process")
    try:
        response = await oauth_access_token(code)

        if (response.error):
            logger.error("failed oauth process")
            raise (HTTPException(status_code=400, detail=response.model_dump()))

        await get_github_user_data(response.access_token)
        logger.info("returning github user data retrieved")
        return response
    except HTTPException as http_exc:
        logger.error(f"failed auth process with: {http_exc}")
        raise HTTPException(status_code=http_exc.status_code, detail= http_exc.detail)
    except Exception as exc:
        logger.error(f"failed auth process with: {exc}")
        raise HTTPException(status_code=500, detail='Unknown error')
