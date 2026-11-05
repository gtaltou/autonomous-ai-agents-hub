import asyncio
import logging

from agents import Runner

from app.agent import build_agent
from app.config import (
    get_openai_api_key,
    load_environment,
)

logger = logging.getLogger(__name__)

TEXT = """
John Doe is 42 years old and lives in Paris.
"""


async def run_agent():

    load_environment()

    get_openai_api_key()

    agent = build_agent()

    result = await Runner.run(
        agent,
        TEXT,
    )

    return result.final_output


async def main():

    logger.info("Starting Structured Output Example")

    person = await run_agent()

    print()
    print("📝 Input:")
    print(TEXT.strip())

    print()
    print("✅ Structured Output:")
    print(person)

    print()
    print("📋 Fields:")
    print(f"Name : {person.name}")
    print(f"Age  : {person.age}")
    print(f"City : {person.city}")

    logger.info("Execution completed")


if __name__ == "__main__":
    asyncio.run(main())
