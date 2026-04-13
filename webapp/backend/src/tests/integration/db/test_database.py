from sqlalchemy import text


async def test_db_connection(engine):
    async with engine.begin() as conn:
        result = await conn.execute(text("SELECT 1"))
        assert result.scalar_one() == 1


async def test_session_execute(session):
    result = await session.execute(text("SELECT 1"))
    assert result.scalar_one() == 1


async def test_transaction_rollback(engine):
    async with engine.connect() as conn:
        async with conn.begin():
            await conn.execute(text("CREATE TEMP TABLE _tx_test (id int)"))
            await conn.execute(text("INSERT INTO _tx_test VALUES (1)"))

        async with conn.begin():
            await conn.execute(text("INSERT INTO _tx_test VALUES (2)"))
            await conn.rollback()

        async with conn.begin():
            result = await conn.execute(text("SELECT id FROM _tx_test"))
            rows = result.scalars().all()
            assert rows == [1]

            await conn.execute(text("DROP TABLE _tx_test"))
            