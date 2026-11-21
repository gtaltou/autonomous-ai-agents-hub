from app.chunking.text_chunker import chunk_text
from app.vectorstore.in_memory_vector_store import (
    InMemoryVectorStore,
)


class DocumentIndexer:
    """Indexes documents into the vector store."""

    def __init__(
        self,
        vector_store: InMemoryVectorStore,
    ) -> None:
        self.vector_store = vector_store

    def index_document(
        self,
        text: str,
        source_document: str,
    ) -> None:
        chunks = chunk_text(
            text=text,
            source_document=source_document,
        )

        self.vector_store.add_documents(chunks)
