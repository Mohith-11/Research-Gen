from tools.tavily_tool import search_web
from models.search import SearchResult


def research_search(topic: str):
    results = search_web(topic, max_results=2)

    formatted_results = []

    for result in results:
        formatted_results.append(
            SearchResult(
                title=result["title"],
                url=result["url"],
                content=result["content"]
            )
        )

    return formatted_results


# -------- LangGraph Node -------- #

def search_node(state):
    topic = state["topic"]

    results = research_search(topic)

    return {
        "search_results": results
    }