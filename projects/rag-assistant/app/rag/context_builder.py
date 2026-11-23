from app.models.document_chunk import DocumentChunk


class ContextBuilder:
    """Builds context from retrieved chunks."""

    def build(
        self,
        chunks: list[DocumentChunk],
    ) -> str:
        return "\n\n".join(chunk.content for chunk in chunks)
