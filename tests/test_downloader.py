from unittest.mock import Mock, patch

import pytest

from data_fetch_cli import download_data


def test_download_data() -> None:
    url = "https://jsonplaceholder.typicode.com/users"
    fake_data = [{"id": 1, "name": "Alice", "email": "alice@example.com"}]

    mock_response = Mock()
    mock_response.json.return_value = fake_data
    mock_response.raise_for_status.return_value = None

    with patch("data_fetch_cli.downloader.requests.get", return_value=mock_response) as mock_get:
        data = download_data(url)

    mock_get.assert_called_once_with(url, timeout=15)
    mock_response.raise_for_status.assert_called_once()
    assert data == fake_data


def test_download_data_rejects_non_list_json() -> None:
    mock_response = Mock()
    mock_response.raise_for_status.return_value = None
    mock_response.json.return_value = {"id": 1}

    with patch("data_fetch_cli.downloader.requests.get", return_value=mock_response):
        with pytest.raises(ValueError, match="Expected JSON array"):
            download_data("https://example.com/users")


def test_download_data_rejects_non_object_items() -> None:
    mock_response = Mock()
    mock_response.raise_for_status.return_value = None
    mock_response.json.return_value = [1, 2, 3]

    with patch("data_fetch_cli.downloader.requests.get", return_value=mock_response):
        with pytest.raises(ValueError, match="Expected each JSON item"):
            download_data("https://example.com/users")