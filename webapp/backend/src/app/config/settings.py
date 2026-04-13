from pydantic_settings import BaseSettings, SettingsConfigDict

from app.config.logging_ import LoggingLevel


_BASE_CONFIG = SettingsConfigDict(
    env_file=".env",
    env_file_encoding="utf-8",
    extra="ignore"
)


class AppSettings(BaseSettings):
    model_config = _BASE_CONFIG | SettingsConfigDict(env_prefix="APP_")
    
    DEBUG_MODE: bool = False
    LOGGING_LEVEL: LoggingLevel = LoggingLevel.INFO
    