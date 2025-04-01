from pydantic import BaseModel, Field
from typing import Optional

class User(BaseModel):
    #id: str = Field(..., description="Unique ID")
    name: str = Field(..., description="User/Organization name")
    user_name: str = Field(..., description="UserName")
    token: str = Field(..., description="Access token")

class ProductUserLogin(BaseModel):
    username: str = Field(..., description="User/Organization name")
    password: Optional[str] = Field(None, description="Password")
    provider_user_id: Optional[str] = Field(None, description="GitHub provider user ID")
    provider: Optional[str] = Field(None, description="Provider (e.g., 'github')")
