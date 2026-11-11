import asyncio

from agents import Runner

from app.agents.search import (
    build_search_agent,
)
from app.config import (
    get_openai_api_key,
    load_environment,
)


async def main():

    load_environment()

    get_openai_api_key()

    print()
    print("=" * 60)
    print("RESEARCH ASSISTANT PLAYGROUND")
    print("=" * 60)

    question = (
        "What is quantum computing?"
    )

    print()
    print(f"Question: {question}")

    search_agent = (
        build_search_agent()
    )

    result = await Runner.run(
        search_agent,
        question,
    )

    search_result = (
        result.final_output
    )

    print()
    print("SEARCH RESULT")
    print("-" * 60)

    print()
    print(
        f"Topic: {search_result.topic}"
    )

    print()
    print("Findings:")

    for index, finding in enumerate(
        search_result.findings,
        start=1,
    ):
        print(
            f"{index}. {finding}"
        )

    print()
    print(
        f"Source Count: "
        f"{search_result.source_count}"
    )

    print()
    print("=" * 60)
    print("DONE")
    print("=" * 60)


if __name__ == "__main__":
    asyncio.run(main())