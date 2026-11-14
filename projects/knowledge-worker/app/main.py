import sys

from app.services.knowledge_service import (
    KnowledgeService,
)


def show_top_reports() -> None:

    reports = (
        KnowledgeService
        .get_top_reports()
    )

    print()
    print("TOP REPORTS")
    print("=" * 40)
    print()

    if not reports:

        print(
            "No reports found."
        )

        return

    for index, report in enumerate(
        reports,
        start=1,
    ):

        print(
            f"{index}. {report.topic}"
        )

        print(
            f"   Score: {report.score}"
        )

        print(
            f"   Grade: {report.grade}"
        )

        print()


def main() -> None:

    if (
        len(sys.argv) > 1
        and sys.argv[1]
        == "--top-reports"
    ):

        show_top_reports()

        return

    print(
        "Usage:"
    )

    print(
        "python -m app.main --top-reports"
    )


if __name__ == "__main__":

    main()