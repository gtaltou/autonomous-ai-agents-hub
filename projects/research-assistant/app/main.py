import asyncio
import logging

from agents import Runner

from app.agents.coordinator import (
    build_coordinator_agent,
)
from app.config import (
    get_openai_api_key,
    load_environment,
)
from app.models import ResearchReport
from app.workflow import (
    ResearchWorkflow,
)

logger = logging.getLogger(__name__)

QUESTION = """
What are the main benefits of quantum computing?
"""


async def run_research() -> ResearchReport:

    load_environment()

    get_openai_api_key()

    agent = build_coordinator_agent()

    result = await Runner.run(
        agent,
        QUESTION,
    )

    return result.final_output


async def main():

    logger.info(
        "Starting Research Assistant"
    )

    report = await run_research()

    print()
    print("🔍 Research Question:")
    print(QUESTION.strip())

    print()
    print("📄 Research Report")
    print("=" * 50)

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
        print(f"- {source}")

    print()
    print("Fact Check Notes:")
    print(report.fact_check_notes)

    print()
    print("Final Conclusion:")
    print(report.final_conclusion)

    logger.info(
        "Research completed"
    )


if __name__ == "__main__":
    asyncio.run(main())
    
workflow = ResearchWorkflow()

pipeline = workflow.run(
    QUESTION
)

print()
print("Workflow:")
print(pipeline)    