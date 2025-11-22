import langchain_openai
from langchain_openai import ChatOpenAI
from langchain_deepseek import ChatDeepSeek
from pydantic import ConfigDict
from env import AGENT_API_KEY, AGENT_BASE_URL, DEEPSEEK_BASE_URL, DEEPSEEK_API_KEY, SILICONFLOW_API_KEY, SILICONFLOW_BASE_URL
from scheme.movie import Movie
# llm_by_openai = ChatOpenAI(model="deepseek-reasoner", 
#     base_url=DEEPSEEK_BASE_URL, 
#     api_key=DEEPSEEK_API_KEY)

# # print(llm_by_openai.invoke("你是谁？"))

# llm_by_deepseek = ChatDeepSeek(model="deepseek-reasoner", 
#     api_base=DEEPSEEK_BASE_URL, 
#     api_key=DEEPSEEK_API_KEY)

# # print(llm_by_deepseek.invoke("你是谁？"))

# llm_by_agent = ChatDeepSeek(
#     model="Qwen-Thinking-Aanu",
#     api_base=AGENT_BASE_URL, 
#     api_key=AGENT_API_KEY)

llm = ChatOpenAI(
    model="deepseek-ai/DeepSeek-V3.2-Exp",
    base_url=SILICONFLOW_BASE_URL,
    api_key=SILICONFLOW_API_KEY)

# print(llm.invoke("你是谁？"))

movie_model = llm.with_structured_output(Movie)

print(movie_model.invoke("我想要一部中国的科幻电影，请推荐一部"))