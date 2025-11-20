import langchain_openai
from langchain_openai import ChatOpenAI
from langchain_deepseek import ChatDeepSeek
from pydantic import ConfigDict
from env import AGENT_API_KEY, AGENT_BASE_URL, DEEPSEEK_BASE_URL, DEEPSEEK_API_KEY
llm_by_openai = ChatOpenAI(model="deepseek-reasoner", 
    base_url=DEEPSEEK_BASE_URL, 
    api_key=DEEPSEEK_API_KEY)

# print(llm_by_openai.invoke("你是谁？"))

llm_by_deepseek = ChatDeepSeek(model="deepseek-reasoner", 
    api_base=DEEPSEEK_BASE_URL, 
    api_key=DEEPSEEK_API_KEY)

# print(llm_by_deepseek.invoke("你是谁？"))

llm_by_agent = ChatDeepSeek(
    model="Qwen-Thinking-Aanu",
    api_base=AGENT_BASE_URL, 
    api_key=AGENT_API_KEY)

# print(llm_by_agent.invoke("你是谁？"))

for chunk in llm_by_agent.stream("你是谁？"):
    if chunk.additional_kwargs.get("reasoning_content"):
        print(chunk.additional_kwargs.get("reasoning_content"), end="", flush=True)
    else:
        print(chunk.text, end="", flush=True)