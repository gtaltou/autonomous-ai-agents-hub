from app.models import (
    ResearchReport,
)


class ReportEvaluator:

    @staticmethod
    def evaluate(
        report: ResearchReport,
    ) -> dict:

        #
        # Completeness Score (50)
        #

        completeness_score = 0

        topic_present = bool(
            report.topic.strip()
        )

        if topic_present:
            completeness_score += 10

        executive_summary_present = bool(
            report.executive_summary.strip()
        )

        if executive_summary_present:
            completeness_score += 10

        fact_check_present = bool(
            report.fact_check_notes.strip()
        )

        if fact_check_present:
            completeness_score += 10

        conclusion_present = bool(
            report.final_conclusion.strip()
        )

        if conclusion_present:
            completeness_score += 10

        key_findings_count = len(
            report.key_findings
        )

        if key_findings_count >= 5:
            completeness_score += 10

        elif key_findings_count >= 3:
            completeness_score += 5

        #
        # Content Score (30)
        #

        content_score = 0

        summary_length = len(
            report.executive_summary
        )

        if summary_length >= 400:
            content_score += 15

        elif summary_length >= 200:
            content_score += 10

        elif summary_length >= 100:
            content_score += 5

        findings_text_length = sum(
            len(finding)
            for finding in report.key_findings
        )

        if findings_text_length >= 500:
            content_score += 15

        elif findings_text_length >= 250:
            content_score += 10

        elif findings_text_length >= 100:
            content_score += 5

        #
        # Source Score (20)
        #

        sources_count = len(
            report.sources_reviewed
        )

        if sources_count >= 5:
            source_score = 20

        elif sources_count >= 3:
            source_score = 15

        elif sources_count > 0:
            source_score = 10

        else:
            source_score = 0

        #
        # Overall Score
        #

        overall_score = min(
            completeness_score
            + content_score
            + source_score,
            100,
        )

        #
        # Grade
        #

        if overall_score >= 95:
            grade = "EXCELLENT"

        elif overall_score >= 85:
            grade = "VERY GOOD"

        elif overall_score >= 70:
            grade = "GOOD"

        elif overall_score >= 50:
            grade = "FAIR"

        else:
            grade = "POOR"

        return {
            "score": overall_score,
            "grade": grade,
            "completeness_score": (
                completeness_score
            ),
            "content_score": (
                content_score
            ),
            "source_score": (
                source_score
            ),
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