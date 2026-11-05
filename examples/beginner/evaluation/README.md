# Evaluation

Learn how to automatically evaluate the quality of AI Agent outputs using the OpenAI Agents SDK.

---

## Objective

Building an agent is only the first step.

To operate AI systems reliably in production, we must be able to evaluate their outputs automatically.

This example demonstrates how to:

- Generate a structured response
- Define an expected result
- Compare actual and expected outputs
- Produce a PASS / FAIL evaluation

---

## Learning Goals

By completing this example, you will learn:

- Evaluation fundamentals
- Automated validation
- Quality gates
- Regression testing concepts
- PASS / FAIL workflows
- Reusable evaluation patterns

---

## Architecture

```text
Input Text
     │
     ▼
AI Agent
     │
     ▼
Structured Output
     │
     ▼
Evaluator
     │
     ▼
PASS / FAIL
```

---

## Project Structure

```text
evaluation/
│
├── app/
│   ├── agent.py
│   ├── config.py
│   ├── evaluator.py
│   ├── main.py
│   └── models.py
│
├── tests/
│   ├── test_agent.py
│   ├── test_models.py
│   └── test_evaluator.py
│
├── README.md
├── requirements.txt
├── pytest.ini
└── .env.example
```

---

## Example

### Input

```text
John Doe is 42 years old and lives in Paris.
```

### Expected Output

```python
Person(
    name="John Doe",
    age=42,
    city="Paris"
)
```

### Actual Output

```python
Person(
    name="John Doe",
    age=42,
    city="Paris"
)
```

### Evaluation

```text
✅ PASS
```

---

## Run

```bash
python -m app.main
```

---

## Run Tests

```bash
python -m pytest -v
```

---

## Run Quality Checks

```bash
python -m ruff check .
```

---

## Validation Criteria

The sprint is considered complete when:

- Agent executes successfully
- Structured output is generated
- Evaluation produces PASS / FAIL
- Tests pass
- Ruff passes
- End-to-end workflow is validated

---

## Expected Output

```text
📝 Input:
John Doe is 42 years old and lives in Paris.

🎯 Expected:
name='John Doe' age=42 city='Paris'

🤖 Actual:
name='John Doe' age=42 city='Paris'

📊 Evaluation Result:
✅ PASS
```

---

## Key Takeaways

This example introduces the concept of evaluation, which is essential for:

- Research Assistants
- RAG Applications
- MCP-based Agents
- Multi-Agent Systems
- Production AI Systems

Without evaluation, agent quality cannot be measured reliably.

This example completes the OpenAI Agents SDK fundamentals track.
