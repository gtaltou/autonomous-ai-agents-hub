from app.workflow import (
    ResearchWorkflow,
)


def test_workflow_creation():

    workflow = ResearchWorkflow()

    assert workflow.coordinator is not None
    assert workflow.search is not None
    assert workflow.summarizer is not None
    assert workflow.fact_checker is not None