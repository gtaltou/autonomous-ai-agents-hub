from openai import OpenAI

from app.config.settings import Settings


class OpenAIClient:
    """OpenAI client."""

    def __init__(self) -> None:
        settings = Settings()

        self.client = OpenAI(
            api_key=settings.openai_api_key,
        )
