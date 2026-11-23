import pytest

from app.vectorstore.vector_store import VectorStore


def test_add_documents_not_implemented() -> None:
    store = VectorStore()

    with pytest.raises(NotImplementedError):
        store.add_documents([])


def test_similarity_search_not_implemented() -> None:
    store = VectorStore()

    with pytest.raises(NotImplementedError):
        store.similarity_search("hello")
