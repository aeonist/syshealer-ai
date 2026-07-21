"""
Настройка логирования для всего проекта.
Один вызов setup_logging() в main.py — и все модули логируют единообразно.
"""
import logging
import logging.handlers
import os
from pathlib import Path

from src.config import BASE_DIR


def setup_logging(verbose: bool = False) -> None:
    """Вызывается ОДИН раз при старте приложения."""
    log_dir = Path(BASE_DIR) / "data"
    log_dir.mkdir(parents=True, exist_ok=True)

    level = logging.DEBUG if verbose else logging.INFO

    formatter = logging.Formatter(
        "[%(asctime)s] %(levelname)-8s %(name)s: %(message)s",
        datefmt="%H:%M:%S",
    )

    # Все логи пишутся в файл (с ротацией — макс 5 МБ, 3 старых копии)
    file_handler = logging.handlers.RotatingFileHandler(
        log_dir / "syshealer.log",
        maxBytes=5_000_000,
        backupCount=3,
        encoding="utf-8",
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    # Корневой логгер — все остальные наследуют от него
    root = logging.getLogger()
    root.setLevel(level)
    root.addHandler(file_handler)


def get_logger(name: str) -> logging.Logger:
    """Фабрика логгеров. Каждый модуль вызывает: logger = get_logger(__name__)"""
    return logging.getLogger(name)
