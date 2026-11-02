from agents import Agent


def build_agent() -> Agent:
    """
    Build the Hello Agent.
    """

    return Agent(
        name="Hello Agent",
        instructions="""
        You are a helpful AI assistant.

        Answer clearly.
        Answer concisely.
        Use simple explanations.
        """
    )