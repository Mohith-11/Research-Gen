#
from fastapi import APIRouter

from graph.workflow import research_graph
from models.request import ResearchRequest
from models.response import ResearchResponse

router = APIRouter()


@router.post("/research", response_model=ResearchResponse)
def generate_research(request: ResearchRequest):

    result = research_graph.invoke(
        {
            "topic": request.topic
        }
    )

    return ResearchResponse(
        topic=result["topic"],
        research_plan=result["research_plan"],
        report=result["report"],
        citations=result["citations"]
    )