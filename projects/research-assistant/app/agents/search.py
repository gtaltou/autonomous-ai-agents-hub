from agents import Agent


def build_search_agent() -> Agent:
    """
    Agent responsible for gathering
    information relevant to a topic.
    """

    return Agent(
        name="Research Search Agent",
        instructions="""
        You are a research specialist.

        Analyze the requested topic.

        Identify the most relevant information.

        Focus on:
        - key concepts
        - important facts
        - major trends
        - useful references

        Return concise and relevant findings.
        """,
    )