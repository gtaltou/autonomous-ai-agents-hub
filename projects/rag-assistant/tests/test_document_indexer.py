from app.services.document_indexer import (
    DocumentIndexer,
)
from app.vectorstore.in_memory_vector_store import (
    InMemoryVectorStore,
)


def test_index_document() -> None:
    store = InMemoryVectorStore()

    indexer = DocumentIndexer(store)

    indexer.index_document(
        text="Python is awesome",
        source_document="test.txt",
    )

    results = store.similarity_search(
        "python",
    )

    assert len(results) == 1
