import pytest

from app.analyzers.top_reports import (
    TopReportsAnalyzer,
)
from app.models.report_metadata import (
    ReportMetadata,
)
from app.services.knowledge_service import (
    KnowledgeService,
)


def test_get_top_reports_sorted_by_score():

    reports = [
        ReportMetadata(
            filename="report_a.md",
            topic="A",
            score=75,
            grade="GOOD",
        ),
        ReportMetadata(
            filename="report_b.md",
            topic="B",
            score=95,
            grade="EXCELLENT",
        ),
        ReportMetadata(
            filename="report_c.md",
            topic="C",
            score=85,
            grade="GOOD",
        ),
    ]

    results = (
        TopReportsAnalyzer.get_top_reports(
            reports,
        )
    )

    assert results[0].score == 95
    assert results[1].score == 85
    assert results[2].score == 75


def test_get_top_reports_limit():

    reports = [
        ReportMetadata(
            filename=f"report_{i}.md",
            topic=f"Topic {i}",
            score=i,
            grade="GOOD",
        )
        for i in range(10)
    ]

    results = (
        TopReportsAnalyzer.get_top_reports(
            reports,
            limit=3,
        )
    )

    assert len(results) == 3


def test_get_top_reports_empty_list():

    results = (
        TopReportsAnalyzer.get_top_reports(
            [],
        )
    )

    assert results == []


def test_get_top_reports_large_limit():

    reports = [
        ReportMetadata(
            filename="report.md",
            topic="Fusion Energy",
            score=95,
            grade="EXCELLENT",
        )
    ]

    results = (
        TopReportsAnalyzer.get_top_reports(
            reports,
            limit=10,
        )
    )

    assert len(results) == 1


def test_get_top_reports_limit_zero():

    with pytest.raises(
        ValueError,
        match="limit must be greater than 0",
    ):

        TopReportsAnalyzer.get_top_reports(
            [],
            limit=0,
        )


def test_get_top_reports_negative_limit():

    with pytest.raises(
        ValueError,
        match="limit must be greater than 0",
    ):

        TopReportsAnalyzer.get_top_reports(
            [],
            limit=-5,
        )


def test_get_top_reports_string_limit(
    monkeypatch,
):

    monkeypatch.setattr(
        "app.services.knowledge_service."
        "ReportRepository.list_report_metadata",
        lambda: [],
    )

    with pytest.raises(
        TypeError,
        match="limit must be an integer",
    ):

        KnowledgeService.get_top_reports(
            limit="5",
        )

def test_get_top_reports_float_limit():

    with pytest.raises(
        TypeError,
        match="limit must be an integer",
    ):

        KnowledgeService.get_top_reports(
            
            limit=2.5,
        )