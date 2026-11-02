import pytest

from app.config import get_openai_api_key


def test_missing_api_key(monkeypatch):

    monkeypatch.delenv(
        "OPENAI_API_KEY",
        raising=False
    )

    with pytest.raises(ValueError):
        get_openai_api_key()