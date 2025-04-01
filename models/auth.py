from pydantic import BaseModel, Field

class OauthResponseError(BaseModel):
    error: str = Field(..., description="The error code returned from GitHub OAuth", example="bad_verification_code")
    error_description: str | None = Field(None, description="A human readable description of the error", example="The code passed is incorrect or expired.")
    error_uri: str | None = Field(None, description="A URL with more information about the error", example="https://docs.github.com/apps/managing-oauth-apps/troubleshooting-oauth-app-access-token-request-errors/#bad-verification-code")
