from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker


def get_session_maker() -> async_sessionmaker[AsyncSession]:
    from core.db.engine import get_engine
    
    engine = get_engine()
    
    return async_sessionmaker(
        bind=engine,
        class_=AsyncSession,
        expire_on_commit=False
    )
    