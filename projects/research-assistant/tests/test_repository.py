from pathlib import Path

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