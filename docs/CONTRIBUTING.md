# 🤝 Contributing Guide

Thank you for your interest in contributing to Autonomous AI Agents Hub.

This repository aims to become a high-quality reference for Agentic AI Engineering, covering modern AI systems built with:

- OpenAI Agents SDK
- MCP (Model Context Protocol)
- LangGraph
- CrewAI
- AutoGen
- RAG Systems
- Evaluation Frameworks
- Production AI Architecture

The goal is to prioritize clarity, maintainability, reproducibility, and engineering best practices.

---

# 🎯 Contribution Principles

Every contribution should satisfy at least one of the following objectives:

| Objective | Description |
|:---|:---|
| Learning | Help engineers understand Agentic AI concepts |
| Reusability | Provide reusable patterns and components |
| Reliability | Improve quality and stability |
| Documentation | Improve understanding and onboarding |
| Production Readiness | Move projects closer to real-world deployment |

If a contribution does not improve one of these areas, it should be reconsidered.

---

# 🏗 Repository Structure

All projects should follow the repository architecture standards.

```text
project-name/
│
├── app/
├── agents/
├── tools/
├── prompts/
├── memory/
├── configs/
├── tests/
├── docs/
│
├── README.md
└── main.py
```

---

# 📋 Before Contributing

Before starting development:

- Review the README
- Review the ROADMAP
- Review the ARCHITECTURE guide
- Review the LEARNING_PATH document

Ensure your contribution aligns with the repository vision and architecture.

---

# 🔀 Git Workflow

## Create a Feature Branch

```bash
git checkout -b feature/short-description
```

Examples:

```bash
feature/research-agent
feature/chromadb-integration
feature/mcp-filesystem
feature/langgraph-routing
```

---

## Keep Branches Small

Preferred:

✅ Small focused pull requests

Avoid:

❌ Massive multi-feature pull requests

---

# 📝 Commit Convention

Use Conventional Commits.

## Features

```bash
feat: add research agent
```

## Bug Fixes

```bash
fix: handle empty search results
```

## Documentation

```bash
docs: update architecture guide
```

## Refactoring

```bash
refactor: simplify agent orchestration
```

## Tests

```bash
test: add evaluation suite
```

## CI/CD

```bash
ci: update github workflow
```

---

# 🧪 Testing Requirements

Every significant contribution should include testing when applicable.

---

## Required Tests

| Area | Requirement |
|:---|:---|
| Agent Logic | Unit Tests |
| RAG Pipelines | Retrieval Validation |
| Tool Integration | Integration Tests |
| Utility Functions | Unit Tests |

---

## Goal

```text
Code → Test → Evaluate → Improve
```

Every project should aim for reliability rather than complexity.

---

# 🤖 Agent Design Standards

All agents should follow a consistent structure.

---

## Agent Responsibilities

Each agent should have:

| Requirement | Description |
|:---|:---|
| Single Responsibility | One primary role |
| Clear Instructions | Explicit behavior |
| Error Handling | Graceful failure |
| Observability | Logging and tracing |
| Documentation | Usage examples |

---

## Good Example

```text
Research Agent
│
├── Search Sources
├── Retrieve Documents
└── Return Findings
```

---

## Bad Example

```text
Super Agent
│
├── Research
├── Coding
├── Marketing
├── Planning
├── Evaluation
└── Everything Else
```

Avoid large agents with multiple responsibilities.

---

# 📚 Documentation Standards

Every project must contain a README.

---

## Required Sections

| Section | Mandatory |
|:---|:---:|
| Overview | ✅ |
| Architecture | ✅ |
| Setup | ✅ |
| Usage | ✅ |
| Limitations | ✅ |

---

## Example Structure

```md
# Project Name

## Overview

## Architecture

## Setup

## Usage

## Limitations
```

---

# 📦 Dependency Management

The repository standard is:

```text
uv
```

---

## Install Dependencies

```bash
uv sync
```

---

## Add Dependencies

```bash
uv add package-name
```

---

## Update Lock File

```bash
uv lock
```

---

# 🔐 Security Guidelines

Security takes priority over convenience.

---

## Rules

| Rule | Requirement |
|:---|:---:|
| No Hardcoded API Keys | ✅ |
| Environment Variables Only | ✅ |
| Principle of Least Privilege | ✅ |
| Input Validation | ✅ |
| Logging | ✅ |

---

## Secrets

Never commit:

```text
.env
.env.local
api_keys.txt
credentials.json
```

---

# 📊 Evaluation Standards

Every AI system should be measurable.

---

## Evaluation Areas

| Metric | Why It Matters |
|:---|:---|
| Accuracy | Response quality |
| Groundedness | Hallucination reduction |
| Latency | User experience |
| Reliability | Stability |
| Cost | Operational efficiency |

---

## Rule

If it cannot be evaluated, it cannot be improved.

---

# 🏭 Production Readiness Checklist

Before a project can be considered production-ready:

- [ ] Clear architecture
- [ ] Documentation completed
- [ ] Error handling implemented
- [ ] Logging enabled
- [ ] Tests implemented
- [ ] Evaluation completed
- [ ] Environment variables configured
- [ ] Security review performed

---

# 🧠 Learning Contributions

Educational contributions are strongly encouraged.

Examples:

- Architecture diagrams
- Tutorials
- Walkthroughs
- Best practices
- MCP examples
- LangGraph patterns
- CrewAI patterns
- AutoGen experiments

---

# 🚫 What We Do Not Accept

The following contributions are generally discouraged:

❌ Hardcoded secrets

❌ Unmaintainable code

❌ Undocumented projects

❌ Copy-pasted examples without explanation

❌ Large features without tests

❌ Breaking existing architecture standards

---

# 🎯 Definition of Done

A contribution is considered complete when:

| Requirement | Status |
|:---|:---:|
| Code Implemented | ✅ |
| Tests Added | ✅ |
| Documentation Updated | ✅ |
| Architecture Respected | ✅ |
| Security Reviewed | ✅ |

---

# 🚀 Long-Term Goal

Build one of the most comprehensive public repositories dedicated to Agentic AI Engineering.

The focus is not on creating the most complex systems.

The focus is on building reliable, understandable, maintainable, and production-ready AI architectures.