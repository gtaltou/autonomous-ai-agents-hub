import pytest

from app.llm.openai_client import OpenAIClient


def test_generate_not_implemented() -> None:
    client = OpenAIClient()

    with pytest.raises(NotImplementedError):
        client.generate(
            question="What is Python?",
            context="Python is awesome",
        )
