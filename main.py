import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from openai import OpenAI
from csv_data import get_csv_data
from nodes import message_node
from state import State
from prompts import GATHER_FINANCIAL_PROMPT, ANALYZE_DATA_PROMPT

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

model = ChatOpenAI(api_key=openai_api_key, model="gpt-4.1-nano", temperature=0.0)

def main():
    state = State(
        analysis="",
        competitors=[],
        content=[],
        csv_file="data/financial_data.csv",
        feedback="",
        financial_data="",
        max_revisions=3,
        report="",
        revision_number=0,
        task="analyze financial data"
    )
    content = get_csv_data(state)
    financial_content = message_node(content, GATHER_FINANCIAL_PROMPT)
    print(financial_content)

    analysis = message_node(financial_content, ANALYZE_DATA_PROMPT)
    print(analysis)

if __name__ == "__main__":
    main()
    