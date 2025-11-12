# app/agents/report_generator_agent.py

"""
───────────────────────────────────────────────────────────────
📝 REPORT GENERATOR AGENT (FULL NARRATIVE VERSION)
───────────────────────────────────────────────────────────────
Purpose:
--------
Generates a comprehensive, professional report combining outputs 
from all analytical agents — Idea, Market, Financial, Competition, and SWOT.

It produces a detailed, context-rich document suitable for 
research reports, startup documentation, or hackathon submissions.
───────────────────────────────────────────────────────────────
"""

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.firecrawl import FirecrawlTools
from agno.tools.serpapi import SerpApiTools
from agno.tools.googlesearch import GoogleSearchTools

# Initialize Model
llm = OpenAIChat(id="gpt-4.1")

ReportGeneratorAgent = Agent(
    name="Report Generator Agent",
    description="""
        Synthesizes insights from idea understanding, market, financial, 
        competition, and SWOT analysis agents into a full-length report.
        The report is narrative, explanatory, and well-formatted.
    """,
    instructions="""

    Input:
        - Aggregated structured data from:
          * IdeaUnderstandingAgent
          * MarketResearchAgent
          * CompetitionAnalysisAgent
          * FinancialAnalysisAgent
          * SWOTAgent
    
    Task requirements (MANDATORY):
    1. Executive Summary (max 350–450 words) — describe or elaborate idea , proposed solution.
    2. Idea Overview — expand the idea into 4-5 paragraphs: problem, target users, product features, value proposition and unique differentiation.
    3. Market Research & Trends — 4-5 paragraphs describing market size (TAM/SAM/SOM where available), growth drivers, segmentation, user personas. Include at least one data point with source/link if available.
    4. Competition Analysis — produce a comparative analysis using the `competitors` list:
    - For each major competitor (at least top 3), provide a 2-paragraph profile: business model, pricing, strengths, weaknesses, market posture.
    - Generate a competitive table (Name | Category | Pricing | Key Strengths | Weaknesses | Evidence Link).
    - Write a 2-paragraph section "Competitive Implications" that states explicit strategic moves (pricing, features, partnerships) the product should pursue.
    5. Financial Analysis — produce a detailed section:
    - List key assumptions (price, conversion, growth, CAC, churn, gross margin).
    - Show a 3-year projection table (Revenue / COGS / Opex / EBITDA per year) and explain how numbers were derived.
    - Show unit economics (CAC, LTV, LTV/CAC, payback period) with explanation.
    - Provide a funding ask and use-of-funds breakdown (with percentages).
    - Include a short sensitivity analysis (best / base / worst cases) and explain key risk drivers.
    6. SWOT — expand each quadrant into 3–6 bullets point and write each point in about 50-60 words and explain how to convert weaknesses into mitigations and threats into contingency plans.
    7. Recommendations & Roadmap — 6–10 tactical recommendations prioritized by impact & effort, and a 6–12 month roadmap with milestones.
    8. Appendix — list all evidence links, datasets used, and a brief "How we estimated" note with formulas/assumptions.

    Formatting & style:
    - Use Markdown headers and subheaders (##, ###). Provide tables using Markdown.
    - Each main section must have **at least one paragraph per key sub-item** (e.g., each competitor gets 2 paragraphs).
    - Where external data is referenced, include the link inline as a citation.
    - If any upstream agent had missing data, explicitly state the gap, then provide a labeled inference with assumptions like: "(Assumption — described)".

    """,
    tools=[GoogleSearchTools(
        enable_google_search=True,
    ), SerpApiTools(), FirecrawlTools()],
    model=llm,
)
