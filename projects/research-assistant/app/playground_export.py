import asyncio

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

    workflow = (
        ResearchWorkflow()
    )

    report = await workflow.run_real(
        "What is quantum computing?"
    )

    filepath = (
        MarkdownExporter.export(
            report
        )
    )

    ExecutionLogger.success(
        f"Report exported to {filepath}"
    )


if __name__ == "__main__":
    asyncio.run(main())