import pytest
from pytest import MonkeyPatch
from pydantic import ValidationError

from app.config.settings import AppSettings


def test_app_settings_invalid_input_raises_validation_error(monkeypatch: MonkeyPatch):
    monkeypatch.setenv("APP_DEBUG_MODE", "not true")
    monkeypatch.setenv("APP_LOGGING_LEVEL", "logging")
    
    with pytest.raises(ValidationError):
        AppSettings()


def test_app_settings_load_from_env(monkeypatch: MonkeyPatch):
    monkeypatch.setenv("APP_DEBUG_MODE", "true")
    monkeypatch.setenv("APP_LOGGING_LEVEL", "INFO")
    
    settings = AppSettings()
    
    assert settings.DEBUG_MODE is True
    assert settings.LOGGING_LEVEL == "INFO"
