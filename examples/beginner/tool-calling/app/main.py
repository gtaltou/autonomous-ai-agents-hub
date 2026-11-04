import asyncio
import logging

from agent import build_agent
from agents import Runner
from config import (
    get_openai_api_key,
    load_environment,
)

logger = logging.getLogger(__name__)

QUESTION = "What is 457 * 124?"


async def run_agent() -> str:

    load_environment()

    get_openai_api_key()

    agent = build_agent()

    result = await Runner.run(
        agent,
        QUESTION,
    )

    return result.final_output


async def main():

    logger.info("Starting Tool Calling")

    answer = await run_agent()

    print()
    print("🤖 Question:")
    print(QUESTION)

    print()
    print("🤖 Response:")
    print(answer)

    logger.info("Execution completed")


if __name__ == "__main__":
    asyncio.run(main())
