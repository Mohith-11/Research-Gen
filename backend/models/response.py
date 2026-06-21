from pydantic import BaseModel
from typing import List

from models.citation import Citation


class ResearchResponse(BaseModel):
    topic: str
    research_plan: str
    report: str
    citations: List[Citation]