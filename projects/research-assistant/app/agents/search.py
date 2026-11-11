from agents import Agent

from app.models import SearchResult


def build_search_agent() -> Agent:
    """
    Agent responsible for gathering
    information relevant to a topic.
    """

    return Agent(
        name="Research Search Agent",
        instructions="""
        You are a research specialist.

        Analyze the topic provided.

        Produce:

        - a research topic
        - a list of findings
        - the estimated number of sources reviewed

        Always return a SearchResult.
        """,
        output_type=SearchResult,
    )