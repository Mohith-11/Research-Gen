from typing import TypedDict, List

from models.search import SearchResult
from models.document import Document
from models.summary import Summary
from models.citation import Citation


class ResearchState(TypedDict):
    topic: str
    research_plan: str

    search_results: List[SearchResult]

    documents: List[Document]

    summaries: List[Summary]

    citations: List[Citation]

    report: str

    report_path: str