import pytest

from app.retrieval.retrieval_service import RetrievalService


def test_retrieve_not_implemented() -> None:
    service = RetrievalService()

    with pytest.raises(NotImplementedError):
        service.retrieve("What is RAG?")
