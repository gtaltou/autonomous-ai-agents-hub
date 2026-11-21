import pytest

from app.config.settings import Settings


def test_missing_openai_api_key(
    monkeypatch,
) -> None:
    monkeypatch.delenv(
        "OPENAI_API_KEY",
        raising=False,
    )

    settings = Settings()

    with pytest.raises(ValueError):
        settings.openai_api_key


def test_openai_api_key_returns_value(
    monkeypatch,
) -> None:
    monkeypatch.setenv(
        "OPENAI_API_KEY",
        "test-key",
    )

    settings = Settings()

    assert settings.openai_api_key == "test-key"
