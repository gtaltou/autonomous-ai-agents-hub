from typing import List


class EmbeddingService:
    """Service responsible for generating embeddings."""

    def embed_text(
        self,
        text: str,
    ) -> List[float]:
        """Generate an embedding for a single text."""

        raise NotImplementedError(
            "Embedding generation is not implemented yet."
        )

    def embed_documents(
        self,
        documents: List[str],
    ) -> List[List[float]]:
        """Generate embeddings for multiple documents."""

        return [
            self.embed_text(document)
            for document in documents
        ]