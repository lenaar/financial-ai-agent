import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from openai import OpenAI
from csv_data import get_csv_data
from model import generate_model_response
from state import State
from prompts import GATHER_FINANCIAL_PROMPT, ANALYZE_DATA_PROMPT
from agent import build_graph_agent

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

model = ChatOpenAI(api_key=openai_api_key, model="gpt-4.1-nano", temperature=0.0)

def main():
    graph = build_graph_agent()
    result = graph.invoke({
        "competitors_names": [],
        "competitors_content": [],
        "csv_file": "data/financial_data.csv",
        "feedback": "",
        "financial_analysis": "",
        "financial_data": "",
        "max_revisions": 3,
        "report": "",
        "revisions": 0,
        "task": "analyze financial data",
    })
    print("Final result:", result)
    return graph

if __name__ == "__main__":
    main()
    