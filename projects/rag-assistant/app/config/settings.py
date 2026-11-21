import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    """Application settings."""

    @property
    def openai_api_key(self) -> str:
        api_key = os.getenv(
            "OPENAI_API_KEY",
        )

        if api_key is None:
            raise ValueError(
                "OPENAI_API_KEY environment variable is not set.",
            )

        return api_key
