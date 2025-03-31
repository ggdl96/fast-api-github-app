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
    PRODUCT_URL: str
    GITHUB_PRIVATE_KEY: str
    AUD_JWT: str

    def __getattr__(self, item):
        return os.getenv(item)


settings = Settings()
