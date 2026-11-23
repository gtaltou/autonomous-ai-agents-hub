from app.models.embedded_document import (
    EmbeddedDocument,
)
from app.vectorstore.vector_similarity import (
    cosine_similarity,
)


class SemanticVectorStore:
    """Semantic vector store."""

    def __init__(self) -> None:
        self._documents: list[
            EmbeddedDocument
        ] = []

    def add_documents(
        self,
        documents: list[EmbeddedDocument],
    ) -> None:
        self._documents.extend(
            documents,
        )

    def similarity_search(
        self,
        query_embedding: list[float],
        k: int = 5,
    ) -> list[EmbeddedDocument]:
        scored_documents = [
            (
                cosine_similarity(
                    query_embedding,
                    document.embedding,
                ),
                document,
            )
            for document in self._documents
        ]

        scored_documents.sort(
            key=lambda item: item[0],
            reverse=True,
        )

        return [
            document
            for _, document
            in scored_documents[:k]
        ]