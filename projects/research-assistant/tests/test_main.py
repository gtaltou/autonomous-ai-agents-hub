from unittest.mock import AsyncMock
from unittest.mock import Mock
from unittest.mock import patch

import pytest

from app.main import main


@pytest.mark.anyio
@patch("app.main.load_environment")
async def test_main_without_arguments(
    mock_load_environment,
    monkeypatch,
    capsys,
):

    monkeypatch.setattr(
        "sys.argv",
        ["main.py"],
    )

    await main()

    captured = capsys.readouterr()

    assert "Usage:" in captured.out


@pytest.mark.anyio
@patch("app.main.MarkdownExporter.export")
@patch("app.main.ReportEvaluator.evaluate")
@patch("app.main.ResearchWorkflow")
@patch("app.main.load_environment")
async def test_main_success(
    mock_load_environment,
    mock_workflow,
    mock_evaluator,
    mock_exporter,
    monkeypatch,
    capsys,
):

    monkeypatch.setattr(
        "sys.argv",
        [
            "main.py",
            "What",
            "is",
            "fusion",
            "energy?",
        ],
    )

    report = Mock()

    report.topic = (
        "Fusion Energy"
    )

    report.executive_summary = (
        "Summary"
    )

    workflow_instance = Mock()

    workflow_instance.run_real = (
        AsyncMock(
            return_value=report,
        )
    )

    mock_workflow.return_value = (
        workflow_instance
    )

    mock_exporter.return_value = (
        "reports/test.md"
    )

    mock_evaluator.return_value = {
        "score": 100,
        "topic_present": True,
        "executive_summary_present": True,
        "key_findings_count": 6,
        "sources_count": 5,
        "fact_check_present": True,
        "conclusion_present": True,
    }

    await main()

    captured = capsys.readouterr()

    assert (
        "Fusion Energy"
        in captured.out
    )

    assert (
        "REPORT EVALUATION"
        in captured.out
    )

    assert (
        "Score: 100/100"
        in captured.out
    )

    workflow_instance.run_real.assert_awaited_once()