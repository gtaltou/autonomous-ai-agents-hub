import asyncio

from app.config import (
    get_openai_api_key,
    load_environment,
)
from app.workflow import (
    ResearchWorkflow,
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
    print("RESEARCH WORKFLOW - REAL EXECUTION")
    print("=" * 60)

    question = (
        "What is quantum computing?"
    )

    print()
    print(f"Question: {question}")

    workflow = ResearchWorkflow()

    try:

        report = await workflow.run_real(
            question
        )

    except Exception as error:

        print()
        print("❌ WORKFLOW FAILED")
        print(error)

        return

    print()
    print("RESEARCH REPORT")
    print("=" * 60)

    print()
    print(f"Topic: {report.topic}")

    print()
    print("Executive Summary:")
    print(report.executive_summary)

    print()
    print("Key Findings:")

    for index, finding in enumerate(
        report.key_findings,
        start=1,
    ):
        print(
            f"{index}. {finding}"
        )

    print()
    print("Sources Reviewed:")

    for source in report.sources_reviewed:
        print(
            f"- {source}"
        )

    print()
    print("Fact Check Notes:")
    print(report.fact_check_notes)

    print()
    print("Final Conclusion:")
    print(report.final_conclusion)

    print()
    print("=" * 60)
    print("WORKFLOW COMPLETED")
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