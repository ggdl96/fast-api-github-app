from pydantic import BaseModel, Field
from typing import Union

class OauthResponseError(BaseModel):
    error: str = Field(..., description="The error code returned from GitHub OAuth", example="bad_verification_code")
    error_description: str | None = Field(None, description="A human readable description of the error", example="The code passed is incorrect or expired.")
    error_uri: str | None = Field(None, description="A URL with more information about the error", example="https://docs.github.com/apps/managing-oauth-apps/troubleshooting-oauth-app-access-token-request-errors/#bad-verification-code")

class OauthResponseSuccess(BaseModel):
    access_token: str = Field(..., description="Access token provided by GitHub OAuth")
    expires_in: int | None = Field(None, description="Number of seconds before the access token expires", example=28800)
    refresh_token: str | None = Field(None, description="Refresh token provided by GitHub OAuth")
    refresh_token_expires_in: int | None = Field(None, description="Number of seconds before the refresh token expires", example=15811200)
    token_type: str = Field(..., description="The type of token, typically 'bearer'", example="bearer")
    scope: str = Field(..., description="The access scope of the token", example="")

OauthResponse = Union[OauthResponseError, OauthResponseSuccess]

class CommonHeaders(BaseModel):
    authorization: str

class JWT_Token(BaseModel):
    access_token: str
    token_type: str
