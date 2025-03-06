from models.github_headers import GitHubHeaders
from core.constants.base_config import settings

def build_repo_url(owner: str, repo: str) -> str:
    """Build url for fetching github repos

    Args:
        owner (str): username
        repo (str): repo description

    Returns:
        str: new url
    """
    return f"{settings.GITHUB_API_URL}/repos/{owner}/{repo}"

def build_token_for_request(github_token: str) -> str:
    """Build Headers for requesting to github api

    Args:
        github_token (str): GITHUB Access Token

    Returns:
        str: Header for authorizing request
    """
    GitHubHeaders(Authorization=f"token {github_token}").model_dump()
