from fastapi import FastAPI
from routers.repos import router

app = FastAPI()

@app.get('/')
async def root():
    return {'message': 'Hello, FastAPI GitHub App'}

app.include_router(router)
