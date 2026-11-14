from app.analyzers.topic_discovery import (
    TopicDiscoveryAnalyzer,
)
from app.models.report_metadata import (
    ReportMetadata,
)


class RecommendationsAnalyzer:

    @classmethod
    def get_recommendations(
        cls,
        reports: list[ReportMetadata],
        limit: int = 3,
    ) -> list[str]:

        if not isinstance(
            limit,
            int,
        ):
            raise TypeError(
                "limit must be an integer",
            )

        if limit < 1:
            raise ValueError(
                "limit must be greater than 0",
            )

        topics = (
            TopicDiscoveryAnalyzer
            .discover_topics(
                reports,
            )
        )

        sorted_topics = sorted(
            topics.items(),
            key=lambda item: item[1],
            reverse=True,
        )

        return [
            topic
            for topic, _
            in sorted_topics[:limit]
        ]       