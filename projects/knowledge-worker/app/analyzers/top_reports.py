from app.models.report_metadata import (
    ReportMetadata,
)


from app.models.report_metadata import (
    ReportMetadata,
)


class TopReportsAnalyzer:

    @classmethod
    def get_top_reports(
        cls,
        reports: list[ReportMetadata],
        limit: int = 5,
    ) -> list[ReportMetadata]:

        if not isinstance(limit, int):

            raise TypeError(
                "limit must be an integer"
            )

        if limit < 1:

            raise ValueError(
                "limit must be greater than 0"
            )

        sorted_reports = sorted(
            reports,
            key=lambda report: report.score,
            reverse=True,
        )

        return sorted_reports[:limit]