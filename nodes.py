from prompts import GATHER_FINANCIAL_PROMPT, ANALYZE_DATA_PROMPT, ANALYZE_COMPETITORS_PROMPT
from langchain_core.messages import SystemMessage, HumanMessage
from model import model
from typing import Dict, List
from state import Queries
from search_tool import tavily

def message_node(content: str, prompt: str) -> str:
    messages = [
        SystemMessage(content=prompt),
        HumanMessage(content=content)
    ]

    data = model.invoke(messages)

    return data.content


def analyze_competitors_node(content: str, competitors: List[str]) -> str:
    for competitor in competitors:
        queries = model.with_structured_output(Queries).invoke(
            [
                SystemMessage(content=ANALYZE_COMPETITORS_PROMPT),
                HumanMessage(content=competitor)
            ]
        )
    
    for query in queries.queries:
        research_content = tavily.search(query=query, max_results=2)
        for result in research_content["results"]:
            content.append(result["content"])


    return content

