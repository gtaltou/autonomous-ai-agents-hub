from openai import OpenAI

from app.config.settings import Settings
from app.embeddings.embedding_service import (
    EmbeddingService,
)


class OpenAIEmbeddingService(
    EmbeddingService,
):
    """OpenAI embedding service."""

    def __init__(
        self,
    ) -> None:
        settings = Settings()

        self.client = OpenAI(
            api_key=settings.openai_api_key,
        )

    def embed_text(
        self,
        text: str,
    ) -> list[float]:
        response = self.client.embeddings.create(
            model="text-embedding-3-small",
            input=text,
        )

        return response.data[0].embedding