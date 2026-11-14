import re
from pathlib import Path

from app.models import (
    ReportMetadata,
)


class ReportRepository:

    REPORTS_DIR = Path(
        "reports"
    )

    @classmethod
    def list_reports(
        cls,
    ) -> list[str]:

        if not cls.REPORTS_DIR.exists():

            return []

        return sorted(
            [
                report.name
                for report in cls.REPORTS_DIR.glob(
                    "*.md"
                )
            ],
            reverse=True,
        )

    @classmethod
    def read_report(
        cls,
        filename: str,
    ) -> str:

        filepath = (
            cls.REPORTS_DIR / filename
        )

        if not filepath.exists():

            raise FileNotFoundError(
                f"Report not found: "
                f"{filename}"
            )

        return filepath.read_text(
            encoding="utf-8",
        )

    @classmethod
    def get_metadata(
        cls,
        filename: str,
    ) -> ReportMetadata:

        content = cls.read_report(
            filename
        )

        topic_match = re.search(
            r"## Topic\s+(.+?)\s+---",
            content,
            re.DOTALL,
        )

        score_match = re.search(
            r"(?:Overall )?Score:\s*(\d+)",
            content,
        )

        grade_match = re.search(
            r"Grade:\s*([A-Z ]+)",
            content,
        )

        topic = (
            topic_match.group(1).strip()
            if topic_match
            else "Unknown"
        )

        score = (
            int(score_match.group(1))
            if score_match
            else 0
        )

        grade = (
            grade_match.group(1).strip()
            if grade_match
            else "UNKNOWN"
        )

        return ReportMetadata(
            filename=filename,
            topic=topic,
            score=score,
            grade=grade,
        )

    @classmethod
    def list_report_metadata(
        cls,
    ) -> list[ReportMetadata]:

        reports = (
            cls.list_reports()
        )

        metadata = []

        for report in reports:

            try:

                metadata.append(
                    cls.get_metadata(
                        report
                    )
                )

            except Exception:

                continue

        return metadata
    
    @classmethod
    def search_reports(
        cls,
        keyword: str,
    ) -> list[ReportMetadata]:

        keyword = keyword.lower().strip()

        reports = (
            cls.list_report_metadata()
        )       
    
        results = []

        for report in reports:

            if (
                keyword
                in report.topic.lower()
            ) or (
                keyword
                in report.filename.lower()
            ):

                results.append(
                    report
                )

        return results
    
    @classmethod
    def compare_reports(
        cls,
        first_filename: str,
        second_filename: str,
    ) -> tuple[ReportMetadata, ReportMetadata]:

        first_report = cls.get_metadata(
            first_filename
        )

        second_report = cls.get_metadata(
            second_filename
        )

        return (
            first_report,
            second_report,
        )
        
    @classmethod
    def get_statistics(
        cls,
        real_only: bool = False,
    ) -> dict:

        reports = (
            cls.list_report_metadata()
        )

        if real_only:

            reports = [
                report
                for report in reports
                if report.topic.strip().lower()
                != "test"
            ]

        if not reports:

            return {
                "total_reports": 0,
                "average_score": 0,
                "best_report": None,
                "worst_report": None,
                "grade_distribution": {},
            }

        total_reports = len(
            reports
        )

        average_score = round(
            sum(
                report.score
                for report in reports
            )
            / total_reports,
            1,
        )

        best_report = max(
            reports,
            key=lambda report: report.score,
        )

        worst_report = min(
            reports,
            key=lambda report: report.score,
        )

        grade_distribution = {
            "EXCELLENT": 0,
            "VERY GOOD": 0,
            "GOOD": 0,
            "FAIR": 0,
            "POOR": 0,
            "NEEDS IMPROVEMENT": 0,
        }

        for report in reports:

            if (
                report.grade
                in grade_distribution
            ):

                grade_distribution[
                    report.grade
                ] += 1

        return {
            "total_reports": (
                total_reports
            ),
            "average_score": (
                average_score
            ),
            "best_report": (
                best_report
            ),
            "worst_report": (
                worst_report
            ),
            "grade_distribution": (
                grade_distribution
            ),
        }