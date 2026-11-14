from app.analyzers.top_reports import (
    TopReportsAnalyzer,
)
from app.analyzers.topic_discovery import (
    TopicDiscoveryAnalyzer,
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
        
        