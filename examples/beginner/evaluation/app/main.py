import asyncio
import logging

from agents import Runner

from app.agent import build_agent
from app.config import (
    get_openai_api_key,
    load_environment,
)
from app.evaluator import evaluate_person
from app.models import Person

logger = logging.getLogger(__name__)

TEXT = """
John Doe is 42 years old and lives in Paris.
"""


async def run_agent() -> Person:

    load_environment()

    get_openai_api_key()

    agent = build_agent()

    result = await Runner.run(
        agent,
        TEXT,
    )

    return result.final_output


async def main():

    logger.info("Starting Evaluation Example")

    expected = Person(
        name="John Doe",
        age=42,
        city="Paris",
    )

    actual = await run_agent()

    evaluation_result = evaluate_person(
        expected,
        actual,
    )

    print()
    print("📝 Input:")
    print(TEXT.strip())

    print()
    print("🎯 Expected:")
    print(expected)

    print()
    print("🤖 Actual:")
    print(actual)

    print()
    print("📊 Evaluation Result:")

    if evaluation_result:
        print("✅ PASS")
    else:
        print("❌ FAIL")

    logger.info("Execution completed")


if __name__ == "__main__":
    asyncio.run(main())