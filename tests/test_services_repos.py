import pytest
from services.repos import build_repo_url


def test_build_repo_url(setup_github_api_url):
    owner = "test_owner"
    repo = "test_repo"
    expected = f"{setup_github_api_url}/repos/{owner}/{repo}"

    actual = build_repo_url(owner, repo)
    assert actual == expected


if __name__ == '__main__':
    pytest.main()
