from pydantic import BaseModel, Field
from typing import Optional

class PullRequest(BaseModel):
    title: str = Field(..., description="Title of Pull Request")
    head: str = Field(..., description="HEAD of Pull Request")
    base: str = Field(..., description="Base branch to merge")
    body: Optional[str] = Field(None, description='Body of Pull Request')
