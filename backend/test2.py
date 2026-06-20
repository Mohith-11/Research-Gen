from agents.search import research_search

results = research_search("Agentic AI")

for i, result in enumerate(results, start=1):
    print(f"\nResult {i}")
    print("Title:", result["title"])
    print("URL:", result["url"])
    print("Content:", result["content"][:200], "...")