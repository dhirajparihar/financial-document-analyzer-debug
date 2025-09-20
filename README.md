# Financial Document Analyzer

## Project Overview
A comprehensive financial document analysis system that processes corporate reports, financial statements, and investment documents using AI-powered analysis agents built with CrewAI. The system provides professional financial analysis, investment recommendations, and risk assessments.

## 🐛 Bugs Found and Fixed

### Deterministic Bugs Fixed:

1. **Circular Reference in LLM Initialization** (`agents.py:12`)
   - **Bug**: `llm = llm` created a circular reference causing NameError
   - **Fix**: Properly imported and initialized ChatOpenAI with correct model configuration

2. **Missing PDF Processing Library** (`tools.py:24`)
   - **Bug**: Missing import for `Pdf` class causing NameError
   - **Fix**: Added `pypdf` library and updated to use `PdfReader` class

3. **Incorrect CrewAI Kickoff Parameters** (`main.py:20`)
   - **Bug**: `kickoff({'query': query})` used wrong parameter format
   - **Fix**: Changed to `kickoff(inputs={'query': query, 'file_path': file_path})`

4. **Unused Import** (`task.py:4`)
   - **Bug**: Importing unused `verifier` agent
   - **Fix**: Removed unused import to clean up dependencies

5. **Async Method Definition** (`tools.py:14`)
   - **Bug**: Method defined as async but not properly handled
   - **Fix**: Changed to static method with proper error handling

6. **Missing Dependencies** (`requirements.txt`)
   - **Bug**: Missing essential packages for the application
   - **Fix**: Added `uvicorn`, `python-multipart`, `python-dotenv`, `pypdf`, and `langchain-openai`

7. **Incorrect Import Paths**
   - **Bug**: Wrong import paths for CrewAI components
   - **Fix**: Updated to use correct import syntax for CrewAI 0.130.0

### Inefficient Prompts Fixed:

1. **Unprofessional Agent Descriptions**
   - **Issue**: All agent prompts contained inappropriate, unprofessional content encouraging unethical behavior
   - **Fix**: Rewrote all agent roles, goals, and backstories to be professional, ethical, and compliant with financial industry standards

2. **Vague Task Descriptions**
   - **Issue**: Task descriptions were unclear and encouraged hallucination
   - **Fix**: Created structured, specific task descriptions with clear expected outputs

3. **Poor Expected Output Format**
   - **Issue**: Expected outputs were unstructured and encouraged misinformation
   - **Fix**: Designed comprehensive, professional report templates with clear sections

4. **Inappropriate Financial Advice**
   - **Issue**: Prompts encouraged providing harmful or misleading financial advice
   - **Fix**: Implemented proper disclaimers and professional standards for financial analysis

## 🚀 Setup and Usage Instructions

### Prerequisites
- Python 3.8 or higher
- OpenAI API key
- (Optional) Serper API key for web search functionality

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/financial-document-analyzer-debug.git
   cd financial-document-analyzer-debug
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   ```bash
   # Copy the example environment file
   cp env_example.txt .env
   
   # Edit .env file and add your API keys
   OPENAI_API_KEY=your_openai_api_key_here
   SERPER_API_KEY=your_serper_api_key_here  # Optional
   OPENAI_MODEL=gpt-3.5-turbo  # Optional
   ```

### Usage

#### Option 1: FastAPI Web Server
```bash
python main.py
```
The server will start on `http://localhost:8000`

#### Option 2: Direct Python Usage
```python
from main import run_crew

# Analyze a financial document
result = run_crew(
    query="Analyze Tesla's financial performance and provide investment recommendations",
    file_path="data/TSLA-Q2-2025-Update.pdf"
)
print(result)
```

### Sample Document
The system comes with Tesla's Q2 2025 financial update (`data/TSLA-Q2-2025-Update.pdf`) for testing purposes.

## 📚 API Documentation

### Endpoints

#### Health Check
- **GET** `/`
- **Description**: Check if the API is running
- **Response**: `{"message": "Financial Document Analyzer API is running"}`

#### Document Analysis
- **POST** `/analyze`
- **Description**: Upload and analyze a financial document
- **Parameters**:
  - `file` (UploadFile): PDF file to analyze
  - `query` (string, optional): Analysis query (default: "Analyze this financial document for investment insights")
- **Response**:
  ```json
  {
    "status": "success",
    "query": "user query",
    "analysis": "detailed analysis report",
    "file_processed": "filename.pdf"
  }
  ```

### Example Usage with curl
```bash
curl -X POST "http://localhost:8000/analyze" \
  -F "file=@your_document.pdf" \
  -F "query=Analyze this company's financial health and provide investment recommendations"
```

## 🏗️ System Architecture

### Components

1. **Agents** (`agents.py`)
   - `financial_analyst`: Senior financial analyst for comprehensive analysis
   - `verifier`: Document verification specialist
   - `investment_advisor`: Investment recommendation specialist
   - `risk_assessor`: Risk analysis specialist

2. **Tools** (`tools.py`)
   - `FinancialDocumentTool`: PDF reading and text extraction
   - `SerperDevTool`: Web search capabilities
   - `InvestmentTool`: Investment analysis utilities
   - `RiskTool`: Risk assessment utilities

3. **Tasks** (`task.py`)
   - `analyze_financial_document`: Main analysis task
   - `investment_analysis`: Investment-focused analysis
   - `risk_assessment`: Risk-focused analysis
   - `verification`: Document verification task

4. **API** (`main.py`)
   - FastAPI web server
   - File upload handling
   - Crew orchestration

### Analysis Output Structure

The system provides structured financial analysis reports including:

- **Executive Summary**: Key findings and recommendations
- **Financial Analysis**: Revenue, profitability, balance sheet, cash flow
- **Key Financial Ratios**: Liquidity, profitability, leverage, efficiency ratios
- **Investment Recommendations**: Buy/Hold/Sell with rationale and price targets
- **Risk Assessment**: Market, credit, liquidity, operational risks
- **Conclusion**: Summary and next steps

## 🔧 Configuration

### Environment Variables
- `OPENAI_API_KEY`: Required for AI analysis
- `SERPER_API_KEY`: Optional for web search functionality
- `OPENAI_MODEL`: Optional model selection (default: gpt-3.5-turbo)

### Model Configuration
The system uses OpenAI's GPT models with the following settings:
- Temperature: 0.1 (for consistent, factual analysis)
- Max iterations: 3 (for thorough analysis)
- Max RPM: 10 (rate limiting)

## 🧪 Testing

The system has been thoroughly tested and all bugs have been resolved. Key test areas include:
- Module imports and dependencies
- PDF reading functionality
- Agent creation and configuration
- Task definition and execution
- API endpoint functionality

## 🚀 Getting Started on GitHub

### Initial Setup

1. **Initialize Git Repository**
   ```bash
   git init
   git add .
   git commit -m "Initial commit: Financial Document Analyzer"
   ```

2. **Create GitHub Repository**
   - Go to [GitHub](https://github.com) and create a new repository
   - Name it `financial-document-analyzer-debug` (or your preferred name)
   - Don't initialize with README, .gitignore, or license (we already have these)

3. **Connect Local Repository to GitHub**
   ```bash
   git remote add origin https://github.com/yourusername/financial-document-analyzer-debug.git
   git branch -M main
   git push -u origin main
   ```

### Development Workflow

1. **Make Changes**
   ```bash
   # Make your changes to the code
   git add .
   git commit -m "Description of changes"
   git push origin main
   ```

2. **Create Releases**
   - Go to GitHub repository → Releases → Create a new release
   - Tag version (e.g., v1.0.0)
   - Add release notes describing features and fixes

### Repository Structure
```
financial-document-analyzer-debug/
├── agents.py              # AI agents configuration
├── main.py                # FastAPI web server
├── task.py                # Analysis tasks definition
├── tools.py               # Utility tools and PDF processing
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── .gitignore            # Git ignore rules
├── env_example.txt       # Environment variables template
├── data/                 # Sample financial documents
│   └── TSLA-Q2-2025-Update.pdf
└── outputs/              # Analysis results (gitignored)
```

### Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### License

This project is open source and available under the [MIT License](LICENSE).

### Support

For support, email your-email@example.com or create an issue in the GitHub repository.

