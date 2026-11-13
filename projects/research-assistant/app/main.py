import asyncio
import sys

from app.config import (
    load_environment,
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

    ExecutionLogger.success(
        f"Report exported to {filepath}"
    )


if __name__ == "__main__":

    asyncio.run(main())
