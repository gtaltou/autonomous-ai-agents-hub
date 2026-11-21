from app.llm.fake_llm import FakeLLM
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

    rag = RagPipeline(
        retrieval_service=retrieval,
        llm=FakeLLM(),
    )

    answer = rag.answer("python")

    assert "Python is awesome" in answer


def test_answer_returns_empty_response() -> None:
    store = InMemoryVectorStore()

    retrieval = RetrievalService(store)

    rag = RagPipeline(
        retrieval_service=retrieval,
        llm=FakeLLM(),
    )

    answer = rag.answer("python")

    assert "Question: python" in answer
    assert "Context:" in answer


def test_answer_contains_question() -> None:
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

    rag = RagPipeline(
        retrieval_service=retrieval,
        llm=FakeLLM(),
    )

    answer = rag.answer("python")

    assert "Question: python" in answer
    assert "Python is awesome" in answer
