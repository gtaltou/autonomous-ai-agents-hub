import asyncio
import time

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
from app.serializers.research import (
    search_result_to_prompt,
    summary_result_to_prompt,
)
from app.logging.execution_logger import (
    ExecutionLogger,
)


class WorkflowError(Exception):
    """Workflow execution error."""


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
    # Shared retry engine
    #

    async def _run_agent_with_retry(
        self,
        agent,
        agent_input: str,
        expected_type,
        timeout: int = 60,
        max_retries: int = 3,
    ):

        for attempt in range(
            1,
            max_retries + 1,
        ):

            try:

                result = await asyncio.wait_for(
                    Runner.run(
                        agent,
                        agent_input,
                    ),
                    timeout=timeout,
                )

                output = result.final_output

                if not isinstance(
                    output,
                    expected_type,
                ):
                    raise WorkflowError(
                        f"{agent.name} returned "
                        f"an invalid output."
                    )

                return output

            except asyncio.TimeoutError:

                if attempt == max_retries:

                    raise WorkflowError(
                        f"{agent.name} timed out "
                        f"after {max_retries} attempts."
                    )

            except Exception as error:

                if attempt == max_retries:

                    raise WorkflowError(
                        f"{agent.name} failed: "
                        f"{error}"
                    ) from error

            backoff = (
                2 ** (attempt - 1)
            )

            print(
                f"⚠️ Retry "
                f"{attempt}/{max_retries}"
                f" for {agent.name}"
                f" in {backoff}s"
            )

            await asyncio.sleep(
                backoff
            )

        raise WorkflowError(
            f"{agent.name} failed."
        )

    #
    # Real OpenAI pipeline
    #

    async def search_real(
        self,
        question: str,
    ) -> SearchResult:

        ExecutionLogger.info(
            "Search Agent started"
        )

        start_time = (
            time.perf_counter()
        )

        try:

            result = await self._run_agent_with_retry(
                agent=self.search_agent,
                agent_input=question,
                expected_type=SearchResult,
            )

            duration = (
                time.perf_counter()
                - start_time
            )

            ExecutionLogger.metric(
                "Search Agent",
                duration,
            )

            ExecutionLogger.info(
                "Search Agent completed"
            )

            return result

        except Exception as error:

            ExecutionLogger.error(
                f"Search Agent failed: "
                f"{error}"
            )

            raise

    async def summarize_real(
        self,
        search_result: SearchResult,
    ) -> SummaryResult:

        ExecutionLogger.info(
            "Summarizer Agent started"
        )

        start_time = (
            time.perf_counter()
        )

        try:

            summary_input = (
                search_result_to_prompt(
                    search_result
                )
            )

            result = await self._run_agent_with_retry(
                agent=self.summarizer_agent,
                agent_input=summary_input,
                expected_type=SummaryResult,
            )

            duration = (
                time.perf_counter()
                - start_time
            )

            ExecutionLogger.metric(
                "Summarizer Agent",
                duration,
            )

            ExecutionLogger.info(
                "Summarizer Agent completed"
            )

            return result

        except Exception as error:

            ExecutionLogger.error(
                f"Summarizer Agent failed: "
                f"{error}"
            )

            raise

    async def fact_check_real(
        self,
        summary_result: SummaryResult,
    ) -> ResearchReport:

        ExecutionLogger.info(
            "Fact Checker Agent started"
        )

        start_time = (
            time.perf_counter()
        )

        try:

            report_input = (
                summary_result_to_prompt(
                    summary_result
                )
            )

            result = await self._run_agent_with_retry(
                agent=self.fact_checker_agent,
                agent_input=report_input,
                expected_type=ResearchReport,
            )

            duration = (
                time.perf_counter()
                - start_time
            )

            ExecutionLogger.metric(
                "Fact Checker Agent",
                duration,
            )

            ExecutionLogger.info(
                "Fact Checker Agent completed"
            )

            return result

        except Exception as error:

            ExecutionLogger.error(
                f"Fact Checker Agent failed: "
                f"{error}"
            )

            raise

    async def run_real(
        self,
        question: str,
    ) -> ResearchReport:

        ExecutionLogger.info(
            "Workflow started"
        )

        workflow_start = (
            time.perf_counter()
        )

        try:

            search_result = await self.search_real(
                question
            )

            summary_result = await self.summarize_real(
                search_result
            )

            report = await self.fact_check_real(
                summary_result
            )

            workflow_duration = (
                time.perf_counter()
                - workflow_start
            )

            ExecutionLogger.metric(
                "Workflow Total",
                workflow_duration,
            )

            ExecutionLogger.info(
                "Workflow completed"
            )

            return report

        except WorkflowError as error:

            workflow_duration = (
                time.perf_counter()
                - workflow_start
            )

            ExecutionLogger.metric(
                "Workflow Total",
                workflow_duration,
            )

            ExecutionLogger.error(
                f"Workflow failed: {error}"
            )

            raise

        except Exception as error:

            workflow_duration = (
                time.perf_counter()
                - workflow_start
            )

            ExecutionLogger.metric(
                "Workflow Total",
                workflow_duration,
            )

            ExecutionLogger.error(
                f"Unexpected workflow error: "
                f"{error}"
            )

            raise WorkflowError(
                f"Workflow failed: {error}"
            ) from error