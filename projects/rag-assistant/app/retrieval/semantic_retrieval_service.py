# app/retrieval/semantic_retrieval_service.py

from app.embeddings.openai_embedding_service import (
    OpenAIEmbeddingService,
)
from app.models.embedded_document import (
    EmbeddedDocument,
)
from app.vectorstore.semantic_vector_store import (
    SemanticVectorStore,
)


class SemanticRetrievalService:
    """Semantic retrieval service."""

    def __init__(
        self,
        vector_store: SemanticVectorStore,
        embedding_service: OpenAIEmbeddingService,
    ) -> None:
        self.vector_store = vector_store
        self.embedding_service = embedding_service

    def retrieve(
        self,
        query: str,
        k: int = 5,
    ) -> list[EmbeddedDocument]:
        query_embedding = self.embedding_service.embed_text(
            query,
        )

        return self.vector_store.similarity_search(
            query_embedding,
            k,
        )
