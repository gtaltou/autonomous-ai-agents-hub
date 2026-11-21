from app.embeddings.fake_embedding_service import (
    FakeEmbeddingService,
)


def test_embed_text_returns_embedding() -> None:
    service = FakeEmbeddingService()

    embedding = service.embed_text("hello")

    assert len(embedding) == 2


def test_embed_text_is_deterministic() -> None:
    service = FakeEmbeddingService()

    embedding_1 = service.embed_text("hello")
    embedding_2 = service.embed_text("hello")

    assert embedding_1 == embedding_2
