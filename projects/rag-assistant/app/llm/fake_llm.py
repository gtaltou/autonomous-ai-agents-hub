from app.llm.llm_interface import LLMInterface


class FakeLLM(LLMInterface):
    """Simple fake LLM."""

    def generate(
        self,
        question: str,
        context: str,
    ) -> str:
        return f"Question: {question}\nContext: {context}"
