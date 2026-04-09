from collections.abc import Mapping
from typing import Any

import requests


def download_data(url: str) -> list[dict[str, Any]]:
    """Download and return a JSON array of objects from the provided URL."""
    response = requests.get(url, timeout=15)
    response.raise_for_status()

    payload = response.json()
    if not isinstance(payload, list):
        raise ValueError("Expected JSON array from endpoint")

    if not all(isinstance(item, Mapping) for item in payload):
        raise ValueError("Expected each JSON item to be an object")

    return [dict(item) for item in payload]