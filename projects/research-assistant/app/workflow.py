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


class ResearchWorkflow:

    def __init__(self):

        self.coordinator = (
            build_coordinator_agent()
        )

        self.search = (
            build_search_agent()
        )

        self.summarizer = (
            build_summarizer_agent()
        )

        self.fact_checker = (
            build_fact_checker_agent()
        )

    def describe(self) -> dict:

        return {
            "coordinator": self.coordinator.name,
            "search": self.search.name,
            "summarizer": self.summarizer.name,
            "fact_checker": self.fact_checker.name,
        }