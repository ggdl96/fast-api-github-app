from typing import Optional, Dict, Any, List
from pydantic import BaseModel, Field
from datetime import datetime

class UserModel(BaseModel):
    login: str = Field(..., description="The username of the GitHub user.")
    id: int = Field(..., description="The unique identifier of the user.")

class RepoModel(BaseModel):
    id: int = Field(..., description="The repository's unique identifier.")
    name: str = Field(..., description="The name of the repository.")
    full_name: str = Field(..., description="The full name of the repository including the owner's login.")

class PullRequestModel(BaseModel):
    id: int = Field(..., description="The unique identifier of the pull request.")
    number: int = Field(..., description="The pull request number within the repository.")
    state: str = Field(..., description="The current state of the pull request (e.g., open, closed).")
    title: str = Field(..., description="The title of the pull request.")
    body: Optional[str] = Field(default=None, description="The description or body of the pull request (optional).")
    user: UserModel = Field(..., description="The user who created the pull request.")
    
class Step(BaseModel):
    name: str = Field(..., description="The name of the step.")
    status: str = Field(..., description="The current status of the step (e.g., completed).")
    conclusion: Optional[str] = Field(None, description="The final conclusion of the step (e.g., success, failure).")
    number: int = Field(..., description="The sequence number of the step.")
    started_at: Optional[datetime] = Field(None, description="Timestamp when the step started.")
    completed_at: Optional[datetime] = Field(None, description="Timestamp when the step completed.")

class WorkflowJob(BaseModel):
    id: int = Field(..., description="The unique identifier for the workflow job.")
    run_id: int = Field(..., description="The identifier of the run that this job belongs to.")
    workflow_name: str = Field(..., description="The name of the workflow.")
    head_branch: str = Field(..., description="The branch from which the workflow was triggered.")
    run_url: str = Field(..., description="URL to access details about the run.")
    run_attempt: int = Field(..., description="The attempt number of the run.")
    node_id: str = Field(..., description="The node identifier for the workflow job.")
    head_sha: str = Field(..., description="The SHA of the head commit.")
    url: str = Field(..., description="The API URL for the workflow job.")
    html_url: str = Field(..., description="The HTML URL for the workflow job on GitHub.")
    status: str = Field(..., description="The current status of the workflow job (e.g., completed).")
    conclusion: Optional[str] = Field(None, description="The final conclusion of the workflow job (e.g., success, failure).")
    created_at: datetime = Field(..., description="Timestamp for when the job was created.")
    started_at: Optional[datetime] = Field(None, description="Timestamp for when the job started.")
    completed_at: Optional[datetime] = Field(None, description="Timestamp for when the job completed.")
    name: str = Field(..., description="The name of the workflow job.")
    steps: List[Step] = Field(..., description="List of steps executed in this job.")
    check_run_url: str = Field(..., description="The URL to the check run associated with this job.")
    labels: List[str] = Field(..., description="Labels assigned to the workflow job.")
    runner_id: int = Field(..., description="The ID of the runner executing the job.")
    runner_name: str = Field(..., description="The name of the runner executing the job.")
    runner_group_id: int = Field(..., description="The group ID of the runner.")
    runner_group_name: str = Field(..., description="The group name of the runner.")

class PullRequestWebhook(BaseModel):
    action: str = Field(..., description="The action that triggered the webhook event (e.g., opened, closed).")
    pull_request: Optional[PullRequestModel] = Field(default=None, description="The pull request data associated with the webhook event.")
    repository: Optional[RepoModel] = Field(default=None, description="The repository related to the pull request event.")
    sender: Optional[UserModel] = Field(default=None, description="The user who initiated the webhook event.")
    # inputs: Optional[Any] = Field(default=None, description="Inputs.")
    # workflow: Optional[str] = Field(default=None, description="Workflow.")
    workflow_job: Optional[WorkflowJob] = Field(default=None, description="the Workflow Job data that is running/completed.")
    # workflow_run: Optional[Any] = Field(default=None, description="Workflow.")