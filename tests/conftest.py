import pytest

from constants.base_config import settings

@pytest.fixture
def setup_github_api_url(monkeypatch):
    fake_api_url = "https://fakeapi.com"

    # Set a fake API URL for testing
    monkeypatch.setattr(settings, "GITHUB_API_URL", fake_api_url)

    return fake_api_url
