# Hello Agent

The simplest production-ready example built with the OpenAI Agents SDK.

## Learning Objectives

- Create an Agent
- Configure Instructions
- Execute an Agent
- Handle Responses
- Structure a Python project
- Write unit tests

---

## Architecture

```text
User
 │
 ▼
Runner
 │
 ▼
Agent
 │
 ▼
Response
```

---

## Setup

Create a virtual environment:

```bash
uv venv
```

Install dependencies:

```bash
uv pip install -r requirements.txt
```

Create environment file:

```bash
cp .env.example .env
```

Add your OpenAI API key.

---

## Run

```bash
python app/main.py
```

---

## Run Tests

```bash
pytest
```

---

## Expected Output

```text
🤖 Question:

What is an AI Agent?

🤖 Response:

An AI Agent is a software program capable of...
```