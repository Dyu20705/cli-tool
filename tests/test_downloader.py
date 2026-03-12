from unittest.mock import Mock, patch

from data_fetch_cli import download_data

def test_download_data():
    url = "https://jsonplaceholder.typicode.com/users"
    fake_data = [{"id": 1, "name": "Alice", "email": "alice@example.com"}]

    mock_response = Mock()
    mock_response.json.return_value = fake_data
    mock_response.raise_for_status.return_value = None

    with patch("data_fetch_cli.downloader.requests.get", return_value=mock_response) as mock_get:
        data = download_data(url)

    mock_get.assert_called_once_with(url)
    mock_response.raise_for_status.assert_called_once()
    assert data == fake_data