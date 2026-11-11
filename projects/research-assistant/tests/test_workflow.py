from app.models import ResearchReport
from app.workflow import ResearchWorkflow


def test_workflow_creation():

    workflow = ResearchWorkflow()

    assert workflow.coordinator is not None
    assert workflow.search_agent is not None
    assert workflow.summarizer_agent is not None
    assert workflow.fact_checker_agent is not None


def test_workflow_description():

    workflow = ResearchWorkflow()

    description = workflow.describe()

    assert description["coordinator"] == (
        "Research Coordinator"
    )

    assert description["search"] == (
        "Research Search Agent"
    )

    assert description["summarizer"] == (
        "Research Summarizer Agent"
    )

    assert description["fact_checker"] == (
        "Research Fact Checker Agent"
    )


def test_workflow_run():

    workflow = ResearchWorkflow()

    report = workflow.run(
        "What is quantum computing?"
    )

    assert isinstance(
        report,
        ResearchReport,
    )

    assert (
        report.executive_summary
        is not None
    )

    assert len(
        report.key_findings
    ) > 0