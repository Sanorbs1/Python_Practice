# test_api_client.py
import pytest
from api_client import fetch_user

@pytest.fixture(scope="session")
def auth_token():
    # Simulate fetching token once per session
    return "fake_token_123"

def test_fetch_user(auth_token):
    user = fetch_user("123", auth_token)
    assert "name" in user