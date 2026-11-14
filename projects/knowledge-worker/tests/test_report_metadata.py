from app.models.report_metadata import (
    ReportMetadata,
)


def test_report_metadata_model():

    report = ReportMetadata(
        filename="report_001.md",
        topic="Fusion Energy",
        score=95,
        grade="EXCELLENT",
    )

    assert (
        report.filename
        == "report_001.md"
    )

    assert (
        report.topic
        == "Fusion Energy"
    )

    assert (
        report.score
        == 95
    )

    assert (
        report.grade
        == "EXCELLENT"
    )