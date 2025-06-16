from prompts import GATHER_FINANCIAL_PROMPT
from langchain_core.messages import SystemMessage, HumanMessage
from model import model
from typing import Dict, List

def gather_financial_data_node(content: str) -> Dict[str, List[str]]:

    messages = [
        SystemMessage(content=GATHER_FINANCIAL_PROMPT),
        HumanMessage(content=content)
    ]

    financial_data = model.invoke(messages)

    return financial_data.content

