from app.models.document_chunk import DocumentChunk


def chunk_text(
    text: str,
    source_document: str,
    chunk_size: int = 500,
) -> list[DocumentChunk]:
    """
    Split text into fixed-size chunks.
    """

    if not text.strip():
        return []

    chunks: list[DocumentChunk] = []

    for i in range(0, len(text), chunk_size):
        content = text[i : i + chunk_size]

        chunks.append(
            DocumentChunk(
                chunk_id=len(chunks),
                source_document=source_document,
                content=content,
            )
        )

    return chunks
