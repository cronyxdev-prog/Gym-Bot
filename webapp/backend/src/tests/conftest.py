import asyncio

import pytest
from sqlalchemy.ext.asyncio import (
    async_sessionmaker,
    create_async_engine,
)

from app.core.db.base import Base 

DATABASE_URL = "sqlite+aiosqlite:///:memory:"


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session")
async def engine():
    engine = create_async_engine(DATABASE_URL)
    yield engine
    await engine.dispose()


@pytest.fixture(scope="session", autouse=True)
async def create_all(engine):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@pytest.fixture
async def session(engine):
    async_session = async_sessionmaker(engine, expire_on_commit=False)

    async with engine.connect() as conn:
        trans = await conn.begin()

        async with async_session(bind=conn) as session:
            yield session

        await trans.rollback()
        