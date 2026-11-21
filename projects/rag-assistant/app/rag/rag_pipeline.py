from app.llm.llm_interface import LLMInterface
from app.rag.context_builder import ContextBuilder
from app.retrieval.retrieval_service import (
    RetrievalService,
)


class RagPipeline:
    """Simple RAG pipeline."""

    def __init__(
        self,
        retrieval_service: RetrievalService,
        llm: LLMInterface,
    ) -> None:
        self.retrieval_service = retrieval_service
        self.context_builder = ContextBuilder()
        self.llm = llm

    def answer(
        self,
        question: str,
    ) -> str:
        chunks = self.retrieval_service.retrieve(
            question,
        )

        context = self.context_builder.build(
            chunks,
        )

        return self.llm.generate(
            question=question,
            context=context,
        )
