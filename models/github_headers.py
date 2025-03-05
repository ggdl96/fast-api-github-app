from pydantic import BaseModel, Field

class GitHubHeaders(BaseModel):
    Authorization: str = Field(..., description="Auth Bearer")
