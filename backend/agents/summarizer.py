from providers.llm_router import invoke_llm
from models.summary import Summary


def summarize_document(document):
    """
    Summarize a single document.
    """

    prompt = f"""
You are an expert research assistant.

Summarize the following article in under 150 words.

Return ONLY this format:

## Summary
(A concise summary in 100–150 words)

## Key Points
- Point 1
- Point 2
- Point 3

Article:

{document.content[:3000]}
"""

    response = invoke_llm(prompt)

    return Summary(
        title=document.title,
        url=document.url,
        summary=response.content
    )


def summarize_documents(documents):
    """
    Summarize all retrieved documents.
    """

    summaries = []

    for document in documents:
        try:
            summary = summarize_document(document)
            summaries.append(summary)

        except Exception as e:
            print(f"Error summarizing '{document.title}': {e}")

    return summaries


# ---------------- LangGraph Node ---------------- #

def summarizer_node(state):
    """
    LangGraph node for summarization.
    """

    documents = state["documents"]

    summaries = summarize_documents(documents)

    return {
        "summaries": summaries
    }