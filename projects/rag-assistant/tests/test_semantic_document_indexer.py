from unittest.mock import Mock

from app.models.document_chunk import (
    DocumentChunk,
)
from app.models.embedded_document import (
    EmbeddedDocument,
)
from app.retrieval.semantic_retrieval_service import (
    SemanticRetrievalService,
)
from app.vectorstore.semantic_vector_store import (
    SemanticVectorStore,
)


def test_retrieve_returns_documents() -> None:
    store = Mock(spec=SemanticVectorStore)

    document = EmbeddedDocument(
        chunk=DocumentChunk(
            chunk_id=1,
            source_document="test.txt",
            content="hello",
        ),
        embedding=[0.1, 0.2],
    )

    store.similarity_search.return_value = [
        document,
    ]

    embedding_service = Mock()

    embedding_service.embed_text.return_value = [
        0.1,
        0.2,
    ]

    service = SemanticRetrievalService(
        vector_store=store,
        embedding_service=embedding_service,
    )

    results = service.retrieve(
        "hello",
    )

    assert len(results) == 1
    assert results[0] == document