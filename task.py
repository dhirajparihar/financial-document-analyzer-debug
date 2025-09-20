## Importing libraries and files
from crewai import Task

from agents import financial_analyst
from tools import search_tool, FinancialDocumentTool

## Creating a task to help solve user's query
analyze_financial_document = Task(
    description="""Analyze the financial document at {file_path} thoroughly based on the user's query: {query}

Your analysis should include:
1. Document overview and key financial metrics
2. Revenue and profitability analysis
3. Balance sheet strength assessment
4. Cash flow analysis
5. Key ratios and financial health indicators
6. Industry comparison and market positioning
7. Investment thesis and recommendations
8. Risk factors and considerations

Use the FinancialDocumentTool to read and extract data from the uploaded document. 
Provide a comprehensive, professional analysis that addresses the user's specific query.""",

    expected_output="""A structured financial analysis report containing:

## Executive Summary
- Key findings and recommendations
- Overall investment thesis

## Financial Analysis
- Revenue and growth trends
- Profitability metrics
- Balance sheet analysis
- Cash flow assessment

## Key Financial Ratios
- Liquidity ratios
- Profitability ratios
- Leverage ratios
- Efficiency ratios

## Investment Recommendations
- Buy/Hold/Sell recommendation with rationale
- Target price or valuation range
- Key catalysts and risks

## Risk Assessment
- Primary risk factors
- Mitigation strategies
- Regulatory considerations

## Conclusion
- Summary of key points
- Next steps for investors""",

    agent=financial_analyst,
    tools=[],
    async_execution=False,
)

## Creating an investment analysis task
investment_analysis = Task(
    description="""Conduct a comprehensive investment analysis based on the financial document and user query: {query}

Focus on:
1. Fundamental analysis of the company's financial health
2. Valuation metrics and price targets
3. Investment thesis development
4. Portfolio allocation recommendations
5. Risk-return profile assessment
6. Market timing considerations

Provide evidence-based investment recommendations that align with the company's financial performance and market conditions.""",

    expected_output="""A detailed investment analysis report including:

## Investment Thesis
- Core investment argument
- Key value drivers
- Competitive advantages

## Valuation Analysis
- DCF model results
- Comparable company analysis
- Price target and rationale

## Investment Recommendations
- Buy/Hold/Sell recommendation
- Position sizing guidance
- Entry and exit strategies

## Portfolio Considerations
- Risk-return profile
- Correlation with existing holdings
- Sector allocation impact

## Key Risks
- Downside scenarios
- Risk mitigation strategies
- Monitoring requirements""",

    agent=financial_analyst,
    tools=[],
    async_execution=False,
)

## Creating a risk assessment task
risk_assessment = Task(
    description="""Conduct a comprehensive risk assessment based on the financial document and user query: {query}

Analyze the following risk categories:
1. Market risk and volatility exposure
2. Credit risk and debt analysis
3. Liquidity risk assessment
4. Operational risk factors
5. Regulatory and compliance risks
6. Industry-specific risks
7. ESG and sustainability risks

Provide quantitative risk metrics where possible and qualitative assessments for complex risks.""",

    expected_output="""A comprehensive risk assessment report including:

## Risk Overview
- Overall risk rating (Low/Medium/High)
- Risk summary and key concerns

## Market Risk Analysis
- Beta and volatility metrics
- Market correlation analysis
- Sector risk exposure

## Credit Risk Assessment
- Debt-to-equity ratios
- Interest coverage ratios
- Credit rating considerations

## Liquidity Risk
- Current and quick ratios
- Cash flow adequacy
- Working capital analysis

## Operational Risks
- Key operational risk factors
- Management quality assessment
- Business model risks

## Risk Mitigation Strategies
- Recommended hedging strategies
- Portfolio diversification advice
- Risk monitoring protocols

## Risk Monitoring
- Key risk indicators to track
- Reporting frequency recommendations
- Escalation procedures""",

    agent=financial_analyst,
    tools=[],
    async_execution=False,
)

    
verification = Task(
    description="""Verify that the uploaded document is a legitimate financial document suitable for analysis.

Check for:
1. Document type and format validation
2. Presence of financial statements or data
3. Document authenticity and completeness
4. Relevance to financial analysis
5. Data quality and readability

Provide clear feedback on document suitability and any issues that may affect analysis quality.""",

    expected_output="""A document verification report including:

## Document Validation
- Document type confirmation
- Format and structure assessment
- File integrity check

## Content Analysis
- Financial data presence
- Document completeness
- Data quality assessment

## Suitability Assessment
- Analysis readiness
- Potential limitations
- Recommendations for improvement

## Next Steps
- Proceed with analysis or request new document
- Specific areas of focus for analysis
- Expected analysis outcomes""",

    agent=financial_analyst,
    tools=[],
    async_execution=False
)