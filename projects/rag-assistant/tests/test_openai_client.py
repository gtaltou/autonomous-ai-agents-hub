import pytest

from app.llm.openai_client import OpenAIClient


def test_client_requires_api_key(
    monkeypatch,
) -> None:
    monkeypatch.delenv(
        "OPENAI_API_KEY",
        raising=False,
    )

    with pytest.raises(ValueError):
        OpenAIClient()


def test_client_initialization(
    monkeypatch,
) -> None:
    monkeypatch.setenv(
        "OPENAI_API_KEY",
        "test-key",
    )

    client = OpenAIClient()

    assert client is not None
