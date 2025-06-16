from prompts import ANALYZE_COMPETITORS_PROMPT, COMPARE_PERFORMANCE_PROMPT
from langchain_core.messages import SystemMessage, HumanMessage
from model import model, generate_model_response
from typing import Dict, List
from state import State,Queries
from search_tool import tavily


def analyze_competitors_node(competitors_content: str, competitors_names: List[str]) -> List[str]:
    for competitor in competitors_names:
        queries = model.with_structured_output(Queries).invoke(
            [
                SystemMessage(content=ANALYZE_COMPETITORS_PROMPT),
                HumanMessage(content=competitor)
            ]
        )
    
    for query in queries.queries:
        research_content = tavily.search(query=query, max_results=2)
        for result in research_content["results"]:
            competitors_content.append(result["content"])


    return competitors_content



