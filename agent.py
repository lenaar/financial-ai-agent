from state import State
from langgraph.graph import StateGraph
from nodes import gather_financial_data_node, analyze_financial_data_node, analyze_competitors_node, compare_performance_node, collect_feedback_node, research_feedback_node, write_report_node
from langgraph.graph import END

def should_continue_node(state: State) -> State:
    if state.get("revisions", 1) > state.get("max_revisions", 3):
        return END
    else:
        return "collect_feedback"

def build_graph_agent(checkpointer):
    graph = StateGraph(State)

    graph.add_node("gather_financial_data", gather_financial_data_node)
    graph.add_node("analyze_financial_data", analyze_financial_data_node)
    graph.add_node("analyze_competitors", analyze_competitors_node)
    graph.add_node("compare_performance", compare_performance_node)
    graph.add_node("collect_feedback", collect_feedback_node)
    graph.add_node("research_feedback", research_feedback_node)
    graph.add_node("write_report", write_report_node)



    # Define the flow
    graph.add_edge("gather_financial_data", "analyze_financial_data")
    graph.add_edge("analyze_financial_data", "analyze_competitors")
    graph.add_edge("analyze_competitors", "compare_performance")
    
    graph.add_conditional_edges("compare_performance", should_continue_node, {END: END, "collect_feedback": "collect_feedback"})
    
    graph.add_edge("collect_feedback", "research_feedback")
    graph.add_edge("research_feedback", "compare_performance")
    graph.add_edge("compare_performance", "write_report")

    graph.add_edge("write_report", END)

    graph.set_entry_point("gather_financial_data")
    return graph.compile(checkpointer=checkpointer)