from providers.llm_router import invoke_llm


def create_research_plan(topic: str):
    prompt = f"""
You are an expert research planner.

Create a structured research plan for the topic:

{topic}

Return:
- Title
- 6-8 major sections
- A short description for each section.
"""

    response = invoke_llm(prompt)

    return response.content


# -------- LangGraph Node -------- #

def planner_node(state):
    topic = state["topic"]

    plan = create_research_plan(topic)

    return {
        "research_plan": plan
    }