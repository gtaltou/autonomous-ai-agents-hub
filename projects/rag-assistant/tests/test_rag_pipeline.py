from app.models.document_chunk import DocumentChunk
from app.rag.rag_pipeline import RagPipeline
from app.retrieval.retrieval_service import (
    RetrievalService,
)
from app.vectorstore.in_memory_vector_store import (
    InMemoryVectorStore,
)


def test_answer_returns_context() -> None:
    store = InMemoryVectorStore()

    store.add_documents(
        [
            DocumentChunk(
                chunk_id=1,
                source_document="python.txt",
                content="Python is awesome",
            ),
        ]
    )

    retrieval = RetrievalService(store)

    rag = RagPipeline(retrieval)

    answer = rag.answer("python")

    assert "Python" in answer


def test_answer_returns_empty_string() -> None:
    store = InMemoryVectorStore()

    retrieval = RetrievalService(store)

    rag = RagPipeline(retrieval)

    answer = rag.answer("python")

    assert answer == ""
