from tools.webpage_loader import load_webpage
from models.document import Document


def read_sources(search_results):
    """
    Reads each webpage and extracts the full text.
    """

    documents = []

    for result in search_results:

        text = load_webpage(result.url)

        documents.append(
            Document(
                title=result.title,
                url=result.url,
                content=text
            )
        )

    return documents


# -------- LangGraph Node -------- #

def reader_node(state):

    search_results = state["search_results"]

    documents = read_sources(search_results)

    return {
        "documents": documents
    }