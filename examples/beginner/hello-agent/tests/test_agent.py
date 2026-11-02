from app.agent import build_agent


def test_agent_name():

    agent = build_agent()

    assert agent.name == "Hello Agent"


def test_agent_instructions_exist():

    agent = build_agent()

    assert len(agent.instructions) > 0