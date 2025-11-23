from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import SimpleJsonOutputParser
from agent.my_llm import llm

# SimpleJsonOutputParser + ChatPromptTemplate 格式化输出，适用于所有模型
prompt = ChatPromptTemplate.from_template(
    "尽你所能回答用户的问题"
    '你必须始终输出一个包含 title, year, director, rating 键的JSON对象'
    "{question}")

chain = prompt | llm | SimpleJsonOutputParser()

result = chain.invoke({"question": "我想要一部中国的动画电影，请推荐一部"})
print(result)
print(type(result))