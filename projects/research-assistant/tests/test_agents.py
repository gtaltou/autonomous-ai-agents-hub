from app.agents.coordinator import (
    build_coordinator_agent,
)
from app.agents.fact_checker import (
    build_fact_checker_agent,
)
from app.agents.search import (
    build_search_agent,
)
from app.agents.summarizer import (
    build_summarizer_agent,
)
from app.models import (
    ResearchReport,
    SearchResult,
)


def test_coordinator_agent_name():

    agent = build_coordinator_agent()

    assert agent.name == "Research Coordinator"


def test_coordinator_output_type():

    agent = build_coordinator_agent()

    assert agent.output_type == ResearchReport


def test_search_agent_name():

    agent = build_search_agent()

    assert agent.name == "Research Search Agent"


def test_search_agent_output_type():

    agent = build_search_agent()

    assert agent.output_type == SearchResult


def test_summarizer_agent_name():

    agent = build_summarizer_agent()

    assert agent.name == "Research Summarizer Agent"


def test_fact_checker_agent_name():

    agent = build_fact_checker_agent()

    assert agent.name == "Research Fact Checker Agent"