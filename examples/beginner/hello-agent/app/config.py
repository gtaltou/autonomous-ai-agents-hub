from pathlib import Path
import os

from dotenv import load_dotenv


def load_environment() -> None:
    """
    Load environment variables.
    """

    env_path = Path(".env")

    if env_path.exists():
        load_dotenv()


def get_openai_api_key() -> str:
    """
    Retrieve OpenAI API key.
    """

    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise ValueError("OPENAI_API_KEY is missing from environment.")

    if not api_key.startswith("sk-"):
        raise ValueError("OPENAI_API_KEY format appears invalid.")

    return api_key