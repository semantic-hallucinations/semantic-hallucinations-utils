import logging
import os

from typing import Optional


class LoggerFactory:
    _instance = None
    _loggers = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(LoggerFactory, cls).__new__(cls)
        return cls._instance

    @classmethod
    def get_logger(
        cls,
        name: Optional[str] = None,
        level: int = logging.INFO,
        log_file: Optional[str] = None,
        fmt: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    ) -> logging.Logger:
        if name in cls._loggers:
            return cls._loggers[name]

        logger = logging.getLogger(name)
        logger.setLevel(level)

        if not logger.handlers:
            formatter = logging.Formatter(fmt)

            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)
            logger.addHandler(console_handler)

            if log_file:
                log_dir = os.path.dirname(log_file)
                if log_dir and not os.path.exists(log_dir):
                    os.makedirs(log_dir)

                file_handler = logging.FileHandler(log_file)
                file_handler.setFormatter(formatter)
                logger.addHandler(file_handler)

        cls._loggers[name] = logger
        return logger


logger_factory = LoggerFactory()
