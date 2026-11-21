from typing import Protocol


class EmbeddingInterface(Protocol):
    def embed_text(
        self,
        text: str,
    ) -> list[float]:
        ...