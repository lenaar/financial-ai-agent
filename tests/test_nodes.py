import pytest
from unittest.mock import patch, MagicMock
from nodes import gather_financial_data_node, analyze_financial_data_node
from state import State

class TestGatherFinancialDataNode:
    """Tests for gather_financial_data_node behavior"""

    @patch('nodes.get_csv_data')
    @patch('nodes.generate_model_response')
    def test_should_process_csv_and_generate_analysis(self, mock_generate_response, mock_get_csv):
        """Given CSV data, should process it and generate financial analysis"""
        # Arrange
        state = {
            "csv_data": "date,revenue\n2023-01-01,1000",
            "task": "Analyze performance"
        }
        mock_get_csv.return_value = "Processed CSV data"
        mock_generate_response.return_value = "Financial analysis result"
        
        # Act
        result = gather_financial_data_node(state)
        
        # Assert
        mock_get_csv.assert_called_once_with(state)
        mock_generate_response.assert_called_once()
        assert result["financial_data"] == "Financial analysis result"
        assert result["task"] == "Analyze performance"  # Original state preserved

    @patch('nodes.get_csv_data')
    @patch('nodes.generate_model_response')
    def test_should_handle_empty_csv(self, mock_generate_response, mock_get_csv):
        """Given empty CSV, should handle it gracefully"""
        # Arrange
        state = {
            "csv_data": "",
            "task": "Analyze performance"
        }
        mock_get_csv.return_value = ""
        mock_generate_response.return_value = "No data available"
        
        # Act
        result = gather_financial_data_node(state)
        
        # Assert
        mock_get_csv.assert_called_once_with(state)
        mock_generate_response.assert_called_once()
        assert result["financial_data"] == "No data available"
        assert result["task"] == "Analyze performance"  # Original state preserved

    @patch('nodes.get_csv_data')
    @patch('nodes.generate_model_response')
    def test_should_preserve_existing_state(self, mock_generate_response, mock_get_csv):
        """Should preserve existing state while adding financial data"""
        # Arrange
        state = {
            "csv_data": "date,revenue\n2023-01-01,1000",
            "task": "Analyze performance",
            "existing_field": "value"
        }
        mock_get_csv.return_value = "Processed CSV data"
        mock_generate_response.return_value = "Financial analysis result"
        
        # Act
        result = gather_financial_data_node(state)
        
        # Assert
        assert result["existing_field"] == "value"
        assert result["financial_data"] == "Financial analysis result"
        assert result["task"] == "Analyze performance"

    @patch('nodes.get_csv_data')
    def test_should_handle_csv_processing_error(self, mock_get_csv):
        """Should handle CSV processing errors gracefully"""
        # Arrange
        state = {
            "csv_data": "invalid,csv",
            "task": "Analyze performance"
        }
        mock_get_csv.side_effect = Exception("CSV processing error")
        
        # Act/Assert
        with pytest.raises(Exception) as exc_info:
            gather_financial_data_node(state)
        assert str(exc_info.value) == "CSV processing error"

    @patch('nodes.get_csv_data')
    @patch('nodes.generate_model_response')
    def test_should_handle_model_error(self, mock_generate_response, mock_get_csv):
        """Should handle model errors gracefully"""
        # Arrange
        state = {
            "csv_data": "date,revenue\n2023-01-01,1000",
            "task": "Analyze performance"
        }
        mock_get_csv.return_value = "Processed CSV data"
        mock_generate_response.side_effect = Exception("Model error")
        
        # Act/Assert
        with pytest.raises(Exception) as exc_info:
            gather_financial_data_node(state)
        assert str(exc_info.value) == "Model error"

class TestAnalyzeFinancialDataNode:
    """Tests for analyze_financial_data_node behavior"""

    @patch('nodes.generate_model_response')
    def test_should_handle_model_error(self, mock_generate_response):
        state = {
            "financial_data": "Some financial data",
            "task": "Analyze performance"
        }
        mock_generate_response.side_effect = Exception("Model error")
        with pytest.raises(Exception) as exc_info:
            analyze_financial_data_node(state)
        assert str(exc_info.value) == "Model error"

    def test_should_handle_missing_financial_data(self):
        state = {"task": "Analyze performance"}
        with pytest.raises(KeyError):
            analyze_financial_data_node(state)
