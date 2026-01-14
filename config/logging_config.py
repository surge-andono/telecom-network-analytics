import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

def setup_logger(name: str) -> logging.Logger:
    
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)
    
    """
    Creates and returns a structured logger
    with rotation and consistent formatting.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    handler = RotatingFileHandler(
        "logs/etl.log",
        maxBytes=5_000_000,  # 5 MB
        backupCount=3
    )
    handler.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(handler)

    return logger
