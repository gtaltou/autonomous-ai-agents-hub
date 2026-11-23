class FakeEmbeddingService:
    """Deterministic embedding generator for testing."""

    def embed_text(self, text: str) -> list[float]:
        return [
            float(len(text)),
            float(sum(ord(char) for char in text)),
        ]
