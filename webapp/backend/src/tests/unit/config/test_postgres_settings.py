from pytest import MonkeyPatch

from app.config.settings import PostgresSettings


def _set_env(monkeypatch: MonkeyPatch):
    monkeypatch.setenv("PG_DB", "testdb")
    monkeypatch.setenv("PG_HOST", "localhost")
    monkeypatch.setenv("PG_PORT", "5432")
    monkeypatch.setenv("PG_USER", "user")
    monkeypatch.setenv("PG_PASSWORD", "pass")


def test_postgres_settings_load_from_env(monkeypatch: MonkeyPatch):
    _set_env(monkeypatch)

    settings = PostgresSettings() # type: ignore[call-arg]

    assert settings.DB == "testdb"
    assert settings.HOST == "localhost"
    assert settings.PORT == 5432
    assert settings.USER == "user"
    assert settings.PASSWORD == "pass"


def test_postgres_dsn(monkeypatch: MonkeyPatch):
    _set_env(monkeypatch)

    settings = PostgresSettings() # type: ignore[call-arg]

    assert settings.dsn == "postgresql+asyncpg://user:pass@localhost:5432/testdb"