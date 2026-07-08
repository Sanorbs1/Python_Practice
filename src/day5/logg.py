# api_client.py
import logging
import requests

logger = logging.getLogger(__name__)

def fetch_user(user_id, token):
    url = f"https://api.example.com/users/{user_id}"
    headers = {"Authorization": f"Bearer {token}"}
    try:
        resp = requests.get(url, headers=headers, timeout=5)
        resp.raise_for_status()
        logger.info("Fetched user %s", user_id)
        return resp.json()
    except requests.RequestException as e:
        logger.error("Failed to fetch user %s: %s", user_id, e)
        raise