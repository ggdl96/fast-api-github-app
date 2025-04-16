import os
from dotenv import load_dotenv

from models.github_headers import GitHubHeaders
from pydantic_settings import BaseSettings, SettingsConfigDict
load_dotenv()

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', extra='allow')

    GITHUB_API_URL: str
    GITHUB_TOKEN: str
    GITHUB_CLIENT_ID: str
    GITHUB_CLIENT_SECRET: str 
    APP_ID: str
    GITHUB_PRIVATE_KEY: str
    AUD_JWT: str
    GTHUB_ISS_JWT: str
    GITHUB_URL: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    ADMIN_USER: str
    ADMIN_PASSWORD: str
    VERSION: str
    GITHUB_WEBHOOK_SECRET: str

    def __getattr__(self, item):
        return os.getenv(item)


settings = Settings()
