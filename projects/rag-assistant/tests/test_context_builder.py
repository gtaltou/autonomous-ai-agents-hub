from app.models.document_chunk import DocumentChunk
from app.rag.context_builder import ContextBuilder


def test_build_context() -> None:
    builder = ContextBuilder()

    context = builder.build(
        [
            DocumentChunk(
                chunk_id=1,
                source_document="a.txt",
                content="First chunk",
            ),
            DocumentChunk(
                chunk_id=2,
                source_document="b.txt",
                content="Second chunk",
            ),
        ]
    )

    assert "First chunk" in context
    assert "Second chunk" in context
