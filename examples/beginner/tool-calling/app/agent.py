from agents import Agent
from tools import calculator


def build_agent() -> Agent:

    return Agent(
        name="Tool Calling Agent",
        instructions="""
        You are a helpful AI assistant.

        For any mathematical operation,
        always use the calculator tool.
        """,
        tools=[
            calculator,
        ],
    )