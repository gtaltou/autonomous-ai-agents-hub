from app.models import (
    ResearchReport,
    SearchResult,
    SummaryResult,
)


def test_search_result_model():

    result = SearchResult(
        topic="Quantum Computing",
        findings=[
            "Finding 1",
            "Finding 2",
        ],
        source_count=2,
    )

    assert result.topic == "Quantum Computing"
    assert len(result.findings) == 2
    assert result.source_count == 2


def test_summary_result_model():

    result = SummaryResult(
        summary="Quantum computing summary",
        key_points=[
            "Point 1",
            "Point 2",
        ],
        confidence_score=0.90,
    )

    assert result.summary == (
        "Quantum computing summary"
    )

    assert len(result.key_points) == 2

    assert result.confidence_score == 0.90


def test_research_report_model():

    report = ResearchReport(
        topic="Quantum Computing",
        executive_summary="Summary",
        key_findings=[
            "Finding 1",
            "Finding 2",
        ],
        sources_reviewed=[
            "IBM Quantum",
            "Google Quantum AI",
        ],
        fact_check_notes="Reviewed",
        final_conclusion="Promising",
    )

    assert report.topic == "Quantum Computing"
    assert len(report.key_findings) == 2
    assert len(report.sources_reviewed) == 2
