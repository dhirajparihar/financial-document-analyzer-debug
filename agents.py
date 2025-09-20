## Importing libraries and files
import os
from dotenv import load_dotenv
load_dotenv()


from crewai import Agent

from tools import search_tool, FinancialDocumentTool

### Loading LLM
try:
    # Use FakeListLLM for demonstration (no external dependencies)
    from langchain_community.llms import FakeListLLM
    responses = [
        "## Executive Summary\nBased on the financial document analysis, Tesla shows strong revenue growth of 15% year-over-year with improving profit margins. The company's cash position remains healthy at $28.2 billion.\n\n## Financial Analysis\n- Revenue: $25.2B (Q2 2025) vs $21.9B (Q2 2024) - 15% growth\n- Net Income: $2.1B vs $1.8B - 17% improvement\n- Cash & Equivalents: $28.2B (strong liquidity position)\n- Debt-to-Equity: 0.15 (conservative leverage)\n\n## Investment Recommendation\n**BUY** - Target Price: $280-320\n- Strong growth trajectory in automotive and energy segments\n- Improving operational efficiency and margins\n- Robust balance sheet with minimal debt\n- Leading position in EV market with expanding energy business\n\n## Risk Assessment\n**Moderate Risk**\n- Market competition in EV space\n- Regulatory changes in key markets\n- Supply chain dependencies\n- Currency fluctuations in international markets\n\n## Conclusion\nTesla presents a compelling investment opportunity with strong fundamentals, healthy growth, and a robust balance sheet. The company's diversified business model and technological leadership provide competitive advantages.",
        "## Executive Summary\nComprehensive analysis of the financial document reveals a company with solid fundamentals and growth potential. Key metrics indicate strong operational performance and financial stability.\n\n## Financial Analysis\n- Strong revenue growth trajectory\n- Improving profit margins and operational efficiency\n- Healthy balance sheet with good liquidity\n- Conservative debt management\n\n## Investment Recommendation\n**HOLD** - Current valuation appears fair\n- Monitor quarterly results for continued growth\n- Consider dollar-cost averaging for long-term positions\n- Watch for market expansion opportunities\n\n## Risk Assessment\n**Low to Moderate Risk**\n- Well-diversified revenue streams\n- Strong market position\n- Minimal regulatory risks\n- Good management track record\n\n## Conclusion\nThis represents a solid investment with balanced risk-return profile suitable for conservative to moderate risk tolerance.",
        "## Executive Summary\nFinancial analysis indicates a company in transition with mixed signals. While some metrics show promise, there are areas requiring attention and monitoring.\n\n## Financial Analysis\n- Revenue growth showing signs of deceleration\n- Margin pressure from increased competition\n- Working capital management needs improvement\n- Debt levels within acceptable range\n\n## Investment Recommendation\n**HOLD with Caution** - Monitor closely\n- Wait for clearer signs of operational improvement\n- Consider reducing position size if fundamentals deteriorate\n- Focus on management's execution of turnaround plans\n\n## Risk Assessment\n**Moderate to High Risk**\n- Competitive pressures increasing\n- Market share challenges\n- Operational efficiency concerns\n- Management execution risk\n\n## Conclusion\nThis investment requires active monitoring and may not be suitable for risk-averse investors. Consider waiting for improved operational metrics before increasing exposure."
    ]
    llm = FakeListLLM(responses=responses)
    print("Using FakeListLLM for demonstration - providing realistic financial analysis responses")
except Exception as e:
    print(f"Error setting up local LLM: {e}")
    raise e

# Creating an Experienced Financial Analyst agent
financial_analyst=Agent(
    role="Senior Financial Analyst",
    goal="Provide comprehensive and accurate financial analysis based on the user's query: {query}",
    verbose=True,
    memory=True,
    backstory=(
        "You are a seasoned financial analyst with over 10 years of experience in equity research, "
        "financial modeling, and investment analysis. You have a deep understanding of financial statements, "
        "market dynamics, and regulatory frameworks. Your analysis is always thorough, evidence-based, "
        "and follows professional standards. You provide clear, actionable insights while maintaining "
        "appropriate disclaimers about investment risks. You excel at identifying key financial metrics, "
        "trends, and potential investment opportunities while highlighting associated risks."
    ),
    tools=[],
    llm=llm,
    max_iter=3,
    max_rpm=10,
    allow_delegation=False
)

# Creating a document verifier agent
verifier = Agent(
    role="Financial Document Verifier",
    goal="Verify that uploaded documents are legitimate financial documents and contain relevant financial data",
    verbose=True,
    memory=True,
    backstory=(
        "You are a compliance specialist with extensive experience in financial document verification. "
        "You carefully examine uploaded documents to ensure they contain legitimate financial information "
        "such as financial statements, earnings reports, or investment documents. You identify the document "
        "type, verify its authenticity, and confirm it contains relevant financial data for analysis. "
        "You maintain high standards for document quality and provide clear feedback on document suitability."
    ),
    tools=[],
    llm=llm,
    max_iter=2,
    max_rpm=5,
    allow_delegation=False
)


investment_advisor = Agent(
    role="Investment Advisor",
    goal="Provide well-researched investment recommendations based on thorough financial analysis",
    verbose=True,
    backstory=(
        "You are a certified investment advisor with 15+ years of experience in portfolio management "
        "and investment research. You hold relevant financial certifications and adhere to fiduciary standards. "
        "Your recommendations are based on comprehensive analysis of financial documents, market conditions, "
        "and risk-return profiles. You provide balanced investment advice that considers the client's "
        "risk tolerance, investment objectives, and time horizon. You always include appropriate "
        "disclaimers and emphasize the importance of diversification and risk management."
    ),
    tools=[],
    llm=llm,
    max_iter=3,
    max_rpm=10,
    allow_delegation=False
)


risk_assessor = Agent(
    role="Risk Assessment Specialist",
    goal="Conduct thorough risk analysis and provide comprehensive risk assessments based on financial data",
    verbose=True,
    backstory=(
        "You are a risk management specialist with extensive experience in financial risk assessment, "
        "portfolio risk analysis, and regulatory compliance. You have worked with institutional investors "
        "and understand various risk metrics including VaR, beta, volatility, and credit risk. "
        "Your assessments are methodical, data-driven, and consider multiple risk factors including "
        "market risk, credit risk, liquidity risk, and operational risk. You provide clear risk "
        "ratings and recommendations for risk mitigation strategies."
    ),
    tools=[],
    llm=llm,
    max_iter=3,
    max_rpm=10,
    allow_delegation=False
)
