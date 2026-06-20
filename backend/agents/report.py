from providers.llm_router import invoke_llm
from tools.report_writer import save_markdown


def generate_report(topic, research_plan, summaries, citations):

    summaries_text = ""

    for summary in summaries:
        summaries_text += f"""
Title: {summary.title}

{summary.summary[:800]}

------------------------------------
"""

    citation_text = ""

    for i, citation in enumerate(citations, start=1):
        citation_text += f"[{i}] {citation.title}\n{citation.url}\n\n"

    prompt = f"""
You are an expert research writer.

Write a professional research report in 600–800 words.

Topic:
{topic}

Research Plan:
{research_plan}

Research Summaries:
{summaries_text}

References:
{citation_text}

Structure the report as follows:

# Title

# Abstract

# Introduction

# Key Concepts

# Applications

# Challenges

# Conclusion

# References

Do not exceed 800 words.
Do not copy the summaries verbatim.
Write in a coherent academic style.
"""

    response = invoke_llm(prompt)

    return response.content


def report_node(state):

    report = generate_report(
        state["topic"],
        state["research_plan"],
        state["summaries"],
        state["citations"]
    )

    report_path = save_markdown(report)

    return {
        "report": report,
        "report_path": report_path
    }