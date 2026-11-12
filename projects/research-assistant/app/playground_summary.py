import asyncio

from agents import Runner

from app.agents.search import (
    build_search_agent,
)
from app.agents.summarizer import (
    build_summarizer_agent,
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
    print("RESEARCH ASSISTANT - AGENT HANDOFF")
    print("=" * 60)

    question = (
        "What is quantum computing?"
    )

    print()
    print(f"Question: {question}")

    #
    # SEARCH AGENT
    #

    search_agent = (
        build_search_agent()
    )

    search_result = (
        await Runner.run(
            search_agent,
            question,
        )
    ).final_output

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

    #
    # SUMMARIZER AGENT
    #

    summarizer_agent = (
        build_summarizer_agent()
    )

    summary_input = f"""
    Topic:
    {search_result.topic}

    Findings:
    {chr(10).join(search_result.findings)}

    Source Count:
    {search_result.source_count}
    """

    summary_result = (
        await Runner.run(
            summarizer_agent,
            summary_input,
        )
    ).final_output

    print()
    print("SUMMARY RESULT")
    print("-" * 60)

    print()
    print("Summary:")

    print(
        summary_result.summary
    )

    print()
    print("Key Points:")

    for index, point in enumerate(
        summary_result.key_points,
        start=1,
    ):
        print(
            f"{index}. {point}"
        )

    print()
    print(
        f"Confidence Score: "
        f"{summary_result.confidence_score}"
    )

    print()
    print("=" * 60)
    print("DONE")
    print("=" * 60)


if __name__ == "__main__":
    asyncio.run(main())