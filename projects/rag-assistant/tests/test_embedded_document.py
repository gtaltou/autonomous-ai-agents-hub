from app.models.document_chunk import (
    DocumentChunk,
)
from app.models.embedded_document import (
    EmbeddedDocument,
)


def test_embedded_document_creation() -> None:
    chunk = DocumentChunk(
        chunk_id=1,
        source_document="test.txt",
        content="Hello",
    )

    document = EmbeddedDocument(
        chunk=chunk,
        embedding=[0.1, 0.2],
    )

    assert document.chunk == chunk
    assert document.embedding == [0.1, 0.2]