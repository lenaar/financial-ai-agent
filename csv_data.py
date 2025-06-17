from state import State
import pandas as pd
from langchain_core.messages import SystemMessage, HumanMessage
from model import model
from io import StringIO

def get_csv_data(state: State) -> str:
    """
    Gather the financial data for the company from a csv file.
    """
    csv_data = state["csv_data"]
    data = pd.read_csv(StringIO(csv_data))
    
    data_str = data.to_string(index=False)

    content = (
        f"Here is the financial data for the chosen company: {data_str}"
    )

    print(f"CSV content: {content}")

    return content
