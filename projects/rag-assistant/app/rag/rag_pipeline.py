from app.rag.context_builder import ContextBuilder
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
        self.context_builder = ContextBuilder()

    def answer(
        self,
        question: str,
    ) -> str:
        chunks = self.retrieval_service.retrieve(
            question,
        )

        return self.context_builder.build(
            chunks,
        )
