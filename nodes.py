import prompts 
from langchain_core.messages import SystemMessage, HumanMessage
from model import model, generate_model_response, generate_model_response_with_structured_output
from typing import Dict, List
from state import State, Queries
from search_tool import tavily
from csv_data import get_csv_data

def gather_financial_data_node(state: State) -> State:
    content = get_csv_data(state)
    financial_content = generate_model_response(content, prompts.GATHER_FINANCIAL_PROMPT)
    print(f"Financial content: {financial_content}")
    return {"financial_data": financial_content}

def analyze_financial_data_node(state: State) -> State:
    analysis = generate_model_response(state["financial_data"], prompts.ANALYZE_DATA_PROMPT)
    print(f"Financial Analysis: {analysis}")
    return {"financial_analysis": analysis}

def analyze_competitors_node(state: State) -> State:
    competitors_content = state.get("full_content") or []
    for competitor in state.get("competitors_names", []):
        queries = model.with_structured_output(Queries).invoke(
            [
                SystemMessage(content=prompts.ANALYZE_COMPETITORS_PROMPT),
                HumanMessage(content=competitor)
            ]
        )
    
        for query in queries.queries:
            research_content = tavily.search(query=query, max_results=2)
            for result in research_content["results"]:
                competitors_content.append(result["content"])

    print(f"Competitors content: {competitors_content}")
    return {"full_content": competitors_content}

def compare_performance_node(state: State) -> State:
    message = f"The task is {state['task']} \n\n The financial analysis is {state['financial_analysis']} \n\n The content is {state['financial_data']}"
    performance_comparison = generate_model_response(message, prompts.COMPARE_PERFORMANCE_PROMPT)
    revisions = state.get("revisions", 1) + 1
    return {
        "performance_comparison": performance_comparison,
        "revisions": revisions,
    }

def collect_feedback_node(state: State) -> State:
    feedback = generate_model_response(state["performance_comparison"], prompts.FEEDBACK_PROMPT)
    return {"feedback": feedback}

def write_report_node(state: State) -> State:
    report = generate_model_response(state["performance_comparison"], prompts.WRITE_REPORT_PROMPT)
    return {"report": report}

def research_feedback_node(state: State) -> State:
    queries = model.with_structured_output(Queries).invoke(
        [
            SystemMessage(content=prompts.RESEARCH_FEEDBACK_PROMPT),
            HumanMessage(content=state["feedback"])
        ]
    )

    content = state["full_content"] or []

    for query in queries.queries:
        response = tavily.search(query=query, max_results=2)
        for result in response["results"]:
            content.append(result["content"])
    return {"full_content": content}

