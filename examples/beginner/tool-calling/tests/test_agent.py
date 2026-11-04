from app.agent import build_agent


def test_agent_name():

    agent = build_agent()

    assert agent.name == "Tool Calling Agent"


def test_agent_has_tools():

    agent = build_agent()

    assert len(agent.tools) == 1