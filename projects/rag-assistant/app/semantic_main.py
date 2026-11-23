from app.chunking.text_chunker import chunk_text
from app.embeddings.cached_embedding_service import (
    CachedEmbeddingService,
)
from app.embeddings.openai_embedding_service import (
    OpenAIEmbeddingService,
)
from app.llm.openai_client import OpenAIClient
from app.rag.semantic_rag_pipeline import (
    SemanticRagPipeline,
)
from app.retrieval.semantic_retrieval_service import (
    SemanticRetrievalService,
)
from app.services.embedding_indexer import (
    EmbeddingIndexer,
)
from app.vectorstore.semantic_vector_store import (
    SemanticVectorStore,
)


def main() -> None:
    embedding_service = CachedEmbeddingService(
        OpenAIEmbeddingService(),
    )

    vector_store = SemanticVectorStore()

    chunks = chunk_text(
        text="Python is a programming language.",
        source_document="python.txt",
    )

    embedding_indexer = EmbeddingIndexer(
        embedding_service,
    )

    embedded_documents = embedding_indexer.index(
        chunks,
    )

    vector_store.add_documents(
        embedded_documents,
    )

    retrieval_service = SemanticRetrievalService(
        vector_store=vector_store,
        embedding_service=embedding_service,
    )

    rag = SemanticRagPipeline(
        retrieval_service=retrieval_service,
        llm=OpenAIClient(),
    )

    answer = rag.answer(
        "What is Python?",
    )

    print(answer)


if __name__ == "__main__":
    main()
