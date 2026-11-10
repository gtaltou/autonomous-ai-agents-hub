from app.agents.fact_checker import (
    build_fact_checker_agent,
)
from app.agents.summarizer import (
    build_summarizer_agent,
)


def test_summarizer_agent_name():

    agent = build_summarizer_agent()

    assert agent.name == "Research Summarizer Agent"


def test_fact_checker_agent_name():

    agent = build_fact_checker_agent()

    assert agent.name == "Research Fact Checker Agent"