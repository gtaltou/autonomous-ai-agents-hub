from app.evaluators.report_evaluator import (
    ReportEvaluator,
)
from app.models import (
    ResearchReport,
)


def test_report_evaluation():

    report = ResearchReport(
        topic="Quantum Computing",
        executive_summary="Summary",
        key_findings=[
            "A",
            "B",
            "C",
            "D",
            "E",
        ],
        sources_reviewed=[
            "Source 1",
            "Source 2",
            "Source 3",
        ],
        fact_check_notes="Validated",
        final_conclusion="Conclusion",
    )

    evaluation = (
        ReportEvaluator.evaluate(
            report
        )
    )

    assert (
        evaluation["score"]
        == 100
    )

    assert (
        evaluation[
            "topic_present"
        ]
        is True
    )