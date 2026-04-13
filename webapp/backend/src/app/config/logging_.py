import logging.config
from enum import StrEnum


class LoggingLevel(StrEnum):
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"


def setup_logging(level: LoggingLevel = LoggingLevel.INFO) -> None:
    logging.config.dictConfig(
        {
            "version": 1,
            "disable_existing_loggers": False,
            "formatters": {
                "default": {
                    "format": "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
                }
            },
            "handlers": {
                "console": {
                    "class": "logging.StreamHandler",
                    "formatter": "default"
                }
            },
            "root": {
                "level": level,
                "handlers": ["console"]
            }
        }
    )
    