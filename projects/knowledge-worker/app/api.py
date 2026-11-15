from fastapi import FastAPI

from app.services.knowledge_service import (
    KnowledgeService,
)

app = FastAPI(
    title="Knowledge Worker API",
    version="1.2.0",
)


@app.get("/health")
def health() -> dict[str, str]:
    return {
        "status": "ok",
    }


@app.get("/topics")
def get_topics():
    return (
        KnowledgeService
        .get_topics()
    )