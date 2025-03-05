import httpx

from models.pull_request import PullRequest
from fastapi import  HTTPException
from constants.base_config import HEADERS, settings

def build_repo_url(owner: str, repo: str) -> str:
    return f"{settings.GITHUB_API_URL}/repos/{owner}/{repo}"

async def get_repo(owner: str, repo: str):
    """
    Fetch details about a GitHub repository.
    """
    async with httpx.AsyncClient() as client:
        response = await client.get(build_repo_url(owner=owner, repo=repo), headers=HEADERS)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code,
                            detail="Error fetching repository information")
    return response.json()

async def create_pull_request(owner: str, repo: str, pr: PullRequest):
    """
    Create a new pull request on a GitHub repository.
    """
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{build_repo_url(owner=owner, repo=repo)}/pulls", headers=HEADERS, json=pr.model_dump())
    if response.status_code != 201:
        # You might want to inspect response.json() for detailed error info
        raise HTTPException(status_code=response.status_code,
                            detail="Error creating pull request")
    return response.json()
