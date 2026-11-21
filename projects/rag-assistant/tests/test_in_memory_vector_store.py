from app.models.document_chunk import DocumentChunk
from app.vectorstore.in_memory_vector_store import (
    InMemoryVectorStore,
)


def test_add_documents() -> None:
    store = InMemoryVectorStore()

    documents = [
        DocumentChunk(
            chunk_id=1,
            source_document="test.txt",
            content="Hello world",
        )
    ]

    store.add_documents(documents)

    results = store.similarity_search("hello")

    assert len(results) == 1


def test_similarity_search_respects_k() -> None:
    store = InMemoryVectorStore()

    documents = [
        DocumentChunk(
            chunk_id=i,
            source_document="test.txt",
            content=f"Chunk {i}",
        )
        for i in range(10)
    ]

    store.add_documents(documents)

    results = store.similarity_search(
        "query",
        k=3,
    )

    assert len(results) == 3
