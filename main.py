from fastapi import FastAPI
from routers.repos import repo_router
from routers.auth_appsec import auth_router
from routers.webhook import webhook_router
from routers.product import product_router
from routers.token import token_router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
async def root():
    return {'message': 'Hello, FastAPI GitHub App'}

app.include_router(repo_router)
app.include_router(auth_router)
app.include_router(webhook_router)
app.include_router(product_router, prefix="/api-product")
app.include_router(token_router)
