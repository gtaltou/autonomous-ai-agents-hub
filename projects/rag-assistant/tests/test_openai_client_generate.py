from unittest.mock import Mock, patch

from app.llm.openai_client import OpenAIClient


def test_generate_returns_response_text(
    monkeypatch,
) -> None:
    monkeypatch.setenv(
        "OPENAI_API_KEY",
        "test-key",
    )

    client = OpenAIClient()

    mock_response = Mock()
    mock_response.output_text = "Python is a programming language."

    with patch.object(
        client.client.responses,
        "create",
        return_value=mock_response,
    ) as mock_create:
        result = client.generate(
            question="What is Python?",
            context="Python is awesome.",
        )

    assert result == "Python is a programming language."

    mock_create.assert_called_once()
