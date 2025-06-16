from prompts import GATHER_FINANCIAL_PROMPT, ANALYZE_DATA_PROMPT, RESEARCH_COMPETITORS_PROMPT
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


