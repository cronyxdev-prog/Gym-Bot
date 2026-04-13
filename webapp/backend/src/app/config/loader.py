from functools import lru_cache

from app.config.settings import (
    AppSettings, 
    PostgresSettings,
    SqlaSettings
)


@lru_cache(maxsize=1)
def load_app_settings() -> AppSettings:
    return AppSettings()


@lru_cache(maxsize=1)
def load_postgres_settings() -> PostgresSettings:
    return PostgresSettings() # type: ignore[call-arg]


@lru_cache(maxsize=1)
def load_sqla_settings() -> SqlaSettings:
    return SqlaSettings()