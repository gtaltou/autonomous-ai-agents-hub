from app.models.document_chunk import DocumentChunk
from app.vectorstore.in_memory_vector_store import (
    InMemoryVectorStore,
)


class RetrievalService:
    """Retrieves relevant chunks."""

    def __init__(
        self,
        vector_store: InMemoryVectorStore,
    ) -> None:
        self.vector_store = vector_store

    def retrieve(
        self,
        query: str,
        k: int = 5,
    ) -> list[DocumentChunk]:
        return self.vector_store.similarity_search(
            query=query,
            k=k,
        )
