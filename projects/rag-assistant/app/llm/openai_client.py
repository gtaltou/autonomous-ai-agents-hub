class OpenAIClient:
    """OpenAI client abstraction."""

    def generate(
        self,
        question: str,
        context: str,
    ) -> str:
        raise NotImplementedError("OpenAI integration is not implemented yet.")
