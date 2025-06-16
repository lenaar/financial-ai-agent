from state import State
from langgraph.graph import StateGraph
from nodes import gather_financial_data_node, analyze_financial_data_node, analyze_competitors_node

def build_graph_agent():
    graph = StateGraph(State)

    graph.add_node("gather_financial_data", gather_financial_data_node)
    graph.add_node("analyze_financial_data", analyze_financial_data_node)
    graph.add_node("analyze_competitors", analyze_competitors_node)

    # Define the flow
    graph.add_edge("gather_financial_data", "analyze_financial_data")
    graph.add_edge("analyze_financial_data", "analyze_competitors")

    graph.set_entry_point("gather_financial_data")
    return graph.compile()