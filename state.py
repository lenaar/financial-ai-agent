from typing import TypedDict, List
from pydantic import BaseModel

class State(TypedDict):
    analysis: str
    competitors: List[str]
    content: List[str]
    csv_file: str
    feedback: str
    financial_data: str
    max_revisions: int
    report: str
    revision_number: int
    task: str

class Queries(BaseModel):
    queries: List[str]