from data_fetch_cli import validate_user
from data_fetch_cli.validator import User

def test_validate_user():
    data = [
        {"id": 1, "name": "Alice", "email": "alice@example.com"},
        {"id": 2, "name": "Bob", "email": "bob@example.com"}
    ]
    result = validate_user(data)

    assert isinstance(result, list)
    assert len(result) == 2
    assert isinstance(result[0], User)
    assert result[0].id == 1
    assert result[0].name == "Alice"
    assert result[0].email == "alice@example.com"