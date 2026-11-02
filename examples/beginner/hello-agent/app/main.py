import asyncio
import logging

from agents import Runner

from config import load_environment
from config import get_openai_api_key
from agent import build_agent

QUESTION = "Explain what an AI Agent is."


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


async def run_agent() -> str:

    load_environment()

    get_openai_api_key()

    agent = build_agent()

    result = await Runner.run(
        agent,
        QUESTION
    )

    return result.final_output


async def main():

    logging.info("Starting Hello Agent")

    answer = await run_agent()

    print("\n🤖 Question:\n")
    print(QUESTION)

    print("\n🤖 Response:\n")
    print(answer)

    logging.info("Execution completed")


if __name__ == "__main__":
    asyncio.run(main())