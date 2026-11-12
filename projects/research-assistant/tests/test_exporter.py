from app.exporters.markdown_exporter import (
    MarkdownExporter,
)
from app.models import (
    ResearchReport,
)


def test_markdown_export():

    report = ResearchReport(
        topic="Test",
        executive_summary="Summary",
        key_findings=["A", "B"],
        sources_reviewed=["Source"],
        fact_check_notes="Notes",
        final_conclusion="Conclusion",
    )

    filepath = (
        MarkdownExporter.export(
            report
        )
    )

    assert filepath.exists()

    content = filepath.read_text(
        encoding="utf-8"
    )

    assert "Test" in content