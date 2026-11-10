from agents import Agent


def build_fact_checker_agent() -> Agent:
    """
    Agent responsible for reviewing and
    validating research findings.
    """

    return Agent(
        name="Research Fact Checker Agent",
        instructions="""
        You are responsible for validating
        research findings.

        Review information carefully.

        Look for:

        - inconsistencies
        - unsupported claims
        - missing context
        - factual accuracy

        Highlight potential issues.

        Focus on reliability and evidence.
        """,
    )