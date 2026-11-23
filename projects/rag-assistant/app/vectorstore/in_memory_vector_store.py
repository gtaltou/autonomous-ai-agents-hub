from app.models.document_chunk import DocumentChunk


class InMemoryVectorStore:
    """Simple in-memory vector store."""

    def __init__(self) -> None:
        self._documents: list[DocumentChunk] = []

    def add_documents(
        self,
        documents: list[DocumentChunk],
    ) -> None:
        self._documents.extend(documents)

    def similarity_search(
        self,
        query: str,
        k: int = 5,
    ) -> list[DocumentChunk]:
        matches = [
            document
            for document in self._documents
            if query.lower() in document.content.lower()
        ]

        return matches[:k]