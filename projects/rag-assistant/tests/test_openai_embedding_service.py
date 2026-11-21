import pytest

from app.embeddings.openai_embedding_service import (
    OpenAIEmbeddingService,
)


def test_embed_text_not_implemented() -> None:
    service = OpenAIEmbeddingService()

    with pytest.raises(NotImplementedError):
        service.embed_text("Python")
