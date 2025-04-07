from fastapi import FastAPI
from core.constants.base_config import settings
from routers.repos import repo_router
from routers.auth import auth_router
from routers.webhook import webhook_router
from routers.product import product_router
from routers.token import token_router
from fastapi.middleware.cors import CORSMiddleware

import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()]
)

logger = logging.getLogger("main_logger")

logger.info('Starting service')

app = FastAPI(
    title="Github App",
    description="Github App to provide services to users",
    version=settings.VERSION,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
async def root():
    return {
        'message': 'Hello, FastAPI GitHub App',
        "version": settings.VERSION,
        "docs_url": "/docs"
    }

app.include_router(repo_router)
app.include_router(auth_router)
app.include_router(webhook_router)
app.include_router(product_router, prefix="/api-product")
app.include_router(token_router)
