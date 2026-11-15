import sys

from app.repositories.report_repository import (
    ReportRepository,
)
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


def show_topics() -> None:

    topics = (
        KnowledgeService
        .get_topics()
    )

    print()
    print("TOPICS")
    print("=" * 40)
    print()

    if not topics:

        print(
            "No topics found."
        )

        return

    for topic, count in sorted(
        topics.items(),
        key=lambda item: item[1],
        reverse=True,
    ):

        print(
            f"{topic}: {count}"
        )


def show_recommendations(
    limit: int = 3,
) -> None:

    recommendations = (
        KnowledgeService
        .get_recommendations(
            limit=limit,
        )
    )

    print()
    print("RECOMMENDATIONS")
    print("=" * 40)
    print()

    if not recommendations:

        print(
            "No recommendations found."
        )

        return

    for recommendation in recommendations:

        print(
            recommendation
        )


def show_top_topics() -> None:

    topics = (
        KnowledgeService
        .get_top_topics()
    )

    print()
    print("TOP TOPICS")
    print("=" * 40)
    print()

    if not topics:

        print(
            "No topics found."
        )

        return

    for index, (
        topic,
        count,
    ) in enumerate(
        topics,
        start=1,
    ):

        print(
            f"{index}. {topic} ({count})"
        )


def show_related_reports(
    topic: str,
) -> None:

    reports = (
        ReportRepository
        .list_report_metadata()
    )

    target = next(
        (
            report
            for report in reports
            if report.topic.lower()
            == topic.lower()
        ),
        None,
    )

    if target is None:

        print(
            "Topic not found."
        )

        return

    related_reports = (
        KnowledgeService
        .get_related_reports(
            target,
        )
    )

    print()
    print("RELATED REPORTS")
    print("=" * 40)
    print()

    if not related_reports:

        print(
            "No related reports found."
        )

        return

    for index, report in enumerate(
        related_reports,
        start=1,
    ):

        print(
            f"{index}. {report.topic}"
        )

        print()


def main(
    args=None,
) -> None:

    if args is None:

        args = sys.argv[1:]

    if not args:

        print("Usage:")

        print(
            "python -m app.main --top-reports"
        )

        print(
            "python -m app.main --topics"
        )

        print(
            "python -m app.main --top-topics"
        )

        print(
            "python -m app.main --recommendations [limit]"
        )

        print(
            'python -m app.main --related "topic"'
        )

        return

    if "--top-reports" in args:

        show_top_reports()

        return

    if "--topics" in args:

        show_topics()

        return

    if "--top-topics" in args:

        show_top_topics()

        return

    if "--related" in args:

        related_index = (
            args.index(
                "--related"
            )
        )

        if (
            related_index + 1
            >= len(args)
        ):

            print(
                "Missing topic."
            )

            return

        topic = args[
            related_index + 1
        ]

        show_related_reports(
            topic,
        )

        return

    if "--recommendations" in args:

        limit = 3

        if len(args) > 1:

            try:

                limit = int(
                    args[1]
                )

            except ValueError:

                print(
                    "Invalid limit."
                )

                return

        show_recommendations(
            limit=limit,
        )

        return

    print(
        "Unknown command."
    )


if __name__ == "__main__":

    main()