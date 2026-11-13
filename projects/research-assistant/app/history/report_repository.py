from pathlib import Path


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