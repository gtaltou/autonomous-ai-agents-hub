from agents import Agent

from app.models import SearchResult


def build_search_agent() -> Agent:

    return Agent(
        name="Research Search Agent",
        instructions="""
You are a research specialist.

Analyze the requested topic.

Return a valid SearchResult.

Rules:

- topic must contain the main subject.
- findings must contain between 3 and 5 findings.
- source_count must be greater than 0.
- source_count should match the estimated number of sources used.

Never return empty findings.
""",
        output_type=SearchResult,
    )