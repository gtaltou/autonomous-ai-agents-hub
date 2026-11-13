from app.models import (
    ResearchReport,
)


class ReportEvaluator:

    @staticmethod
    def evaluate(
        report: ResearchReport,
    ) -> dict:

        score = 0

        topic_present = bool(
            report.topic.strip()
        )

        if topic_present:
            score += 15

        executive_summary_present = bool(
            report.executive_summary.strip()
        )

        if executive_summary_present:
            score += 15

        key_findings_count = len(
            report.key_findings
        )

        if key_findings_count >= 5:
            score += 25

        elif key_findings_count >= 3:
            score += 15

        elif key_findings_count > 0:
            score += 5

        sources_count = len(
            report.sources_reviewed
        )

        if sources_count >= 3:
            score += 20

        elif sources_count > 0:
            score += 10

        fact_check_present = bool(
            report.fact_check_notes.strip()
        )

        if fact_check_present:
            score += 15

        conclusion_present = bool(
            report.final_conclusion.strip()
        )

        if conclusion_present:
            score += 10

        score = min(
            score,
            100,
        )

        return {
            "score": score,
            "topic_present": (
                topic_present
            ),
            "executive_summary_present": (
                executive_summary_present
            ),
            "key_findings_count": (
                key_findings_count
            ),
            "sources_count": (
                sources_count
            ),
            "fact_check_present": (
                fact_check_present
            ),
            "conclusion_present": (
                conclusion_present
            ),
        }