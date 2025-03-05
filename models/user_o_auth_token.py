import datetime
from typing import Optional
from pydantic import BaseModel, Field

class UserOAuthToken(BaseModel):
    account_id: str = Field(..., description="Unique account ID")
    access_token: str = Field(..., description="Encrypted access token")
    refresh_token: Optional[str]  = Field(None, description="Encrypted refresh token")
    token_type: str = Field(..., description="Token type, e.g. bearer")
    expires_at: datetime.datetime = Field(..., description="Expiration timestamp") 
