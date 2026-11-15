import json
import sys

from app.repositories.report_repository import (
    ReportRepository,
)
from app.services.knowledge_service import (
    KnowledgeService,
)


def show_top_reports(
    as_json: bool = False,
) -> None:

    reports = (
        KnowledgeService
        .get_top_reports()
    )

    if as_json:

        print(
            json.dumps(
                [
                    {
                        "topic": report.topic,
                        "score": report.score,
                        "grade": report.grade,
                    }
                    for report in reports
                ],
                indent=4,
            )
        )

        return

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


def show_topics(
    as_json: bool = False,
) -> None:

    topics = (
        KnowledgeService
        .get_topics()
    )

    if as_json:

        print(
            json.dumps(
                topics,
                indent=4,
            )
        )

        return

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
    as_json: bool = False,
) -> None:

    recommendations = (
        KnowledgeService
        .get_recommendations(
            limit=limit,
        )
    )

    if as_json:

        print(
            json.dumps(
                recommendations,
                indent=4,
            )
        )

        return

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


def show_top_topics(
    as_json: bool = False,
) -> None:

    topics = (
        KnowledgeService
        .get_top_topics()
    )

    if as_json:

        print(
            json.dumps(
                [
                    {
                        "topic": topic,
                        "count": count,
                    }
                    for topic, count in topics
                ],
                indent=4,
            )
        )

        return

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
    as_json: bool = False,
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

    if as_json:

        print(
            json.dumps(
                [
                    {
                        "topic": report.topic,
                        "score": report.score,
                        "grade": report.grade,
                    }
                    for report in related_reports
                ],
                indent=4,
            )
        )

        return

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

    as_json = (
        "--json"
        in args
    )

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
        print(
            "python -m app.main [command] --json"
        )

        return

    if "--top-reports" in args:

        show_top_reports(
            as_json=as_json,
        )

        return

    if "--topics" in args:

        show_topics(
            as_json=as_json,
        )

        return

    if "--top-topics" in args:

        show_top_topics(
            as_json=as_json,
        )

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
            as_json=as_json,
        )

        return

    if "--recommendations" in args:

        limit = 3

        recommendation_index = (
            args.index(
                "--recommendations"
            )
        )

        if (
            recommendation_index + 1
            < len(args)
            and args[
                recommendation_index + 1
            ] != "--json"
        ):

            try:

                limit = int(
                    args[
                        recommendation_index
                        + 1
                    ]
                )

            except ValueError:

                print(
                    "Invalid limit."
                )

                return

        show_recommendations(
            limit=limit,
            as_json=as_json,
        )

        return

    print(
        "Unknown command."
    )


if __name__ == "__main__":

    main()