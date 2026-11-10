from app.models import ResearchReport


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