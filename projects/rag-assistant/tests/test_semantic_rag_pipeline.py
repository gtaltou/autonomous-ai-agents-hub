from unittest.mock import Mock

from app.llm.fake_llm import FakeLLM
from app.models.document_chunk import (
    DocumentChunk,
)
from app.models.embedded_document import (
    EmbeddedDocument,
)
from app.rag.semantic_rag_pipeline import (
    SemanticRagPipeline,
)


def test_answer_returns_context() -> None:
    document = EmbeddedDocument(
        chunk=DocumentChunk(
            chunk_id=1,
            source_document="python.txt",
            content="Python is a programming language.",
        ),
        embedding=[1.0, 0.0],
    )

    retrieval_service = Mock()

    retrieval_service.retrieve.return_value = [
        document,
    ]

    pipeline = SemanticRagPipeline(
        retrieval_service=retrieval_service,
        llm=FakeLLM(),
    )

    answer = pipeline.answer(
        "What is Python?",
    )

    assert "Python is a programming language." in answer
