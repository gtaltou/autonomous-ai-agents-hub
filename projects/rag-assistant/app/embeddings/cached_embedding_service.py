from app.embeddings.embedding_service import (
    EmbeddingService,
)


class CachedEmbeddingService(
    EmbeddingService,
):
    """Embedding service with in-memory cache."""

    def __init__(
        self,
        embedding_service: EmbeddingService,
    ) -> None:
        self.embedding_service = embedding_service

        self._cache: dict[
            str,
            list[float],
        ] = {}

    def embed_text(
        self,
        text: str,
    ) -> list[float]:
        if text in self._cache:
            return self._cache[text]

        embedding = self.embedding_service.embed_text(
            text,
        )

        self._cache[text] = embedding

        return embedding