from models.citation import Citation


def generate_citations(summaries):
    citations = []
    seen_urls = set()

    for summary in summaries:
        if summary.url not in seen_urls:
            citations.append(
                Citation(
                    title=summary.title,
                    url=summary.url
                )
            )
            seen_urls.add(summary.url)

    return citations


def citation_node(state):
    citations = generate_citations(state["summaries"])

    return {
        "citations": citations
    }