from datetime import datetime
from pathlib import Path

from app.models import (
    ResearchReport,
)


class MarkdownExporter:

    @staticmethod
    def export(
        report: ResearchReport,
    ) -> Path:

        reports_dir = Path(
            "reports"
        )

        reports_dir.mkdir(
            exist_ok=True
        )

        timestamp = (
            datetime.now()
            .strftime(
                "%Y-%m-%d_%H%M%S"
            )
        )

        filename = (
            f"report_{timestamp}.md"
        )

        filepath = (
            reports_dir / filename
        )

        content = f"""# Research Report

## Topic

{report.topic}

---

## Executive Summary

{report.executive_summary}

---

## Key Findings

"""

        for finding in (
            report.key_findings
        ):
            content += (
                f"- {finding}\n"
            )

        content += """

---

## Sources Reviewed

"""

        for source in (
            report.sources_reviewed
        ):
            content += (
                f"- {source}\n"
            )

        content += f"""

---

## Fact Check Notes

{report.fact_check_notes}

---

## Final Conclusion

{report.final_conclusion}
"""

        filepath.write_text(
            content,
            encoding="utf-8",
        )

        return filepath