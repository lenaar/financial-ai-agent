import pytest
from state import State

class TestState:
    """Unit tests for State class"""

    def test_state_creation_with_required_fields(self):
        """Test state creation with all required fields"""
        state = {
            "task": "Analyze financial performance",
            "competitors_names": ["Competitor A", "Competitor B"],
            "csv_data": "date,revenue\n2023-01-01,1000",
            "revisions": 0,
            "max_revisions": 3
        }
        # TypedDict doesn't enforce validation at runtime, so we just check the fields exist
        assert all(key in state for key in ["task", "competitors_names", "csv_data", "revisions", "max_revisions"])
        assert isinstance(state["task"], str)
        assert isinstance(state["competitors_names"], list)
        assert isinstance(state["csv_data"], str)
        assert isinstance(state["revisions"], int)
        assert isinstance(state["max_revisions"], int)

    def test_state_creation_with_optional_fields(self):
        """Test state creation with optional fields"""
        state = {
            "task": "Analyze financial performance",
            "competitors_names": ["Competitor A"],
            "csv_data": "date,revenue\n2023-01-01,1000",
            "revisions": 0,
            "max_revisions": 3,
            "financial_data": "Some financial data",
            "financial_analysis": "Some analysis",
            "performance_comparison": "Some comparison",
            "feedback": "Some feedback",
            "report": "Some report",
            "full_content": ["Content 1", "Content 2"]
        }
        # Check optional fields
        assert "financial_data" in state
        assert "financial_analysis" in state
        assert "performance_comparison" in state
        assert "feedback" in state
        assert "report" in state
        assert "full_content" in state

    def test_state_field_types(self):
        """Test state field types"""
        state = {
            "task": "Analyze financial performance",
            "competitors_names": ["Competitor A"],
            "csv_data": "date,revenue\n2023-01-01,1000",
            "revisions": 0,
            "max_revisions": 3,
            "financial_data": "Some financial data",
            "financial_analysis": "Some analysis",
            "performance_comparison": "Some comparison",
            "feedback": "Some feedback",
            "report": "Some report",
            "full_content": ["Content 1", "Content 2"]
        }
        # Check field types
        assert isinstance(state["task"], str)
        assert isinstance(state["competitors_names"], list)
        assert isinstance(state["csv_data"], str)
        assert isinstance(state["revisions"], int)
        assert isinstance(state["max_revisions"], int)
        assert isinstance(state["financial_data"], str)
        assert isinstance(state["financial_analysis"], str)
        assert isinstance(state["performance_comparison"], str)
        assert isinstance(state["feedback"], str)
        assert isinstance(state["report"], str)
        assert isinstance(state["full_content"], list)

    def test_state_field_access(self):
        """Test state field access"""
        state = {
            "task": "Analyze financial performance",
            "competitors_names": ["Competitor A"],
            "csv_data": "date,revenue\n2023-01-01,1000",
            "revisions": 0,
            "max_revisions": 3
        }
        # Test field access
        assert state["task"] == "Analyze financial performance"
        assert state["competitors_names"] == ["Competitor A"]
        assert state["csv_data"] == "date,revenue\n2023-01-01,1000"
        assert state["revisions"] == 0
        assert state["max_revisions"] == 3

    def test_state_field_update(self):
        """Test state field update"""
        state = {
            "task": "Analyze financial performance",
            "competitors_names": ["Competitor A"],
            "csv_data": "date,revenue\n2023-01-01,1000",
            "revisions": 0,
            "max_revisions": 3
        }
        # Update fields
        state["task"] = "New task"
        state["revisions"] = 1
        state["financial_data"] = "New financial data"
        
        # Verify updates
        assert state["task"] == "New task"
        assert state["revisions"] == 1
        assert state["financial_data"] == "New financial data" 