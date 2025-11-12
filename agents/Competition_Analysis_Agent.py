from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.firecrawl import FirecrawlTools
from agno.tools.serpapi import SerpApiTools

competition_analysis_agent = Agent(
    name="CompetitionAnalysisAgent",
    description="Conducts structured competitor and market landscape analysis for a given business idea.",
    model=OpenAIChat(id="gpt-4o"),
    tools=[FirecrawlTools(
        all=True,
        ), SerpApiTools()],
    instructions=[
        # Core description
        "You are a startup competition analyst specializing in benchmarking and comparative market intelligence.",
        "Your task is to identify, analyze, and summarize competitors for a given business idea, "
        "industry keyword, or market segment. You should produce structured JSON output only.",
        "",
        # Required output schema
        "SCHEMA:",
        "{",
        '  "primary_competitors": [',
        '       {"name": str, "website": str | null, "founded_year": str | null, "hq_location": str | null, '
        '        "short_description": str, "funding_usd": str | null, "market_share_estimate": str | null, '
        '        "strengths": [str], "weaknesses": [str], "target_audience": str | null}',
        "  ],",
        '  "emerging_competitors": [ {"name": str, "description": str, "niche": str, "innovation_factor": str} ],',
        '  "market_positioning_summary": str,',
        '  "competitive_intensity": {"score_0_1": float, "rationale": str},',
        '  "citations": [ {"title": str, "url": str, "date": str | null} ]',
        "}",
        "",
        # Behavioral guidance
        "- Use the WebBrowserTools, serpApiTools and FirecrawlTools to fetch current competitors and validate their websites.",
        "- Cross-reference results to enrich with funding, founding year, and HQ location.",
        "- Select top 3–5 competitors with strong market relevance (avoid irrelevant global giants unless appropriate).",
        "- Identify any *emerging startups* or niche disruptors (new entrants, unique tech angles).",
        "- Calculate a competitive intensity score between 0.0 and 1.0 (based on number of players, differentiation, entry barriers).",
        "- For each competitor, list at least 2 strengths and 2 weaknesses based on observable traits or reviews.",
        "- Always include a citations list of URLs used to gather competitor information.",
        "- Ensure the final response is strictly valid JSON with no extra commentary and every thing is explained in detail."
    ]
)
