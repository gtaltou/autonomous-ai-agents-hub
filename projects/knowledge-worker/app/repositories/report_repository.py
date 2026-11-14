import re
from pathlib import Path

from app.models.report_metadata import (
    ReportMetadata,
)


class ReportRepository:

    REPORTS_DIR = Path(
        "reports"
    )

    @classmethod
    def list_reports(
        cls,
    ) -> list[Path]:

        if not cls.REPORTS_DIR.exists():

            return []

        return sorted(
            cls.REPORTS_DIR.glob(
                "*.md"
            )
        )

    @classmethod
    def read_report(
        cls,
        filepath: Path,
    ) -> str:

        return filepath.read_text(
            encoding="utf-8",
        )

    @classmethod
    def get_metadata(
        cls,
        filepath: Path,
    ) -> ReportMetadata:

        content = cls.read_report(
            filepath
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
            r"Grade:\s*(.+)",
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
            filename=filepath.name,
            topic=topic,
            score=score,
            grade=grade,
        )

    @classmethod
    def list_report_metadata(
        cls,
    ) -> list[ReportMetadata]:

        reports = cls.list_reports()

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
