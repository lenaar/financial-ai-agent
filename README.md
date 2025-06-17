# Financial Analysis AI Agent

An intelligent agent that analyzes financial data, compares performance with competitors, and generates comprehensive reports using LangGraph and LangChain.

## Features

- Financial data analysis from CSV files
- Competitor performance comparison
- Automated research using Tavily search
- Interactive feedback loop for report refinement
- Beautiful Streamlit interface
- Comprehensive test suite

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/financial-ai-agent.git
cd financial-ai-agent
```

2. Create and activate a virtual environment

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Set up environment variables:
   - Copy `.env.example` to `.env`
   - Add your API keys:
     ```
     OPENAI_API_KEY=your_openai_api_key
     TAVILY_API_KEY=your_tavily_api_key
     ```

## Usage

1. Start the application:

```bash
streamlit run main.py
```

2. The application will open in your default web browser.

3. Input your analysis requirements:

   - Enter the task description
   - Specify competitor names
   - Upload your financial data CSV file
   - Set the maximum number of revisions

4. Click "Start" to begin the analysis.

## CSV File Format

The application expects financial data in CSV format. Here's an example structure:

```csv
year,revenue,cost_of_goods_sold,operating_expenses,net_income
2019,1000000,600000,250000,150000
2020,1200000,720000,280000,200000
2021,1500000,900000,300000,300000
2022,1800000,1080000,350000,370000
2023,2100000,1260000,400000,440000
2024,2500000,1500000,450000,550000
```

## Application Interface

### Stage 1: Input

![Input Stage](images/frontend_1.jpg)
The initial interface where you can:

- Enter your analysis task
- Specify competitors
- Upload financial data
- Set revision limits

### Stage 2: Processing

![Processing Stage](images/frontend_processing.jpg)
The agent will:

- Analyze financial data
- Research competitors
- Compare performance
- Generate initial report

### Stage 3: Final Report

![Final Report](images/frontend_final_report.jpg)
The comprehensive report includes:

- Financial analysis
- Competitor comparison
- Performance metrics
- Strategic recommendations

## Testing

Run the test suite:

```bash
pytest
```

Run tests with coverage report:

```bash
pytest --cov
```

## Project Structure

```
financial-ai-agent/
├── agent.py              # LangGraph agent definition and build
├── csv_data.py          # CSV data processing
├── data/                # Example data
├── images/              # Screenshots
├── main.py             # Streamlit application
├── memory.py           # Memory and thread management
├── model.py            # LLM integration
├── nodes.py            # Agent nodes
├── prompts.py          # System prompts
├── requirements.txt    # Dependencies
├── search_tool.py      # Tavily search integration
├── state.py            # State definitions
└── tests/              # Test suite
```
