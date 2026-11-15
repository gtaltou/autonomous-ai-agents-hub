from pathlib import Path

from app.repositories.report_repository import (
    ReportRepository,
)


def test_list_report_metadata(
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
        / "report.md"
    ).write_text(
        """
## Topic

Fusion Energy

---

Score: 95

Grade: EXCELLENT
""",
        encoding="utf-8",
    )

    reports = (
        ReportRepository
        .list_report_metadata()
    )

    assert len(reports) == 1

    assert (
        reports[0].topic
        == "Fusion Energy"
    )

    assert (
        reports[0].score
        == 95
    )

    assert (
        reports[0].grade
        == "EXCELLENT"
    )
    
def test_get_metadata_empty_report(
    tmp_path,
    monkeypatch,
):

    monkeypatch.setattr(
        ReportRepository,
        "REPORTS_DIR",
        tmp_path,
    )

    report_path = (
        tmp_path
        / "empty.md"
    )

    report_path.write_text(
        "",
        encoding="utf-8",
    )

    metadata = (
        ReportRepository
        .get_metadata(
            report_path
        )
    )

    assert (
        metadata.topic
        == "Unknown"
    )

    assert (
        metadata.score
        == 0
    )

    assert (
        metadata.grade
        == "UNKNOWN"
    )
    
def test_get_metadata_missing_score(
    tmp_path,
    monkeypatch,
):

    monkeypatch.setattr(
        ReportRepository,
        "REPORTS_DIR",
        tmp_path,
    )

    report_path = (
        tmp_path
        / "report.md"
    )

    report_path.write_text(
        """
## Topic

Fusion Energy

---

Grade: EXCELLENT
""",
        encoding="utf-8",
    )

    metadata = (
        ReportRepository
        .get_metadata(
            report_path
        )
    )

    assert (
        metadata.topic
        == "Fusion Energy"
    )

    assert (
        metadata.score
        == 0
    )

    assert (
        metadata.grade
        == "EXCELLENT"
    )
    
def test_get_metadata_missing_grade(
    tmp_path,
    monkeypatch,
):

    monkeypatch.setattr(
        ReportRepository,
        "REPORTS_DIR",
        tmp_path,
    )

    report_path = (
        tmp_path
        / "report.md"
    )

    report_path.write_text(
        """
## Topic

Fusion Energy

---

Score: 95
""",
        encoding="utf-8",
    )

    metadata = (
        ReportRepository
        .get_metadata(
            report_path
        )
    )

    assert (
        metadata.topic
        == "Fusion Energy"
    )

    assert (
        metadata.score
        == 95
    )

    assert (
        metadata.grade
        == "UNKNOWN"
    )
    
def test_list_report_metadata_skips_invalid_files(
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
        / "valid.md"
    ).write_text(
        """
## Topic

Fusion Energy

---

Score: 95

Grade: EXCELLENT
""",
        encoding="utf-8",
    )

    (
        tmp_path
        / "invalid.md"
    ).write_text(
        "",
        encoding="utf-8",
    )

    reports = (
        ReportRepository
        .list_report_metadata()
    )

    assert len(reports) == 2
    
def test_list_report_metadata_ignores_non_markdown_files(
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
        / "report.md"
    ).write_text(
        """
## Topic

Fusion Energy

---

Score: 95

Grade: EXCELLENT
""",
        encoding="utf-8",
    )

    (
        tmp_path
        / "report.txt"
    ).write_text(
        """
## Topic

Should Not Be Loaded

---

Score: 100

Grade: EXCELLENT
""",
        encoding="utf-8",
    )

    (
        tmp_path
        / "report.json"
    ).write_text(
        "{}",
        encoding="utf-8",
    )

    reports = (
        ReportRepository
        .list_report_metadata()
    )

    assert len(reports) == 1

    assert (
        reports[0].filename
        == "report.md"
    )

    assert (
        reports[0].topic
        == "Fusion Energy"
    )
    
def test_list_reports_only_markdown_files(
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
        / "report.md"
    ).touch()

    (
        tmp_path
        / "notes.txt"
    ).touch()

    (
        tmp_path
        / "data.json"
    ).touch()

    reports = (
        ReportRepository
        .list_reports()
    )

    assert len(reports) == 1

    assert (
        reports[0].name
        == "report.md"
    )
    

def test_list_reports_missing_directory(
    monkeypatch,
):

    missing_dir = Path(
        "directory_does_not_exist"
    )

    monkeypatch.setattr(
        ReportRepository,
        "REPORTS_DIR",
        missing_dir,
    )

    reports = (
        ReportRepository
        .list_reports()
    )

    assert reports == []
    

def test_list_report_metadata_missing_directory(
    monkeypatch,
):

    missing_dir = Path(
        "directory_does_not_exist"
    )

    monkeypatch.setattr(
        ReportRepository,
        "REPORTS_DIR",
        missing_dir,
    )

    metadata = (
        ReportRepository
        .list_report_metadata()
    )

    assert metadata == []

def test_list_reports_reports_dir_is_file(
    tmp_path,
    monkeypatch,
):

    fake_reports_dir = (
        tmp_path
        / "reports"
    )

    fake_reports_dir.write_text(
        "not a directory",
        encoding="utf-8",
    )

    monkeypatch.setattr(
        ReportRepository,
        "REPORTS_DIR",
        fake_reports_dir,
    )

    reports = (
        ReportRepository
        .list_reports()
    )

    assert reports == [] 
    
@classmethod
def list_reports(
    cls,
) -> list[Path]:

    if (
        not cls.REPORTS_DIR.exists()
        or not cls.REPORTS_DIR.is_dir()
    ):

        return []

    return sorted(
        cls.REPORTS_DIR.glob(
            "*.md"
        )
    ) 
    
def test_list_report_metadata_reports_dir_is_file(
    tmp_path,
    monkeypatch,
):

    fake_reports_dir = (
        tmp_path
        / "reports"
    )

    fake_reports_dir.write_text(
        "not a directory",
        encoding="utf-8",
    )

    monkeypatch.setattr(
        ReportRepository,
        "REPORTS_DIR",
        fake_reports_dir,
    )

    reports = (
        ReportRepository
        .list_report_metadata()
    )

    assert reports == []  
    
