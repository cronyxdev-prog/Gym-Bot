from pydantic import PostgresDsn
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


class PostgresSettings(BaseSettings):
    model_config = _BASE_CONFIG | SettingsConfigDict(env_prefix="PG_")
    
    DB: str
    HOST: str
    PORT: int
    USER: str
    PASSWORD: str
    
    @property
    def dsn(self) -> str:
        return str(
            PostgresDsn.build(
                scheme="postgresql+asyncpg",
                username=self.USER,
                password=self.PASSWORD,
                host=self.HOST,
                port=self.PORT,
                path=self.DB
            )
        )
    

class SqlaSettings(BaseSettings):
    model_config = _BASE_CONFIG | SettingsConfigDict(env_prefix="SQLA_")
    
    ECHO: bool = False
    ECHO_POOL: bool = False
    POOL_SIZE: int = 15
    MAX_OVERFLOW: int = 10
    