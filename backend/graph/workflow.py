from langgraph.graph import StateGraph, START, END

from graph.state import ResearchState

from agents.planner import planner_node
from agents.search import search_node
from agents.reader import reader_node
from agents.summarizer import summarizer_node
from agents.citation import citation_node
from agents.report import report_node

# Create the graph
graph = StateGraph(ResearchState)

# ---------------- Nodes ---------------- #

graph.add_node("planner", planner_node)
graph.add_node("search", search_node)
graph.add_node("reader", reader_node)
graph.add_node("summarizer", summarizer_node)
graph.add_node("citation", citation_node)
graph.add_node("report", report_node)

# ---------------- Edges ---------------- #

graph.add_edge(START, "planner")
graph.add_edge("planner", "search")
graph.add_edge("search", "reader")
graph.add_edge("reader", "summarizer")
graph.add_edge("summarizer", "citation")
graph.add_edge("citation", "report")
graph.add_edge("report", END)

# Compile the graph
research_graph = graph.compile()