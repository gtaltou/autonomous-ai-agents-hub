from agents import Runner

from app.agents.coordinator import (
    build_coordinator_agent,
)
from app.agents.fact_checker import (
    build_fact_checker_agent,
)
from app.agents.search import (
    build_search_agent,
)
from app.agents.summarizer import (
    build_summarizer_agent,
)
from app.models import (
    ResearchReport,
    SearchResult,
    SummaryResult,
)


class ResearchWorkflow:

    def __init__(self):

        self.coordinator = (
            build_coordinator_agent()
        )

        self.search_agent = (
            build_search_agent()
        )

        self.summarizer_agent = (
            build_summarizer_agent()
        )

        self.fact_checker_agent = (
            build_fact_checker_agent()
        )

    def describe(self) -> dict:

        return {
            "coordinator": self.coordinator.name,
            "search": self.search_agent.name,
            "summarizer": self.summarizer_agent.name,
            "fact_checker": self.fact_checker_agent.name,
        }

    #
    # Mock pipeline (tests)
    #

    def search(
        self,
        question: str,
    ) -> SearchResult:

        return SearchResult(
            topic=question,
            findings=[
                "Finding 1",
                "Finding 2",
                "Finding 3",
            ],
            source_count=3,
        )

    def summarize(
        self,
        search_result: SearchResult,
    ) -> SummaryResult:

        return SummaryResult(
            summary=(
                f"Summary about "
                f"{search_result.topic}"
            ),
            key_points=search_result.findings,
            confidence_score=0.90,
        )

    def fact_check(
        self,
        summary_result: SummaryResult,
    ) -> ResearchReport:

        return ResearchReport(
            topic="Validated Research",
            executive_summary=(
                summary_result.summary
            ),
            key_findings=(
                summary_result.key_points
            ),
            sources_reviewed=[
                "Internal Validation",
            ],
            fact_check_notes=(
                "Validated by Fact Checker."
            ),
            final_conclusion=(
                "Research completed."
            ),
        )

    def run(
        self,
        question: str,
    ) -> ResearchReport:

        search_result = self.search(
            question
        )

        summary_result = self.summarize(
            search_result
        )

        report = self.fact_check(
            summary_result
        )

        return report

    #
    # Real OpenAI pipeline
    #

    async def search_real(
        self,
        question: str,
    ) -> SearchResult:

        result = await Runner.run(
            self.search_agent,
            question,
        )

        return result.final_output

    async def summarize_real(
        self,
        search_result: SearchResult,
    ) -> SummaryResult:

        summary_input = f"""
Topic:
{search_result.topic}

Findings:
{chr(10).join(search_result.findings)}

Source Count:
{search_result.source_count}
"""

        result = await Runner.run(
            self.summarizer_agent,
            summary_input,
        )

        return result.final_output

    async def fact_check_real(
        self,
        summary_result: SummaryResult,
    ) -> ResearchReport:

        report_input = f"""
Summary:
{summary_result.summary}

Key Points:
{chr(10).join(summary_result.key_points)}

Confidence Score:
{summary_result.confidence_score}
"""

        result = await Runner.run(
            self.fact_checker_agent,
            report_input,
        )

        print()
        print("DEBUG FACT CHECKER OUTPUT")
        print(type(result.final_output))
        print(result.final_output)

        return result.final_output

    async def run_real(
        self,
        question: str,
    ) -> ResearchReport:

        search_result = await self.search_real(
            question
        )

        summary_result = await self.summarize_real(
            search_result
        )

        report = await self.fact_check_real(
            summary_result
        )

        return report