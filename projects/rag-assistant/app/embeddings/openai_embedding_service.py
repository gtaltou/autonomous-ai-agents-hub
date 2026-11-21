class OpenAIEmbeddingService:
    """OpenAI embedding service abstraction."""

    def embed_text(
        self,
        text: str,
    ) -> list[float]:
        raise NotImplementedError("OpenAI embeddings are not implemented yet.")
