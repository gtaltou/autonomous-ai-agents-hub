from app.evaluators.report_evaluator import (
    ReportEvaluator,
)
from app.models import (
    ResearchReport,
)


def test_report_evaluation_excellent():

    report = ResearchReport(
        topic="Quantum Computing",
        executive_summary=(
            "A" * 500
        ),
        key_findings=[
            "Finding 1 " * 20,
            "Finding 2 " * 20,
            "Finding 3 " * 20,
            "Finding 4 " * 20,
            "Finding 5 " * 20,
        ],
        sources_reviewed=[
            "Source 1",
            "Source 2",
            "Source 3",
            "Source 4",
            "Source 5",
        ],
        fact_check_notes=(
            "Validated"
        ),
        final_conclusion=(
            "Conclusion"
        ),
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
        evaluation["grade"]
        == "EXCELLENT"
    )

    assert (
        evaluation[
            "topic_present"
        ]
        is True
    )

    assert (
        evaluation[
            "executive_summary_present"
        ]
        is True
    )

    assert (
        evaluation[
            "fact_check_present"
        ]
        is True
    )

    assert (
        evaluation[
            "conclusion_present"
        ]
        is True
    )


def test_report_evaluation_poor():

    report = ResearchReport(
        topic="",
        executive_summary="",
        key_findings=[],
        sources_reviewed=[],
        fact_check_notes="",
        final_conclusion="",
    )

    evaluation = (
        ReportEvaluator.evaluate(
            report
        )
    )

    assert (
        evaluation["grade"]
        == "POOR"
    )

    assert (
        evaluation["score"]
        == 0
    )


def test_report_evaluation_subscores():

    report = ResearchReport(
        topic="AI",
        executive_summary=(
            "A" * 250
        ),
        key_findings=[
            "Finding A",
            "Finding B",
            "Finding C",
        ],
        sources_reviewed=[
            "Source 1",
            "Source 2",
            "Source 3",
        ],
        fact_check_notes=(
            "Validated"
        ),
        final_conclusion=(
            "Conclusion"
        ),
    )

    evaluation = (
        ReportEvaluator.evaluate(
            report
        )
    )

    assert (
        "completeness_score"
        in evaluation
    )

    assert (
        "content_score"
        in evaluation
    )

    assert (
        "source_score"
        in evaluation
    )

    assert (
        evaluation[
            "sources_count"
        ]
        == 3
    )