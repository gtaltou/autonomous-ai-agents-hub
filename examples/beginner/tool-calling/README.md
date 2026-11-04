# Tool Calling

Learn how AI Agents interact with external tools using the OpenAI Agents SDK.

---

## Objectives

This project introduces one of the most important concepts in Agentic AI:

**Tool Calling**

Instead of generating an answer directly, the agent can:

- Select a tool
- Execute a function
- Analyze the result
- Generate an informed response

---

## Learning Goals

By completing this example, you will learn:

- Tool Definitions
- Function Calling
- Agent Decision Making
- Tool Execution
- Result Interpretation
- Testing Tool Functions

---

## Architecture

```text
User
 │
 ▼
Agent
 │
 ├── Calculator Tool
 ├── Temperature Converter Tool
 └── Date Tool
 │
 ▼
Response
```

---

## Planned Tools

### Calculator Tool

Examples:

```text
What is 245 + 987?
```

---

### Temperature Converter Tool

Examples:

```text
Convert 20°C to Fahrenheit
```

---

### Date Tool

Examples:

```text
What date is it today?
```

---

## Project Structure

```text
tool-calling/
│
├── app/
│   ├── agent.py
│   ├── config.py
│   ├── tools.py
│   └── main.py
│
├── tests/
│   ├── test_tools.py
│   └── test_agent.py
│
├── README.md
├── requirements.txt
├── pytest.ini
└── .env.example
```

---

## Run

```bash
python app/main.py
```

---

## Run Tests

```bash
pytest -v
```

---

## Quality Checks

```bash
python -m ruff check .
```

---

## Sprint Status

🚧 In Progress

---

## Sprint Objectives

- [ ] Tool Definitions
- [ ] Tool Registration
- [ ] Calculator Tool
- [ ] Temperature Converter Tool
- [ ] Date Tool
- [ ] Tool Calling Workflow
- [ ] Unit Tests
- [ ] Documentation

---

## Expected Outcome

At the end of this sprint, the agent will be capable of deciding when a tool should be used and how to use it effectively.

This is the first step from a simple LLM-powered assistant to a true AI Agent.