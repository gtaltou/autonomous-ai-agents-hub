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

                word = word.lower()

                if word in STOP_WORDS:
                    continue

                topics[word] += 1

        return dict(topics)
    

STOP_WORDS = {
    "a",
    "an",
    "and",
    "of",
    "in",
    "on",
    "the",
    "to",
}  