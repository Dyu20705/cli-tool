from collections.abc import Mapping
from typing import Any

from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    email: str

def validate_user(data: list[dict[str, Any]]) -> list[User]:
    if not isinstance(data, list):
        raise TypeError("Expected a list of user objects")

    validated_users: list[User] = []

    for item in data:
        if not isinstance(item, Mapping):
            raise TypeError("Each user item must be an object")
        user = User(**item)
        validated_users.append(user)

    return validated_users