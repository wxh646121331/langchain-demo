from agent.my_llm import llm
from agent.tool.web_search_tool import web_search
from agent.tool.date_tool import get_date
from langchain.agents import create_agent


def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"


agent = create_agent(
    llm,
    tools = [get_date, web_search],
    system_prompt = "尽你所能回答用户的问题"
)
