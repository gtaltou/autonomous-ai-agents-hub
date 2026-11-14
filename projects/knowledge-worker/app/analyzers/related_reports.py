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

        related = []

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

            if shared_words:

                related.append(
                    report
                )

        return related
