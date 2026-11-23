# RAG Assistant

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Tests](https://img.shields.io/badge/Tests-34_Passed-success)
![Coverage](https://img.shields.io/badge/Coverage-100%25-success)
![MyPy](https://img.shields.io/badge/MyPy-Passing-success)
![Ruff](https://img.shields.io/badge/Ruff-Passing-success)
![Semantic RAG](https://img.shields.io/badge/Semantic_RAG-v3.0.0-purple)
![OpenAI](https://img.shields.io/badge/OpenAI-Integrated-green)

A production-oriented Retrieval-Augmented Generation (RAG) assistant built with clean architecture, semantic retrieval, OpenAI embeddings, vector similarity search, and end-to-end validation.

---

> 🚀 **Release v3.0.0**
>
> End-to-end Semantic Retrieval-Augmented Generation pipeline powered by OpenAI Embeddings, vector similarity search, cached embeddings, semantic retrieval, and clean architecture principles.

---

# Table of Contents

- [Overview](#overview)
- [Current Status](#current-status)
- [Architecture](#architecture)
- [Project Structure](#project-structure)
- [Features](#features)
- [Semantic Retrieval Flow](#semantic-retrieval-flow)
- [Example](#example)
- [Testing](#testing)
- [Design Principles](#design-principles)
- [Road to Production](#road-to-production)
- [License](#license)

---


# Overview

RAG Assistant demonstrates the complete lifecycle of a modern Retrieval-Augmented Generation pipeline:

```text
Document
    ↓
Chunking
    ↓
Embeddings
    ↓
Vector Storage
    ↓
Semantic Retrieval
    ↓
Context Building
    ↓
LLM Generation
    ↓
Answer
```

The project is intentionally designed with strong separation of concerns, dependency injection, strict type checking, and comprehensive automated testing.

---

# Current Status

## Release

```text
v3.0.0
```

## Quality Gates

```text
✅ Pytest
✅ Ruff
✅ MyPy
✅ Type Hints
✅ Dependency Injection
✅ Layered Architecture
✅ Semantic Search
✅ OpenAI Embeddings
✅ Cached Embeddings
✅ Semantic RAG Pipeline
✅ 100% Test Coverage
```

## Metrics

```text
Tests:        34 Passed
Coverage:     100%
MyPy:         Clean
Ruff:         Clean
Architecture: Layered
```

---

# Architecture

## High-Level Architecture

```text
                         ┌─────────────────┐
                         │     User        │
                         └────────┬────────┘
                                  │
                                  ▼
                    ┌────────────────────────┐
                    │ SemanticRagPipeline    │
                    └───────────┬────────────┘
                                │
                  ┌─────────────┴─────────────┐
                  ▼                           ▼
     ┌────────────────────┐      ┌────────────────────┐
     │ ContextBuilder     │      │ SemanticRetrieval  │
     └────────────────────┘      └─────────┬──────────┘
                                           │
                                           ▼
                             ┌────────────────────────┐
                             │ SemanticVectorStore    │
                             └───────────┬────────────┘
                                         │
                                Cosine Similarity
                                         │
                                         ▼

                          ┌─────────────────────────┐
                          │ EmbeddedDocument        │
                          └──────────┬──────────────┘
                                     │
                                     ▼
                           ┌────────────────────┐
                           │ EmbeddingIndexer   │
                           └──────────┬─────────┘
                                      │
                                      ▼
                       ┌─────────────────────────────┐
                       │ CachedEmbeddingService      │
                       └──────────┬──────────────────┘
                                  │
                                  ▼
                       ┌─────────────────────────────┐
                       │ OpenAIEmbeddingService      │
                       └─────────────────────────────┘
```

---

# Project Structure

```text
app
│
├── chunking
│   └── text_chunker.py
│
├── config
│   └── settings.py
│
├── embeddings
│   ├── embedding_service.py
│   ├── fake_embedding_service.py
│   ├── openai_embedding_service.py
│   └── cached_embedding_service.py
│
├── llm
│   ├── llm_interface.py
│   ├── fake_llm.py
│   └── openai_client.py
│
├── models
│   ├── document_chunk.py
│   └── embedded_document.py
│
├── rag
│   ├── context_builder.py
│   ├── rag_pipeline.py
│   └── semantic_rag_pipeline.py
│
├── retrieval
│   ├── retrieval_service.py
│   └── semantic_retrieval_service.py
│
├── services
│   ├── document_indexer.py
│   ├── embedding_indexer.py
│   └── semantic_document_indexer.py
│
├── vectorstore
│   ├── in_memory_vector_store.py
│   ├── semantic_vector_store.py
│   ├── vector_similarity.py
│   └── vector_store.py
│
├── main.py
└── semantic_main.py
```

---

# Features

## Document Processing

```text
✅ Text Chunking
✅ Context Building
✅ Document Indexing
```

## Embeddings

```text
✅ EmbeddingService Abstraction
✅ OpenAI Embeddings
✅ Cached Embeddings
```

## Vector Search

```text
✅ Cosine Similarity
✅ SemanticVectorStore
✅ EmbeddedDocument Model
```

## Retrieval

```text
✅ Lexical Retrieval
✅ Semantic Retrieval
✅ Top-K Retrieval
```

## Pipelines

```text
✅ RagPipeline
✅ SemanticRagPipeline
```

## OpenAI Integration

```text
✅ GPT Responses API
✅ Text Embeddings API
```

---

# Semantic Retrieval Flow

```text
Question
    ↓
OpenAI Embedding
    ↓
Cached Embedding Layer
    ↓
SemanticVectorStore
    ↓
Cosine Similarity Ranking
    ↓
Top-K Results
    ↓
Context Builder
    ↓
GPT
    ↓
Answer
```

---

# Example

## Run

```bash
python -m app.semantic_main
```

## Example Output

```text
Python is a programming language.
```

---

# Testing

Run the complete test suite:

```bash
pytest -v
```

Run static analysis:

```bash
ruff check .
```

Type checking:

```bash
mypy .
```

Coverage:

```bash
pytest --cov=app --cov-report=term-missing
```

---

# Design Principles

## Clean Architecture

Each layer has a single responsibility.

```text
Models
    ↓
Services
    ↓
Retrieval
    ↓
RAG
    ↓
LLM
```

## Testability

Every component can be tested independently.

```text
Dependency Injection
+
Fake Implementations
+
Semantic Integration Tests
```

## Extensibility

The architecture allows easy replacement of:

```text
Embeddings Provider
Vector Store
LLM Provider
Retrieval Strategy
```

---

# Road to Production

Current implementation:

```text
Semantic RAG
+
OpenAI Embeddings
+
In-Memory Vector Store
```

Future milestones:

```text
Persistent Embedding Cache
Multi-Document Corpus
ChromaDB Integration
FAISS Integration
CLI Interface
Production Configuration Profiles
```

---


# License

Educational and experimental project for learning modern RAG architecture, semantic search, vector retrieval, and LLM integration.