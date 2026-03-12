# data-fetch-cli

CLI nhỏ gọn để tải dữ liệu user từ HTTP endpoint, xác thực schema bằng Pydantic, và chạy như một installable command qua `data-fetch`.

## Features

- Installable CLI qua entry point `data-fetch = data_fetch_cli.cli:app`.
- `fetch` command để tải + validate dữ liệu theo luồng end-to-end.
- `--version` lấy version từ package metadata.
- `--json` để xuất dữ liệu máy có thể parse trong pipeline.
- Structured logging (JSON) với `timestamp`, `level`, `message`, `module`.
- Kiến trúc package chuẩn `src/` và test bằng `pytest` + `CliRunner`.
- Unit test không phụ thuộc internet (mock `requests.get`).

## Project Structure

```text
src/
  data_fetch_cli/
    __init__.py
    __main__.py
    cli.py
    downloader.py
    logger.py
    validator.py
tests/
  conftest.py
  test_downloader.py
  test_validator.py
.github/workflows/ci.yml
```

## Requirements

- Python `3.11+`

## Installation

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
pip install -e .
```

Sau khi cài, bạn có thể chạy CLI bằng script `data-fetch`.

## Packaging

CLI được publish nội bộ dưới dạng package Python chuẩn thông qua [pyproject.toml](pyproject.toml). Entry point hiện tại là:

```toml
[project.scripts]
data-fetch = "data_fetch_cli.cli:app"
```

Khi chạy `pip install -e .`, môi trường sẽ tạo command `data-fetch` và trỏ trực tiếp tới source code hiện tại.

## Usage

### Fetch users from URL

```bash
data-fetch fetch "https://jsonplaceholder.typicode.com/users"
```

### Emit JSON for scripting

```bash
data-fetch fetch "https://jsonplaceholder.typicode.com/users" --json
```

### Show version

```bash
data-fetch --version
```

Hoặc chạy module trực tiếp:

```bash
python -m data_fetch_cli fetch "https://jsonplaceholder.typicode.com/users"
```

## Development

### Run tests

```bash
pytest tests
```

Bao gồm cả function tests và CLI behavior tests bằng `typer.testing.CliRunner`.

### CI

GitHub Actions workflow tại `.github/workflows/ci.yml` chạy:

1. Checkout code
2. Setup Python 3.11
3. Cache pip
4. Install dependencies + editable package
5. Run test suite

## Public API

`data_fetch_cli/__init__.py` export API chính:

- `download_data`
- `validate_user`

Nên bạn có thể import ngắn gọn:

```python
from data_fetch_cli import download_data, validate_user
```
