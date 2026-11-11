from app.workflow import ResearchWorkflow


def test_workflow_creation():

    workflow = ResearchWorkflow()

    assert workflow.coordinator is not None
    assert workflow.search is not None
    assert workflow.summarizer is not None
    assert workflow.fact_checker is not None


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