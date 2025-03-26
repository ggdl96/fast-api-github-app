from fastapi import FastAPI
from routers.repos import repo_router
from routers.auth import auth_router
from routers.webhook import webhook_router
from routers.product import product_router

app = FastAPI()

@app.get('/')
async def root():
    return {'message': 'Hello, FastAPI GitHub App'}

app.include_router(repo_router)
app.include_router(auth_router)
app.include_router(webhook_router)
app.include_router(product_router, prefix="/api-product")
