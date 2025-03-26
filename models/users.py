from pydantic import BaseModel, Field
from typing import List

class User(BaseModel):
    #id: str = Field(..., description="Unique ID")
    name: str = Field(..., description="User/Organization name")
    user_name: str = Field(..., description="UserName")
    token: str = Field(..., description="Access token")

class ProductUserLogin(BaseModel):
    username: str = Field(..., description="User/Organization name")
    password: str = Field(..., description="Password")
