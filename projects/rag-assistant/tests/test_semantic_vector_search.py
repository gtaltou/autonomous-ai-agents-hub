from app.models.document_chunk import (
    DocumentChunk,
)
from app.models.embedded_document import (
    EmbeddedDocument,
)
from app.vectorstore.semantic_vector_store import (
    SemanticVectorStore,
)


def test_similarity_search_returns_best_match() -> None:
    store = SemanticVectorStore()

    store.add_documents(
        [
            EmbeddedDocument(
                chunk=DocumentChunk(
                    chunk_id=1,
                    source_document="a.txt",
                    content="A",
                ),
                embedding=[1.0, 0.0],
            ),
            EmbeddedDocument(
                chunk=DocumentChunk(
                    chunk_id=2,
                    source_document="b.txt",
                    content="B",
                ),
                embedding=[0.0, 1.0],
            ),
        ]
    )

    results = store.similarity_search(
        [1.0, 0.0],
    )

    assert results[0].chunk.content == "A"
