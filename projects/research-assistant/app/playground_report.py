import asyncio

from agents import Runner

from app.agents.fact_checker import (
    build_fact_checker_agent,
)
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

    try:
        get_openai_api_key()

    except ValueError as error:

        print()
        print("❌ CONFIGURATION ERROR")
        print(error)

        return

    print()
    print("=" * 60)
    print("RESEARCH ASSISTANT - FULL PIPELINE")
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

    try:

        search_result = (
            await Runner.run(
                search_agent,
                question,
            )
        ).final_output

    except Exception as error:

        print()
        print("❌ SEARCH AGENT FAILED")
        print(error)

        return

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

    try:

        summary_result = (
            await Runner.run(
                summarizer_agent,
                summary_input,
            )
        ).final_output

    except Exception as error:

        print()
        print("❌ SUMMARIZER AGENT FAILED")
        print(error)

        return

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

    #
    # FACT CHECKER AGENT
    #

    fact_checker_agent = (
        build_fact_checker_agent()
    )

    report_input = f"""
Summary:
{summary_result.summary}

Key Points:
{chr(10).join(summary_result.key_points)}

Confidence Score:
{summary_result.confidence_score}
"""

    try:

        research_report = (
            await Runner.run(
                fact_checker_agent,
                report_input,
            )
        ).final_output

    except Exception as error:

        print()
        print("❌ FACT CHECKER AGENT FAILED")
        print(error)

        return

    print()
    print("RESEARCH REPORT")
    print("=" * 60)

    print()
    print(
        f"Topic: "
        f"{research_report.topic}"
    )

    print()
    print("Executive Summary:")

    print(
        research_report.executive_summary
    )

    print()
    print("Key Findings:")

    for index, finding in enumerate(
        research_report.key_findings,
        start=1,
    ):
        print(
            f"{index}. {finding}"
        )

    print()
    print("Sources Reviewed:")

    for source in (
        research_report.sources_reviewed
    ):
        print(
            f"- {source}"
        )

    print()
    print("Fact Check Notes:")

    print(
        research_report.fact_check_notes
    )

    print()
    print("Final Conclusion:")

    print(
        research_report.final_conclusion
    )

    print()
    print("=" * 60)
    print("PIPELINE COMPLETED")
    print("=" * 60)


if __name__ == "__main__":

    try:

        asyncio.run(main())

    except KeyboardInterrupt:

        print()
        print("⚠️ Execution cancelled by user.")

    except Exception as error:

        print()
        print("💥 UNEXPECTED ERROR")
        print(error)