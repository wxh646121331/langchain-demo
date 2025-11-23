from agent.my_llm import llm
from langchain.agents import create_agent


def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"


agent = create_agent(
    llm,
    tools = [get_weather],
    system_prompt = "你是一个天气预报员，请根据用户的问题预报天气"
)
