from app.models.report_metadata import (
    ReportMetadata,
)


class RelatedReportsAnalyzer:

    @classmethod
    def find_related_reports(
        cls,
        target: ReportMetadata,
        reports: list[ReportMetadata],
    ) -> list[ReportMetadata]:
        target_words = {
            word.lower()
            for word in target.topic.split()
        }

        scored_reports: list[
            tuple[int, ReportMetadata]
        ] = []

        for report in reports:

            if report == target:
                continue

            report_words = {
                word.lower()
                for word in report.topic.split()
            }

            shared_words = (
                target_words
                & report_words
            )

            similarity_score = (
                len(shared_words)
            )

            if similarity_score > 0:

                scored_reports.append(
                    (
                        similarity_score,
                        report,
                    )
                )

        scored_reports.sort(
            key=lambda item: item[0],
            reverse=True,
        )

        return [
            report
            for _, report
            in scored_reports
        ]