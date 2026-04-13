from functools import lru_cache

from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine


@lru_cache(maxsize=1)
def get_engine() -> AsyncEngine:
    from app.config.loader import load_postgres_settings, load_sqla_settings
    
    pg_settings = load_postgres_settings()
    sqla_settings = load_sqla_settings()
    
    return create_async_engine(
        url=pg_settings.dsn,
        echo=sqla_settings.ECHO,
        echo_pool=sqla_settings.ECHO_POOL,
        pool_pre_ping=True,
        pool_size=sqla_settings.POOL_SIZE,
        max_overflow=sqla_settings.MAX_OVERFLOW
    )
    