import logging
from contextlib import asynccontextmanager
from collections.abc import AsyncIterator

from sqlalchemy.ext.asyncio import AsyncSession

from core.db.session_maker import get_session_maker

logger = logging.getLogger(__name__)


@asynccontextmanager
async def get_db() -> AsyncIterator[AsyncSession]:
    session_maker = get_session_maker()
    
    async with session_maker() as session:
        try:
            yield session
        except Exception:
            logger.error(
                "Database error occurred, rolling back transaction", 
                exc_info=True
            )
            await session.rollback()
            raise
        