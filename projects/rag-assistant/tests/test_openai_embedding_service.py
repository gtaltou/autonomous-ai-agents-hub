from unittest.mock import Mock, patch

from app.embeddings.openai_embedding_service import (
    OpenAIEmbeddingService,
)


def test_embed_text_returns_embedding(
    monkeypatch,
) -> None:
    monkeypatch.setenv(
        "OPENAI_API_KEY",
        "test-key",
    )

    service = OpenAIEmbeddingService()

    embedding = [0.1, 0.2, 0.3]

    mock_response = Mock()
    mock_response.data = [
        Mock(
            embedding=embedding,
        )
    ]

    with patch.object(
        service.client.embeddings,
        "create",
        return_value=mock_response,
    ):
        result = service.embed_text(
            "Python",
        )

    assert result == embedding
