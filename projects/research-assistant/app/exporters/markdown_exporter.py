from datetime import datetime
from pathlib import Path

from app.evaluators.report_evaluator import (
    ReportEvaluator,
)
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

        for finding in report.key_findings:
            content += (
                f"- {finding}\n"
            )

        content += """

---

## Sources Reviewed

"""

        for source in report.sources_reviewed:
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

        evaluation = (
            ReportEvaluator.evaluate(
                report
            )
        )

        score = (
            evaluation["score"]
        )

        if score >= 90:
            grade = "EXCELLENT"

        elif score >= 75:
            grade = "GOOD"

        else:
            grade = (
                "NEEDS IMPROVEMENT"
            )

        content += f"""

---

# Evaluation

Score: {score}/100

Grade: {grade}

## Validation Checklist

- Topic Present: {"✅" if evaluation["topic_present"] else "❌"}
- Executive Summary Present: {"✅" if evaluation["executive_summary_present"] else "❌"}
- Key Findings Count: {evaluation["key_findings_count"]}
- Sources Count: {evaluation["sources_count"]}
- Fact Check Present: {"✅" if evaluation["fact_check_present"] else "❌"}
- Conclusion Present: {"✅" if evaluation["conclusion_present"] else "❌"}
"""

        filepath.write_text(
            content,
            encoding="utf-8",
        )

        return filepath