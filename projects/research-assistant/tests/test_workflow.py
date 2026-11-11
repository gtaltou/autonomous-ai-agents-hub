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


def test_workflow_run():
    
    workflow = ResearchWorkflow()

    result = workflow.run(
        "What is quantum computing?"
    )

    assert result["question"] == (
        "What is quantum computing?"
    )

    assert "search_stage" in result

    assert "summary_stage" in result

    assert "fact_check_stage" in result