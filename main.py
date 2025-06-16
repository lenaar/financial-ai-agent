import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from openai import OpenAI
from csv_data import get_csv_data
from nodes import gather_financial_data_node

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

model = ChatOpenAI(api_key=openai_api_key, model="gpt-4.1-nano", temperature=0.0)

def main():
    content = get_csv_data()
    financial_content = gather_financial_data_node(content)
    print(financial_content)

if __name__ == "__main__":
    main()
    