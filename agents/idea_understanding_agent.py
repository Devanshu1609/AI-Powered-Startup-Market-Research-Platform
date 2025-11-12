from agno.agent import Agent
from agno.models.openai import OpenAIChat
from dotenv import load_dotenv
from agno.tools.googlesearch import GoogleSearchTools
load_dotenv()

idea_understanding_agent = Agent(
    name="IdeaUnderstandingAgent",
    description="Analyzes and refines business ideas provided by entrepreneurs.",
    model=OpenAIChat(id="gpt-4o"),
    tools=[GoogleSearchTools(
        enable_google_search=True,
    ),],
    instructions=[
        "You are a startup idea analyst agent who specializes in evaluating new business ideas.",
        "Given a short idea description, your task is to extract key business insights:",
        "- Problem being solved",
        "- Target audience or customer segment",
        "- Unique value proposition (UVP)",
        "- Core product or service description",
        "- Revenue model (if inferable)",
        "- Keywords and industry classification",
        "Respond in JSON format for structured parsing.",
        "Keep your output detailed and professional."
    ],
    markdown=True,
)

