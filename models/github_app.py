import datetime
from pydantic import BaseModel, Field
from typing import List, Literal

from models.account_type import ACCOUNT_TYPE
from models.permissions import Permissions
from models.repository import Repository


class GithubApp(BaseModel):
    installation_id: str = Field(..., description="Provided by GitHub")
    account_id: str = Field(..., description="User or organization ID")
    account_type: ACCOUNT_TYPE = Field(..., description="Account type: User/Organization")
    repositories: List[Repository] = Field(default_factory=list, description="Optional repository information")
    permissions: Permissions = Field(..., description="Permissions granted to the app")
    created_at: datetime.datetime = Field(..., description="Creation timestamp")
    updated_at: datetime.datetime = Field(..., description="Update timestamp") 
