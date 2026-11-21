from app.models.document_chunk import DocumentChunk


class RetrievalService:
    """RAG retrieval service."""

    def retrieve(
        self,
        query: str,
        k: int = 5,
    ) -> list[DocumentChunk]:
        """Retrieve relevant document chunks."""

        raise NotImplementedError("Retrieval is not implemented yet.")
