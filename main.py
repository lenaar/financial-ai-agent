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
import streamlit as st

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

model = ChatOpenAI(api_key=openai_api_key, model="gpt-4.1-nano", temperature=0.0)

def main():
    st.set_page_config(page_title="Financial Analysis Agent", page_icon="📊", layout="centered")
    st.title("Financial Analysis Agent")
    st.write("This is a financial analysis agent that can analyze financial data and performance of a company by reading the financial data and compare it with the competitors")

    task = st.text_input("Enter the task", value="analyze financial data and performance of the given company by reading the financial data and compare it with the competitors")
    competitors_names = st.text_input("Enter the competitors names", value="Apple, Google")
    csv_file = st.file_uploader("Upload the financial data", type=["csv"])
    max_revisions = st.number_input("Enter the max revisions", value=3, min_value=1, max_value=10)
    initial_state = None

    if st.button("Start") and task and competitors_names and csv_file and max_revisions:
        csv_data = csv_file.getvalue().decode("utf-8")
        initial_state = {
            "task": task,
            "competitors_names": competitors_names.split(","),
            "csv_data": csv_data,
            "max_revisions": max_revisions
        }


        with get_memory_saver() as checkpointer:
            graph = build_graph_agent(checkpointer)

            thread_config = get_thread_config()

            try:
                events = graph.stream(initial_state, thread_config)

                for event in events:
                    st.write(event)
                    final_event = event
                    

                if final_event and "write_report" in final_event:
                    st.subheader("Final Report")
                    st.success("Report generated successfully", icon="✅")
                    st.write(final_event["write_report"])
                else:
                    st.warning(f"No final report was generated. Last event: {final_event}", icon="⚠️")

            except Exception as e:
                st.error(f"Error in stream processing: {e}", icon="🚨")

        return

if __name__ == "__main__":
    main()
    