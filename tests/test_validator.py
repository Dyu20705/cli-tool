import pytest

from data_fetch_cli import validate_user
from data_fetch_cli.validator import User


def test_validate_user() -> None:
    data = [
        {"id": 1, "name": "Alice", "email": "alice@example.com"},
        {"id": 2, "name": "Bob", "email": "bob@example.com"},
    ]
    result = validate_user(data)

    assert isinstance(result, list)
    assert len(result) == 2
    assert isinstance(result[0], User)
    assert result[0].id == 1
    assert result[0].name == "Alice"
    assert result[0].email == "alice@example.com"


def test_validate_user_requires_list_input() -> None:
    with pytest.raises(TypeError, match="Expected a list"):
        validate_user({"id": 1, "name": "Alice", "email": "alice@example.com"})  # type: ignore[arg-type]


def test_validate_user_requires_object_items() -> None:
    with pytest.raises(TypeError, match="Each user item must be an object"):
        validate_user(["invalid-item"])  # type: ignore[list-item]