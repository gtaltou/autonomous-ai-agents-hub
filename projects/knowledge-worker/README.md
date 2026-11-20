# Knowledge Worker

A Python application that analyzes collections of markdown reports and extracts actionable knowledge through topic discovery, recommendations, report ranking, and similarity analysis.




## Status

```text
Version: 1.1.0
Tests: 62/62 Passing
Lint: Ruff Passing
Status: Production Ready
```


## Installation

### Prérequis

- Python 3.10+
- Git

Vérifiez votre version Python :

```bash
python --version
```

---

### Cloner le dépôt

```bash
git clone <repository-url>
cd projects/knowledge-worker
```

---

### Créer un environnement virtuel

Windows :

```bash
python -m venv .venv
```

Activer l'environnement :

```bash
.venv\Scripts\activate
```

---

### Installer les dépendances

```bash
pip install -r requirements.txt
```

---

### Vérifier l'installation

Exécutez :

```bash
python -m pytest -v
```

Résultat attendu :

```text
62 passed
```

Puis :

```bash
python -m ruff check .
```

Résultat attendu :

```text
All checks passed!
```

---

## Configuration

### Structure du projet

```text
knowledge-worker/
│
├── app/
│   ├── analyzers/
│   ├── models/
│   ├── repositories/
│   ├── services/
│   └── main.py
│
├── reports/
│
├── tests/
│
├── requirements.txt
├── pytest.ini
└── README.md
```

---

### Répertoire des rapports

Le moteur de connaissances analyse automatiquement les fichiers Markdown présents dans :

```text
reports/
```

Exemple :

```text
reports/
├── fusion-energy.md
├── energy-storage.md
└── fusion-research.md
```

---

### Format attendu d'un rapport

Chaque rapport doit contenir des métadonnées exploitables.

Exemple :

```markdown
# Fusion Energy

Score: 95

Grade: EXCELLENT

Fusion energy technologies continue to evolve...
```

---

### Métadonnées extraites

Le système extrait automatiquement :

```text
Topic
Score
Grade
```

Exemple :

```text
Topic  -> Fusion Energy
Score  -> 95
Grade  -> EXCELLENT
```

---

## Quick Start

Afficher les meilleurs rapports :

```bash
python -m app.main --top-reports
```

Afficher les sujets :

```bash
python -m app.main --topics
```

Afficher les recommandations :

```bash
python -m app.main --recommendations
```

Afficher les sujets principaux :

```bash
python -m app.main --top-topics
```

Afficher les rapports similaires :

```bash
python -m app.main --related "Fusion Energy"
```

---

## JSON Export

Tous les résultats peuvent être exportés au format JSON.

### Topics

```bash
python -m app.main --topics --json
```

### Top Topics

```bash
python -m app.main --top-topics --json
```

### Recommendations

```bash
python -m app.main --recommendations --json
```

### Related Reports

```bash
python -m app.main --related "Fusion Energy" --json
```

### Top Reports

```bash
python -m app.main --top-reports --json
```


## Features

### Top Reports

Retrieve the highest-scoring reports.

```bash
python -m app.main --top-reports
```

Example:

```text
TOP REPORTS
========================================

1. Fusion Energy
   Score: 95
   Grade: EXCELLENT
```

---

### Topics

Discover the most common topics across reports.

```bash
python -m app.main --topics
```

Example:

```text
TOPICS
========================================

energy: 2
fusion: 2
storage: 1
research: 1
```

---

### Top Topics

Display topics ranked by popularity.

```bash
python -m app.main --top-topics
```

Example:

```text
TOP TOPICS
========================================

1. energy (2)
2. fusion (2)
3. storage (1)
4. research (1)
```

---

### Recommendations

Generate topic recommendations based on report analysis.

```bash
python -m app.main --recommendations
```

Example:

```text
RECOMMENDATIONS
========================================

energy
fusion
storage
```

Custom limit:

```bash
python -m app.main --recommendations 5
```

---

### Related Reports

Find reports related to a specific topic.

```bash
python -m app.main --related "Fusion Energy"
```

Example:

```text
RELATED REPORTS
========================================

1. Fusion Research

2. Energy Storage
```

---

## JSON Export

All major commands support JSON output.

### Topics

```bash
python -m app.main --topics --json
```

Example:

```json
{
    "energy": 2,
    "fusion": 2,
    "storage": 1,
    "research": 1
}
```

---

### Top Topics

```bash
python -m app.main --top-topics --json
```

---

### Recommendations

```bash
python -m app.main --recommendations --json
```

---

### Related Reports

```bash
python -m app.main --related "Fusion Energy" --json
```

---

### Top Reports

```bash
python -m app.main --top-reports --json
```

---

## Architecture

```text
app/
├── analyzers/
│   ├── recommendations.py
│   ├── related_reports.py
│   ├── top_reports.py
│   ├── top_topics.py
│   └── topic_discovery.py
│
├── repositories/
│   └── report_repository.py
│
├── services/
│   └── knowledge_service.py
│
├── models/
│   └── report_metadata.py
│
└── main.py
```

### Layers

#### Repository Layer

Responsible for loading markdown reports and extracting metadata.

#### Analyzer Layer

Contains all business logic:

- TopReportsAnalyzer
- RelatedReportsAnalyzer
- TopicDiscoveryAnalyzer
- RecommendationsAnalyzer
- TopTopicsAnalyzer

#### Service Layer

Coordinates repositories and analyzers.

#### CLI Layer

Provides command-line access to all features.

---

## Quality

Project quality gates:

```text
✅ Ruff

✅ 70 Passing Tests

✅ 92% Code Coverage

✅ Type Hints

✅ Layered Architecture

✅ Repository Pattern

✅ Service Layer

✅ REST API Layer

✅ Docker Support

✅ GitHub Actions CI

✅ OpenAPI Documentation

✅ Swagger UI
```

Testing Strategy:

```text
✅ Unit Tests

✅ Integration Tests

✅ API Tests

✅ End-to-End API Workflow
```

Current status:

```text
Version: v1.2.1

Tests: 70 Passed

Coverage: 92%

Lint: All Checks Passed

Docker: Validated

CI Pipeline: Passing

REST API: Complete

OpenAPI: Complete

Swagger: Complete

Status: Production Ready
```

---

## Running Tests

```bash
python -m pytest -v
```

---

## Running Ruff

```bash
python -m ruff check .
```

---

## Usage Summary

```bash
python -m app.main --top-reports

python -m app.main --topics

python -m app.main --top-topics

python -m app.main --recommendations

python -m app.main --recommendations 5

python -m app.main --related "Fusion Energy"

python -m app.main --topics --json

python -m app.main --top-topics --json

python -m app.main --recommendations --json

python -m app.main --related "Fusion Energy" --json
```

---

## Version

```text
Knowledge Worker v1.1.0
```

A lightweight knowledge analysis engine for markdown-based report collections.