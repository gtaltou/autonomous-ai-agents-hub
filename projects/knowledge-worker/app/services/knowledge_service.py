from app.analyzers.recommendations import (
    RecommendationsAnalyzer,
)
from app.analyzers.related_reports import (
    RelatedReportsAnalyzer,
)
from app.analyzers.top_reports import (
    TopReportsAnalyzer,
)
from app.analyzers.top_topics import (
    TopTopicsAnalyzer,
)
from app.analyzers.topic_discovery import (
    TopicDiscoveryAnalyzer,
)
from app.models.report_metadata import (
    ReportMetadata,
)
from app.repositories.report_repository import (
    ReportRepository,
)


class KnowledgeService:

    @classmethod
    def get_top_reports(
        cls,
        limit: int = 5,
    ):

        reports = (
            ReportRepository
            .list_report_metadata()
        )

        return (
            TopReportsAnalyzer
            .get_top_reports(
                reports,
                limit,
            )
        )

    @classmethod
    def get_topics(
        cls,
    ) -> dict[str, int]:

        reports = (
            ReportRepository
            .list_report_metadata()
        )

        return (
            TopicDiscoveryAnalyzer
            .discover_topics(
                reports,
            )
        )

    @classmethod
    def get_related_reports(
        cls,
        target: ReportMetadata,
    ) -> list[ReportMetadata]:

        reports = (
            ReportRepository
            .list_report_metadata()
        )

        return (
            RelatedReportsAnalyzer
            .find_related_reports(
                target,
                reports,
            )
        )

    @classmethod
    def get_recommendations(
        cls,
        limit: int = 3,
    ) -> list[str]:

        reports = (
            ReportRepository
            .list_report_metadata()
        )

        return (
            RecommendationsAnalyzer
            .get_recommendations(
                reports,
                limit=limit,
            )
        )

    @classmethod
    def get_top_topics(
        cls,
        limit: int = 10,
    ) -> list[tuple[str, int]]:

        topics = (
            cls.get_topics()
        )

        return (
            TopTopicsAnalyzer
            .get_top_topics(
                topics,
                limit,
            )
        )