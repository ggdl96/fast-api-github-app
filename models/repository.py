from pydantic import BaseModel, Field

class Repository(BaseModel):
    id: str = Field(..., description="Unique repository identifier")
    name: str = Field(..., description="Repository name")
    url: str = Field(..., description="Repository URL")
