from dataclasses import dataclass

from pydantic import BaseModel


class SearchResult(BaseModel):

    topic: str
    findings: list[str]
    source_count: int


class SummaryResult(BaseModel):

    summary: str
    key_points: list[str]
    confidence_score: float


class ResearchReport(BaseModel):

    topic: str

    executive_summary: str

    key_findings: list[str]

    sources_reviewed: list[str]

    fact_check_notes: str

    final_conclusion: str


@dataclass
class ReportMetadata:

    filename: str
    topic: str
    score: int
    grade: str