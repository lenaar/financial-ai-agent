from typing import TypedDict, List
from pydantic import BaseModel

class State(TypedDict):
    competitors_names: List[str]
    csv_file: str
    feedback: str
    financial_analysis: str
    financial_data: str
    full_content: List[str]
    max_revisions: int
    performance_comparison: str
    report: str
    revisions: int
    task: str

class Queries(BaseModel):
    queries: List[str]