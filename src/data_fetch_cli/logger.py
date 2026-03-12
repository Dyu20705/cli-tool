import logging
from pythonjsonlogger.json import JsonFormatter

def get_logger():
    logger = logging.getLogger("app")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = JsonFormatter(
            fmt="%(asctime)s %(levelname)s %(message)s %(module)s",
            rename_fields={"asctime": "timestamp", "levelname": "level"},
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger
