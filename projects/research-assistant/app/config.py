import os
from pathlib import Path

from dotenv import load_dotenv


def load_environment() -> None:

    env_path = Path(".env")

    if env_path.exists():
        load_dotenv()


def get_openai_api_key() -> str:

    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise ValueError(
            "OPENAI_API_KEY is missing."
        )

    return api_key