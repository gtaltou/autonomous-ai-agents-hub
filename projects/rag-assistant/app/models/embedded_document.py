from dataclasses import dataclass

from app.models.document_chunk import DocumentChunk


@dataclass
class EmbeddedDocument:
    chunk: DocumentChunk
    embedding: list[float]
