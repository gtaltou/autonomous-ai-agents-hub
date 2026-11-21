from app.chunking.text_chunker import chunk_text
from app.llm.openai_client import OpenAIClient
from app.rag.rag_pipeline import RagPipeline
from app.retrieval.retrieval_service import (
    RetrievalService,
)
from app.vectorstore.in_memory_vector_store import (
    InMemoryVectorStore,
)


def main() -> None:
    store = InMemoryVectorStore()

    chunks = chunk_text(
        text="Python is a programming language.",
        source_document="sample.txt",
    )

    store.add_documents(chunks)

    retrieval = RetrievalService(store)

    rag = RagPipeline(
        retrieval_service=retrieval,
        llm=OpenAIClient(),
    )

    answer = rag.answer("What is Python?")

    print(answer)


if __name__ == "__main__":
    main()
