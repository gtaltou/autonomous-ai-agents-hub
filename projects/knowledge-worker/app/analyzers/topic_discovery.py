from collections import Counter

from app.models.report_metadata import (
    ReportMetadata,
)


class TopicDiscoveryAnalyzer:

    @classmethod
    def discover_topics(
        cls,
        reports: list[ReportMetadata],
    ) -> dict[str, int]:

        topics: Counter[str] = Counter()

        for report in reports:

            for word in report.topic.split():

                topics[word.lower()] += 1

        return dict(topics)