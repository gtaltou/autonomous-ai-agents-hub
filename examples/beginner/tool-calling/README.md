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


## Implemented Tools

### Calculator Tool

Supported operations:

```text
+
-
*
/
```

Examples:

```text
What is 457 * 124?

What is (145 + 87) * 3?

What is 100 / 4?
```

## Example

Question:

```text
What is 457 * 124?
```

Response:

```text
56,668
```


---

## Run

```bash
python -m app.main
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

- [x] Tool Definitions
- [x] Tool Registration
- [x] Calculator Tool
- [x] Tool Calling Workflow
- [x] Unit Tests
- [x] Ruff Validation
- [x] Documentation

Future Extensions:

- [ ] Temperature Converter Tool
- [ ] Date Tool
- [ ] Multi-Tool Agent

---


## Validation

✅ OpenAI Tool Calling operational

✅ Calculator Tool operational

✅ Ruff checks passing

✅ Unit tests passing

✅ End-to-End execution validated

## Expected Outcome

At the end of this sprint, the agent will be capable of deciding when a tool should be used and how to use it effectively.

This is the first step from a simple LLM-powered assistant to a true AI Agent.

✅ Completed