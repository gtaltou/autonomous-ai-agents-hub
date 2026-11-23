from openai import OpenAI

from app.config.settings import Settings
from app.llm.llm_interface import LLMInterface


class OpenAIClient(LLMInterface):
    """OpenAI client."""

    def __init__(self) -> None:
        settings = Settings()

        self.client = OpenAI(
            api_key=settings.openai_api_key,
        )

    def generate(
        self,
        question: str,
        context: str,
    ) -> str:
        response = self.client.responses.create(
            model="gpt-5-mini",
            input=f"""
SYSTEM ROLE

You are a strict Retrieval-Augmented Generation (RAG)
assistant.

RULES

1. Use ONLY the information contained in CONTEXT.
2. Never add external information.
3. Never guess.
4. If the answer is not fully present in the context,
   respond exactly:

   I do not have enough information in the provided context.

5. Keep answers clear and concise.

CONTEXT

{context}

QUESTION

{question}
""",
        )

        return response.output_text
