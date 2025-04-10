import logging
from models.pull_request import PullRequest
from fastapi import APIRouter
from services.repos import get_repo, create_pull_request


repo_router = APIRouter()

logger = logging.getLogger("repos_logger")

@repo_router.get("/repo/{owner}/{repo}")
async def get_repo_by_owner(owner: str, repo: str):
    logger.info('Get Repo')
    return await get_repo(owner=owner, repo=repo)

@repo_router.post("/repo/{owner}/{repo}/pulls")
async def create_pull_request_by_owner(owner: str, repo: str, pr: PullRequest):
    logger.info('Create Pull Request')
    return await create_pull_request(owner=owner, repo=repo, pr=pr)
