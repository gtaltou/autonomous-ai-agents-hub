from unittest.mock import Mock

from app.embeddings.cached_embedding_service import (
    CachedEmbeddingService,
)


def test_cache_is_text_specific() -> None:
    embedding_service = Mock()

    embedding_service.embed_text.side_effect = [
        [1.0],
        [2.0],
    ]

    service = CachedEmbeddingService(
        embedding_service,
    )

    python_embedding = service.embed_text(
        "Python",
    )

    ai_embedding = service.embed_text(
        "AI",
    )

    assert python_embedding == [1.0]
    assert ai_embedding == [2.0]

    assert (
        embedding_service.embed_text.call_count
        == 2
    )