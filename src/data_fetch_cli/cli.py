import json
from importlib.metadata import PackageNotFoundError, version

import requests
import typer
from pydantic import ValidationError

from data_fetch_cli.downloader import download_data
from data_fetch_cli.logger import get_logger
from data_fetch_cli.validator import validate_user

app = typer.Typer()
logger = get_logger()


def get_package_version() -> str:
    try:
        return version("data-fetch-cli")
    except PackageNotFoundError:
        return "unknown"


def version_callback(value: bool) -> None:
    if not value:
        return
    typer.echo(get_package_version())
    raise typer.Exit()


def exit_with_error(message: str) -> None:
    typer.secho(message, fg=typer.colors.RED, err=True)
    raise typer.Exit(code=1)

@app.callback()
def main(
    version_option: bool = typer.Option(
        False,
        "--version",
        help="Show the installed CLI version and exit.",
        callback=version_callback,
        is_eager=True,
    ),
) -> None:
    """Data fetch CLI."""
    return None

@app.command()
def fetch(
    url: str = typer.Argument(..., help="URL để lấy dữ liệu"),
    json_output: bool = typer.Option(
        False,
        "--json",
        help="Emit validated records as JSON for scripting and pipelines.",
    ),
) -> None:
    logger.info("download_started", extra={"url": url})

    try:
        data = download_data(url)
    except requests.RequestException as exc:
        logger.error("download_failed", extra={"url": url, "error": str(exc)})
        exit_with_error(f"Request failed: {exc}")

    logger.info("download_completed", extra={"record_count": len(data)})

    try:
        users = validate_user(data)
    except (ValidationError, TypeError, ValueError) as exc:
        logger.error("validation_failed", extra={"url": url, "error": str(exc)})
        exit_with_error(f"Validation failed: {exc}")

    logger.info("validation_completed", extra={"valid_user_count": len(users)})

    if json_output:
        typer.echo(json.dumps([user.model_dump() for user in users], ensure_ascii=False))
        return

    for user in users:
        typer.echo(f"{user.id}: {user.name} <{user.email}>")

if __name__ == "__main__":
    app()


