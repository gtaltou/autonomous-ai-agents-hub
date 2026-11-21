import pytest

from app.config.settings import Settings


def test_missing_openai_api_key() -> None:
    settings = Settings()

    with pytest.raises(ValueError):
        settings.openai_api_key
