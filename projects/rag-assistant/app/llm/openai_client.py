from openai import OpenAI

from app.config.settings import Settings


class OpenAIClient:
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
        """Generate an answer using OpenAI."""

        response = self.client.responses.create(
            model="gpt-5-mini",
            input=f"""
Question:
{question}

Context:
{context}
""",
        )

        return response.output_text