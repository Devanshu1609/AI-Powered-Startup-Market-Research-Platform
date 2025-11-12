from agents.Competition_Analysis_Agent import competition_analysis_agent
from agents.idea_understanding_agent import idea_understanding_agent
from agents.swot_agent import swot_agent
from agents.financial_analysis_agent import financial_analysis_agent
from agents.market_research_agent import market_research_agent
from agents.report_generator_agent import ReportGeneratorAgent

from agno.team import Team
from agno.models.openai import OpenAIChat
from agno.run.agent import RunOutput
from dotenv import load_dotenv

load_dotenv()

analysis_team = Team(
    name="StartupAnalysisTeam",
    description=(
        "A collaborative AI team that analyzes, validates, and documents startup business ideas. "
        "The team autonomously performs idea understanding, market research, competition study, "
        "financial analysis, and SWOT evaluation — then produces a detailed professional report."
    ),
    model=OpenAIChat(id="gpt-4o"),
    members=[
        idea_understanding_agent,
        market_research_agent,
        competition_analysis_agent,
        financial_analysis_agent,
        swot_agent,
        ReportGeneratorAgent
    ],
    instructions=[
        """
        You are an AI-driven startup intelligence system composed of multiple specialized agents.
        Your collective mission is to transform a user's startup idea into a complete, research-backed,
        and professionally formatted report.

        🧩 Core Objectives:
        - Understand and refine the user’s raw idea.
        - Conduct in-depth market research and identify key trends.
        - Analyze competitors and industry positioning.
        - Generate realistic financial projections and insights.
        - Perform SWOT analysis to identify internal and external factors.
        - Combine all analytical insights into a detailed, context-rich final report.

        🧠 Behavioral Rules:
        - Collaborate autonomously across all team members.
        - Exchange intermediate outputs internally; do not rely on user intervention.
        - Maintain structured, factual, and well-connected analysis throughout the process.
        - Ensure the final report is professional, elaborative, and formatted clearly in Markdown, PDF, or DOCX.
        - Highlight key opportunities, challenges, and recommendations.

        🎯 Final Deliverable:
        - Reort generate by the ReportGeneratorAgent that synthesizes all findings into a comprehensive document.
        """
    ],
    markdown=True,
    show_members_responses=True,
    debug_mode=True
)


if __name__ == "__main__":
    user_idea = """
    An AI-powered SaaS platform that helps small businesses automate bookkeeping,
    generate invoices, and forecast cash flow using predictive analytics.
    """

    print("\n🚀 Launching VentureIQ — Startup Analysis System...\n")
    response: RunOutput = analysis_team.run(user_idea, stream=False)
    print("\n✅ VentureIQ Team Completed Full Workflow:\n")
    print(response.content)
