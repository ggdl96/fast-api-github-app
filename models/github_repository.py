from pydantic import BaseModel, Field
from typing import List

class GithubRepository(BaseModel):
    repo_id: str = Field(..., description="Unique repository ID")
    name: str = Field(..., description="Repository name")
    owner: str = Field(..., description="Owner name")
    private: bool = Field(..., description="Indicates if the repository is private")
    tracked_branches: List[str] = Field(..., description="List of tracked branches, e.g. ['main', 'develop']")
    last_synced: str = Field(..., description="Timestamp of last synchronization")
