from app.models.document_chunk import (
    DocumentChunk,
)
from app.models.embedded_document import (
    EmbeddedDocument,
)
from app.vectorstore.semantic_vector_store import (
    SemanticVectorStore,
)


def test_add_documents() -> None:
    store = SemanticVectorStore()

    chunk = DocumentChunk(
        chunk_id=1,
        source_document="test.txt",
        content="Hello",
    )

    document = EmbeddedDocument(
        chunk=chunk,
        embedding=[0.1, 0.2],
    )

    store.add_documents(
        [document],
    )

    assert len(store._documents) == 1