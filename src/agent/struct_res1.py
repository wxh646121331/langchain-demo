from agent.my_llm import llm
from agent.scheme.movie import Movie

# with_structured_output 结构化输出，部分模型支持结构化输出，如deepseek-ai/DeepSeek-V3.2-Exp
# include_raw=True 返回原始数据
movie_model = llm.with_structured_output(Movie)
result = movie_model.invoke("我想要一部中国的科幻电影，请推荐一部")
print(result)
print(type(result))