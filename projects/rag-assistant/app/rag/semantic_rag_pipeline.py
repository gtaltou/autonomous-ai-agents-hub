from app.llm.llm_interface import LLMInterface
from app.rag.context_builder import ContextBuilder
from app.retrieval.semantic_retrieval_service import (
    SemanticRetrievalService,
)


class SemanticRagPipeline:
    """Semantic RAG pipeline."""

    def __init__(
        self,
        retrieval_service: SemanticRetrievalService,
        llm: LLMInterface,
    ) -> None:
        self.retrieval_service = retrieval_service
        self.context_builder = ContextBuilder()
        self.llm = llm

    def answer(
        self,
        question: str,
    ) -> str:
        documents = self.retrieval_service.retrieve(
            question,
        )

        chunks = [document.chunk for document in documents]

        context = self.context_builder.build(
            chunks,
        )

        return self.llm.generate(
            question=question,
            context=context,
        )
