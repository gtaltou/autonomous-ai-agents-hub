from app.retrieval.retrieval_service import (
    RetrievalService,
)


class RagPipeline:
    """Simple RAG pipeline."""

    def __init__(
        self,
        retrieval_service: RetrievalService,
    ) -> None:
        self.retrieval_service = retrieval_service

    def answer(
        self,
        question: str,
    ) -> str:
        chunks = self.retrieval_service.retrieve(
            question,
        )

        return "\n".join(chunk.content for chunk in chunks)
