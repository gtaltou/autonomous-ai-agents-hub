from app.models.document_chunk import DocumentChunk
from app.retrieval.retrieval_service import RetrievalService
from app.vectorstore.in_memory_vector_store import (
    InMemoryVectorStore,
)


def test_retrieve_returns_documents() -> None:
    store = InMemoryVectorStore()

    store.add_documents(
        [
            DocumentChunk(
                chunk_id=1,
                source_document="test.txt",
                content="Hello World",
            )
        ]
    )

    retrieval = RetrievalService(store)

    results = retrieval.retrieve("hello")

    assert len(results) == 1
