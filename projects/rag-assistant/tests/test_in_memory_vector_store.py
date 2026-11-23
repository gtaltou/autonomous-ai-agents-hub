from app.models.document_chunk import DocumentChunk
from app.vectorstore.in_memory_vector_store import (
    InMemoryVectorStore,
)


def test_similarity_search_filters_results() -> None:
    store = InMemoryVectorStore()

    store.add_documents(
        [
            DocumentChunk(
                chunk_id=1,
                source_document="python.txt",
                content="Python is awesome",
            ),
            DocumentChunk(
                chunk_id=2,
                source_document="java.txt",
                content="Java is verbose",
            ),
        ]
    )

    results = store.similarity_search("python")

    assert len(results) == 1
    assert results[0].chunk_id == 1
