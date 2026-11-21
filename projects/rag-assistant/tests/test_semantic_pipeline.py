from unittest.mock import Mock

from app.models.document_chunk import (
    DocumentChunk,
)
from app.retrieval.semantic_retrieval_service import (
    SemanticRetrievalService,
)
from app.services.embedding_indexer import (
    EmbeddingIndexer,
)
from app.vectorstore.semantic_vector_store import (
    SemanticVectorStore,
)


def test_semantic_retrieval_flow() -> None:
    embedding_service = Mock()

    embedding_service.embed_text.side_effect = [
        [1.0, 0.0],  # document
        [1.0, 0.0],  # query
    ]

    indexer = EmbeddingIndexer(
        embedding_service,
    )

    store = SemanticVectorStore()

    chunk = DocumentChunk(
        chunk_id=1,
        source_document="python.txt",
        content="Python",
    )

    embedded = indexer.index([chunk])

    store.add_documents(
        embedded,
    )

    retrieval = SemanticRetrievalService(
        store,
        embedding_service,
    )

    results = retrieval.retrieve(
        "What is Python?",
    )

    assert len(results) == 1

    assert results[0].chunk.content == "Python"
