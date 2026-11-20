from pydantic import BaseModel


class DocumentChunk(BaseModel):
    chunk_id: int
    source_document: str
    content: str
