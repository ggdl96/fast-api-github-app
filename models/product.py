from enum import Enum
from typing import List, Optional
from pydantic import BaseModel, Field

from models.github import GithubActionJWTDecoded

class SubmitPayload(BaseModel):
    owner: str = Field(..., description="The owner of the repository", example="octocat")
    message: str = Field(..., description="The message to process", example="Hi there!")

class StepStatus(str, Enum):
    completed = "completed"
    failed = "failed"

class Step(BaseModel):
    name: str = Field(..., description="The name of the step", example="processing message")
    status: StepStatus = Field(..., description="The status of the step", example="completed")


class SubmitResponse(BaseModel):
    message: str = Field(..., description="A response message indicating the outcome", example="Submission successful")
    description: Optional[str] = Field(None, description="Optional detailed description", example="The message was processed successfully")
    steps: List[Step] = Field(..., description="List of steps detailing the submission process")

class DecodedGithubJWT(BaseModel):
    decoded: GithubActionJWTDecoded

