import httpx

from models.pull_request import PullRequest
from fastapi import  HTTPException
from crud.user import user_by_owner
from utils.repos import build_repo_url, build_token_for_request

async def get_repo(owner: str, repo: str):
    """Fetch details about a GitHub repository.

    Args:
        owner (str): username
        repo (str): repository name

    Raises:
        HTTPException: User not found
        HTTPException: Error fetching repository information

    Returns:
        _type_: _description_
    """
    async with httpx.AsyncClient() as client:
        user = user_by_owner(owner)
        if not user:
            raise HTTPException(status_code=400, detail=f"User '{owner}' not found")
            
        response = await client.get(build_repo_url(owner=owner, repo=repo), headers=build_token_for_request(user["name"]))
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code,
                            detail="Error fetching repository information")
    return response.json()

async def create_pull_request(owner: str, repo: str, pr: PullRequest):
    """Create a new pull request on a GitHub repository.

    Args:
        owner (str): username
        repo (str): repository name
        pr (PullRequest): the body of the pull request

    Raises:
        HTTPException: User not found
        HTTPException: Error creating PR

    Returns:
        _type_: _description_
    """
    async with httpx.AsyncClient() as client:
        user = user_by_owner(owner)
        if not user:
            raise HTTPException(status_code=400, detail=f"User '{owner}' not found")
            
        response = await client.post(f"{build_repo_url(owner=owner, repo=repo)}/pulls", headers=build_token_for_request(user["name"]), json=pr.model_dump())
    if response.status_code != 201:
        # You might want to inspect response.json() for detailed error info
        raise HTTPException(status_code=response.status_code,
                            detail="Error creating pull request")
    return response.json()
