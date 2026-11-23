import pytest

from app.embeddings.embedding_service import EmbeddingService


def test_embed_text_not_implemented() -> None:
    service = EmbeddingService()

    with pytest.raises(NotImplementedError):
        service.embed_text("hello world")


def test_embed_documents_not_implemented() -> None:
    service = EmbeddingService()

    with pytest.raises(NotImplementedError):
        service.embed_documents(["doc 1", "doc 2"])
