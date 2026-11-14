
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
    
def test_compare_reports(
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
        / "report_a.md"
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
        / "report_b.md"
    ).write_text(
        """
## Topic

History

---

Score: 75

Grade: GOOD
""",
        encoding="utf-8",
    )

    report_a, report_b = (
        ReportRepository.compare_reports(
            "report_a.md",
            "report_b.md",
        )
    )

    assert (
        report_a.score == 95
    )

    assert (
        report_b.score == 75
    )
    
    @classmethod
    def get_statistics(
        cls,
    ) -> dict:

        reports = (
            cls.list_report_metadata()
        )

        if not reports:

            return {
                "total_reports": 0,
                "average_score": 0,
                "best_report": None,
                "worst_report": None,
                "grade_distribution": {},
            }

        total_reports = len(
            reports
        )

        average_score = round(
            sum(
                report.score
                for report in reports
            )
            / total_reports,
            1,
        )

        best_report = max(
            reports,
            key=lambda report: report.score,
        )

        worst_report = min(
            reports,
            key=lambda report: report.score,
        )

        grade_distribution = {
            "EXCELLENT": 0,
            "VERY GOOD": 0,
            "GOOD": 0,
            "FAIR": 0,
            "POOR": 0,
        }

        for report in reports:

            grade = report.grade

            if (
                grade
                in grade_distribution
            ):
                grade_distribution[
                    grade
                ] += 1

        return {
            "total_reports": (
                total_reports
            ),
            "average_score": (
                average_score
            ),
            "best_report": (
                best_report
            ),
            "worst_report": (
                worst_report
            ),
            "grade_distribution": (
                grade_distribution
            ),
        }
        
def test_get_statistics(
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
        / "report_a.md"
    ).write_text(
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

    (
        tmp_path
        / "report_b.md"
    ).write_text(
        """
# Research Report

## Topic

History

---

# Evaluation

Score: 75

Grade: GOOD
""",
        encoding="utf-8",
    )

    stats = (
        ReportRepository
        .get_statistics()
    )

    assert (
        stats["total_reports"]
        == 2
    )

    assert (
        stats["average_score"]
        == 85.0
    )

    assert (
        stats["best_report"].score
        == 95
    )

    assert (
        stats["worst_report"].score
        == 75
    )

    assert (
        stats["grade_distribution"][
            "EXCELLENT"
        ]
        == 1
    )

    assert (
        stats["grade_distribution"][
            "GOOD"
        ]
        == 1
    )
    
def test_get_statistics_real_only(
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
        / "report_a.md"
    ).write_text(
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

    (
        tmp_path
        / "report_b.md"
    ).write_text(
        """
# Research Report

## Topic

Test

---

# Evaluation

Score: 50

Grade: NEEDS IMPROVEMENT
""",
        encoding="utf-8",
    )

    stats = (
        ReportRepository
        .get_statistics(
            real_only=True
        )
    )

    assert (
        stats["total_reports"]
        == 1
    )

    assert (
        stats["average_score"]
        == 95.0
    )

    assert (
        stats["best_report"].topic
        == "Fusion Energy"
    )

    assert (
        stats["worst_report"].topic
        == "Fusion Energy"
    )

    assert (
        stats["grade_distribution"][
            "NEEDS IMPROVEMENT"
        ]
        == 0
    )                      