# Structured Outputs

Learn how to generate validated and typed responses using the OpenAI Agents SDK and Pydantic.

---

## Objectives

This project introduces structured outputs.

Instead of returning free-form text, the agent returns validated Python objects.

---

## Learning Goals

By completing this example, you will learn:

- Pydantic Models
- Structured Outputs
- Response Validation
- Typed Responses
- JSON Reliability
- Agent Output Schemas

---

## Architecture

```text
User
 │
 ▼
Agent
 │
 ▼
Pydantic Model
 │
 ▼
Structured Output
```

---

## Example

Input:

```text
John Doe is 42 years old and lives in Paris.
```

Output:

```json
{
  "name": "John Doe",
  "age": 42,
  "city": "Paris"
}
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

- [ ] Create Pydantic Schema
- [ ] Configure Structured Output
- [ ] Validate Responses
- [ ] Unit Tests
- [ ] Ruff Validation
- [ ] Documentation

---

## Expected Outcome

The agent will return a validated Python object rather than free-form text.