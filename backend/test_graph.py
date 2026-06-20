from graph.workflow import research_graph

result = research_graph.invoke(
    {
        "topic": "Agentic AI"
    }
)

print(result.keys())

print("\n" + "=" * 80)
print("RESEARCH TOPIC")
print("=" * 80)
print(result["topic"])

print("\n" + "=" * 80)
print("RESEARCH PLAN")
print("=" * 80)
print(result["research_plan"])

print("\n" + "=" * 80)
print("SEARCH RESULTS")
print("=" * 80)

for i, search in enumerate(result["search_results"], start=1):
    print(f"\nResult {i}")
    print(f"Title : {search.title}")
    print(f"URL   : {search.url}")

print("\n" + "=" * 80)
print("DOCUMENTS")
print("=" * 80)

for i, document in enumerate(result["documents"], start=1):
    print(f"\nDocument {i}")
    print(f"Title : {document.title}")
    print(f"URL   : {document.url}")
    print(f"Content Preview:\n{document.content[:300]}...")
    print("-" * 80)

print("\n" + "=" * 80)
print("SUMMARIES")
print("=" * 80)

for i, summary in enumerate(result["summaries"], start=1):
    print(f"\nSummary {i}")
    print(f"Title : {summary.title}")
    print(summary.summary)
    print("-" * 80)

print("\n" + "=" * 80)
print("CITATIONS")
print("=" * 80)

for i, citation in enumerate(result["citations"], start=1):
    print(f"[{i}] {citation.title}")
    print(citation.url)
    print()

print("\n" + "=" * 80)
print("REPORT")
print("=" * 80)

print(result["report"])

print("\n" + "=" * 80)
print("REPORT SAVED")
print("=" * 80)

print(result["report_path"])