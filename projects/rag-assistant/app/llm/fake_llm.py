class FakeLLM:
    """Simple fake LLM used for testing."""

    def generate(
        self,
        context: str,
        question: str,
    ) -> str:
        return f"Question: {question}\nContext: {context}"
