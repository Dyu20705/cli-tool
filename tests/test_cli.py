import json
from importlib.metadata import version
from unittest.mock import patch

import requests
from pydantic import ValidationError
from typer.testing import CliRunner

from data_fetch_cli.cli import app
from data_fetch_cli.validator import User

runner = CliRunner()


def test_fetch_json_output() -> None:
    fake_data = [{"id": 1, "name": "Alice", "email": "alice@example.com"}]

    with patch("data_fetch_cli.cli.download_data", return_value=fake_data), patch(
        "data_fetch_cli.cli.validate_user"
    ) as mock_validate:
        mock_validate.return_value = [
            type("UserStub", (), {"model_dump": lambda self: fake_data[0]})()
        ]
        result = runner.invoke(app, ["fetch", "https://example.com/users", "--json"])

    assert result.exit_code == 0
    assert json.loads(result.stdout) == fake_data


def test_fetch_human_output() -> None:
    users = [User(id=1, name="Alice", email="alice@example.com")]

    with patch("data_fetch_cli.cli.download_data", return_value=[{"ignored": True}]), patch(
        "data_fetch_cli.cli.validate_user", return_value=users
    ):
        result = runner.invoke(app, ["fetch", "https://example.com/users"])

    assert result.exit_code == 0
    assert "1: Alice <alice@example.com>" in result.stdout


def test_fetch_request_error_is_reported_cleanly() -> None:
    with patch(
        "data_fetch_cli.cli.download_data",
        side_effect=requests.HTTPError("404 Client Error: Not Found"),
    ):
        result = runner.invoke(app, ["fetch", "https://example.com/missing"])

    assert result.exit_code == 1
    assert "Request failed: 404 Client Error: Not Found" in result.output


def test_fetch_validation_error_is_reported_cleanly() -> None:
    invalid_data = [{"id": 1, "name": "Alice"}]

    with patch("data_fetch_cli.cli.download_data", return_value=invalid_data), patch(
        "data_fetch_cli.cli.validate_user",
        side_effect=ValidationError.from_exception_data(
            "User",
            [
                {
                    "type": "missing",
                    "loc": ("email",),
                    "msg": "Field required",
                    "input": {"id": 1, "name": "Alice"},
                }
            ],
        ),
    ):
        result = runner.invoke(app, ["fetch", "https://example.com/users"])

    assert result.exit_code == 1
    assert "Validation failed:" in result.output
    assert "email" in result.output


def test_version_option_uses_package_metadata() -> None:
    result = runner.invoke(app, ["--version"])

    assert result.exit_code == 0
    assert result.stdout.strip() == version("data-fetch-cli")