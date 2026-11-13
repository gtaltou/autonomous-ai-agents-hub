import asyncio
import sys

from app.config import (
    load_environment,
)
from app.evaluators.report_evaluator import (
    ReportEvaluator,
)
from app.exporters.markdown_exporter import (
    MarkdownExporter,
)
from app.logging.execution_logger import (
    ExecutionLogger,
)
from app.workflow import (
    ResearchWorkflow,
)


async def main():

    load_environment()

    if len(sys.argv) < 2:

        print(
            "Usage:"
        )

        print(
            'python -m app.main '
            '"Your research question"'
        )

        return

    question = " ".join(
        sys.argv[1:]
    )

    workflow = (
        ResearchWorkflow()
    )

    report = await workflow.run_real(
        question
    )

    filepath = (
        MarkdownExporter.export(
            report
        )
    )

    evaluation = (
        ReportEvaluator.evaluate(
            report
        )
    )

    score = evaluation["score"]

    if score >= 90:
        grade = "EXCELLENT"

    elif score >= 75:
        grade = "GOOD"

    else:
        grade = (
            "NEEDS IMPROVEMENT"
        )

    print()

    print(
        "Topic:"
    )

    print(
        report.topic
    )

    print()

    print(
        "Executive Summary:"
    )

    print(
        report.executive_summary
    )

    print()

    print(
        "REPORT EVALUATION"
    )

    print(
        "-" * 40
    )

    print(
        f"Score: {score}/100"
    )

    print(
        f"Grade: {grade}"
    )

    print()

    print(
        f"Topic Present: "
        f"{'✅' if evaluation['topic_present'] else '❌'}"
    )

    print(
        "Executive Summary Present: "
        f"{'✅' if evaluation['executive_summary_present'] else '❌'}"
    )

    print(
        f"Key Findings Count: "
        f"{evaluation['key_findings_count']}"
    )

    print(
        f"Sources Count: "
        f"{evaluation['sources_count']}"
    )

    print(
        "Fact Check Present: "
        f"{'✅' if evaluation['fact_check_present'] else '❌'}"
    )

    print(
        "Conclusion Present: "
        f"{'✅' if evaluation['conclusion_present'] else '❌'}"
    )

    print()

    ExecutionLogger.success(
        f"Report exported to {filepath}"
    )


if __name__ == "__main__":

    asyncio.run(main())