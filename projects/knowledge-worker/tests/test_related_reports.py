from app.analyzers.related_reports import (
    RelatedReportsAnalyzer,
)
from app.models.report_metadata import (
    ReportMetadata,
)


def test_find_related_reports():

    target = ReportMetadata(
        filename="report_1.md",
        topic="Fusion Energy",
        score=95,
        grade="EXCELLENT",
    )

    reports = [
        target,
        ReportMetadata(
            filename="report_2.md",
            topic="Fusion Energy Research",
            score=85,
            grade="GOOD",
        ),
        ReportMetadata(
            filename="report_3.md",
            topic="History of Science",
            score=75,
            grade="GOOD",
        ),
    ]

    related = (
        RelatedReportsAnalyzer
        .find_related_reports(
            target,
            reports,
        )
    )

    assert len(related) == 1

    assert (
        related[0].topic
        == "Fusion Energy Research"
    )
    
def test_find_related_reports_empty_list():
    
    target = ReportMetadata(
        filename="report.md",
        topic="Fusion Energy",
        score=95,
        grade="EXCELLENT",
    )

    related = (
        RelatedReportsAnalyzer
        .find_related_reports(
            target,
            [],
        )
    )

    assert related == []
    
def test_find_related_reports_excludes_target():
    
    target = ReportMetadata(
        filename="report.md",
        topic="Fusion Energy",
        score=95,
        grade="EXCELLENT",
    )

    related = (
        RelatedReportsAnalyzer
        .find_related_reports(
            target,
            [target],
        )
    )

    assert related == []  