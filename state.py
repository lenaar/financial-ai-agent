from typing import TypedDict, List
from pydantic import BaseModel

class State(TypedDict):
    competitors_names: List[str]
    competitors_content: List[str]
    csv_file: str
    feedback: str
    financial_analysis: str
    financial_data: str
    max_revisions: int
    report: str
    revisions: int
    task: str

class Queries(BaseModel):
    queries: List[str]