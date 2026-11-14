from app.analyzers.top_reports import (
    TopReportsAnalyzer,
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
    ) -> list[ReportMetadata]:

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