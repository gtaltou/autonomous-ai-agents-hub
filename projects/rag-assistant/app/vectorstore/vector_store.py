from app.models.document_chunk import DocumentChunk


class VectorStore:
    """Vector store abstraction."""

    def add_documents(
        self,
        documents: list[DocumentChunk],
    ) -> None:
        """Add documents to the vector store."""

        raise NotImplementedError(
            "Vector store insertion is not implemented yet."
        )

    def similarity_search(
        self,
        query: str,
        k: int = 5,
    ) -> list[DocumentChunk]:
        """Search for the most similar documents."""

        raise NotImplementedError(
            "Similarity search is not implemented yet."
        )