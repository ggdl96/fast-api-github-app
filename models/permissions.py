from pydantic import BaseModel, Field

class Permissions(BaseModel):
    contents: str = Field(..., description="Permission for contents, e.g. read/write")
    issues: str = Field(..., description="Permission for issues, e.g. read/write")
