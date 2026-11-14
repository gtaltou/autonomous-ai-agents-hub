
import pytest

from app.history.report_repository import (
    ReportRepository,
)


def test_list_reports_empty(
    tmp_path,
    monkeypatch,
):

    monkeypatch.setattr(
        ReportRepository,
        "REPORTS_DIR",
        tmp_path,
    )

    reports = (
        ReportRepository
        .list_reports()
    )

    assert reports == []


def test_list_reports(
    tmp_path,
    monkeypatch,
):

    monkeypatch.setattr(
        ReportRepository,
        "REPORTS_DIR",
        tmp_path,
    )

    (
        tmp_path
        / "report_1.md"
    ).write_text(
        "content",
        encoding="utf-8",
    )

    (
        tmp_path
        / "report_2.md"
    ).write_text(
        "content",
        encoding="utf-8",
    )

    reports = (
        ReportRepository
        .list_reports()
    )

    assert len(reports) == 2

    assert (
        "report_1.md"
        in reports
    )

    assert (
        "report_2.md"
        in reports
    )


def test_read_report(
    tmp_path,
    monkeypatch,
):

    monkeypatch.setattr(
        ReportRepository,
        "REPORTS_DIR",
        tmp_path,
    )

    report = (
        tmp_path
        / "report.md"
    )

    report.write_text(
        "Hello Report",
        encoding="utf-8",
    )

    content = (
        ReportRepository
        .read_report(
            "report.md"
        )
    )

    assert (
        content
        == "Hello Report"
    )


def test_read_report_not_found(
    tmp_path,
    monkeypatch,
):

    monkeypatch.setattr(
        ReportRepository,
        "REPORTS_DIR",
        tmp_path,
    )

    with pytest.raises(
        FileNotFoundError
    ):

        ReportRepository.read_report(
            "missing.md"
        )
        
def test_search_reports(
    tmp_path,
    monkeypatch,
):

    monkeypatch.setattr(
        ReportRepository,
        "REPORTS_DIR",
        tmp_path,
    )

    report = (
        tmp_path
        / "fusion_report.md"
    )

    report.write_text(
        """
# Research Report

## Topic

Fusion Energy

---

# Evaluation

Score: 95

Grade: EXCELLENT
""",
        encoding="utf-8",
    )

    results = (
        ReportRepository
        .search_reports(
            "fusion"
        )
    )

    assert len(results) == 1

    assert (
        results[0].topic
        == "Fusion Energy"
    )        