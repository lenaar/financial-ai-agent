import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from openai import OpenAI
from csv_data import get_csv_data
from model import generate_model_response
from state import State
from prompts import GATHER_FINANCIAL_PROMPT, ANALYZE_DATA_PROMPT
from agent import build_graph_agent
from memory import get_memory_saver, get_thread_config

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

model = ChatOpenAI(api_key=openai_api_key, model="gpt-4.1-nano", temperature=0.0)

def main():
    with get_memory_saver() as checkpointer:
        graph = build_graph_agent(checkpointer)
        initial_state = {
            "competitors_names": ["Apple", "Google", "Microsoft", "Amazon", "Tesla"],
            "csv_file": "data/financial_data.csv",
            "max_revisions": 3,
            "revisions": 1,
            "task": "analyze financial data and performance of the given company by reading the financial data and compare it with the competitors",
        }
        thread_config = get_thread_config()

        try:
            events = graph.stream(initial_state, thread_config)

            for event in events:
                print(event)
                print("--------------------------------")

        except Exception as e:
            print(f"Error in stream processing: {e}")

        return

if __name__ == "__main__":
    main()
    