from app.embeddings.openai_embedding_service import (
    OpenAIEmbeddingService,
)
from app.models.document_chunk import (
    DocumentChunk,
)
from app.models.embedded_document import (
    EmbeddedDocument,
)


class EmbeddingIndexer:
    """Convert chunks into embedded documents."""

    def __init__(
        self,
        embedding_service: OpenAIEmbeddingService,
    ) -> None:
        self.embedding_service = embedding_service

    def index(
        self,
        chunks: list[DocumentChunk],
    ) -> list[EmbeddedDocument]:
        return [
            EmbeddedDocument(
                chunk=chunk,
                embedding=self.embedding_service.embed_text(
                    chunk.content,
                ),
            )
            for chunk in chunks
        ]