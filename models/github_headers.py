from typing import Optional
from pydantic import BaseModel, Field

class GitHubHeaders(BaseModel):
    Authorization: str = Field(..., description="Auth Bearer")
    Accept: Optional[str] = Field(default=None, description="Accept Encoding")
