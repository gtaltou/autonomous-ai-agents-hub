from unittest.mock import Mock

from app.models.document_chunk import (
    DocumentChunk,
)
from app.services.embedding_indexer import (
    EmbeddingIndexer,
)


def test_index_creates_embedded_documents() -> None:
    embedding_service = Mock()

    embedding_service.embed_text.return_value = [
        0.1,
        0.2,
        0.3,
    ]

    indexer = EmbeddingIndexer(
        embedding_service=embedding_service,
    )

    chunks = [
        DocumentChunk(
            chunk_id=1,
            source_document="test.txt",
            content="Hello world",
        ),
    ]

    embedded_documents = indexer.index(
        chunks,
    )

    assert len(embedded_documents) == 1

    assert (
        embedded_documents[0].embedding
        == [0.1, 0.2, 0.3]
    )

    assert (
        embedded_documents[0].chunk.content
        == "Hello world"
    )