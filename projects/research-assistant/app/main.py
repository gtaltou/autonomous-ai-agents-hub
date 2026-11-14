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
from app.history.report_repository import (
    ReportRepository,
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

        print()

        print(
            "Available commands:"
        )

        print(
            "python -m app.main --history"
        )

        print(
            "python -m app.main --latest"
        )

        print(
            "python -m app.main --show <report>"
        )

        print(
            "python -m app.main --search <keyword>"
        )

        return

    #
    # Report History
    #

    if sys.argv[1] == "--history":

        reports = (
            ReportRepository
            .list_report_metadata()
        )

        print()

        print(
            "AVAILABLE REPORTS"
        )

        print()

        if not reports:

            print(
                "No reports found."
            )

            return

        for report in reports:

            print(
                report.topic
            )

            print(
                f"  Score: "
                f"{report.score}"
            )

            print(
                f"  Grade: "
                f"{report.grade}"
            )

            print(
                f"  File: "
                f"{report.filename}"
            )

            print()

        return

    #
    # Latest Report
    #

    if sys.argv[1] == "--latest":

        reports = (
            ReportRepository
            .list_reports()
        )

        if not reports:

            print(
                "No reports found."
            )

            return

        latest_report = reports[0]

        content = (
            ReportRepository.read_report(
                latest_report
            )
        )

        print(content)

        return

    #
    # Show Specific Report
    #

    if sys.argv[1] == "--show":

        if len(sys.argv) < 3:

            print(
                "Usage:"
            )

            print(
                "python -m app.main "
                "--show <report>"
            )

            return

        filename = sys.argv[2]

        content = (
            ReportRepository.read_report(
                filename
            )
        )

        print(content)

        return

    #
    # Search Reports
    #

    if sys.argv[1] == "--search":

        if len(sys.argv) < 3:

            print(
                "Usage:"
            )

            print(
                "python -m app.main "
                "--search <keyword>"
            )

            return

        keyword = sys.argv[2]

        results = (
            ReportRepository.search_reports(
                keyword
            )
        )

        print()

        print(
            "SEARCH RESULTS"
        )

        print()

        if not results:

            print(
                "No matching reports found."
            )

            return

        for report in results:

            print(
                report.topic
            )

            print(
                f"  Score: "
                f"{report.score}"
            )

            print(
                f"  Grade: "
                f"{report.grade}"
            )

            print(
                f"  File: "
                f"{report.filename}"
            )

            print()

        return
    
        #
    # Compare Reports
    #

    if sys.argv[1] == "--compare":

        if len(sys.argv) < 4:

            print(
                "Usage:"
            )

            print(
                "python -m app.main "
                "--compare "
                "<report_a> "
                "<report_b>"
            )

            return

        report_a_filename = (
            sys.argv[2]
        )

        report_b_filename = (
            sys.argv[3]
        )

        (
            report_a,
            report_b,
        ) = (
            ReportRepository
            .compare_reports(
                report_a_filename,
                report_b_filename,
            )
        )

        print()

        print(
            "REPORT COMPARISON"
        )

        print(
            "=" * 40
        )

        print()

        print(
            "REPORT A"
        )

        print(
            "-" * 40
        )

        print(
            f"Topic: "
            f"{report_a.topic}"
        )

        print(
            f"Score: "
            f"{report_a.score}"
        )

        print(
            f"Grade: "
            f"{report_a.grade}"
        )

        print(
            f"File: "
            f"{report_a.filename}"
        )

        print()

        print(
            "REPORT B"
        )

        print(
            "-" * 40
        )

        print(
            f"Topic: "
            f"{report_b.topic}"
        )

        print(
            f"Score: "
            f"{report_b.score}"
        )

        print(
            f"Grade: "
            f"{report_b.grade}"
        )

        print(
            f"File: "
            f"{report_b.filename}"
        )

        print()

        print(
            "-" * 40
        )

        if (
            report_a.score
            > report_b.score
        ):

            winner = report_a

        elif (
            report_b.score
            > report_a.score
        ):

            winner = report_b

        else:

            winner = None

        print()

        print(
            "BEST REPORT"
        )

        print()

        if winner is None:

            print(
                "Tie"
            )

            print(
                f"Score: "
                f"{report_a.score}"
            )

        else:

            print(
                winner.topic
            )

            print(
                f"Score: "
                f"{winner.score}"
            )

            print(
                f"Grade: "
                f"{winner.grade}"
            )

        return
    
    #
    # Research Workflow
    #

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
        f"Overall Score: "
        f"{evaluation['score']}/100"
    )

    print(
        f"Grade: "
        f"{evaluation['grade']}"
    )

    print()

    print(
        f"Completeness Score: "
        f"{evaluation['completeness_score']}/50"
    )

    print(
        f"Content Score: "
        f"{evaluation['content_score']}/30"
    )

    print(
        f"Source Score: "
        f"{evaluation['source_score']}/20"
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