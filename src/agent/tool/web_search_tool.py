from ast import main
import re
from agent.env import ZHIPU_API_KEY
from langchain_core.tools import tool
from pydantic import BaseModel, Field

import logging

from zai import ZhipuAiClient

logger = logging.getLogger(__name__)

@tool('web_search', parse_docstring = True)
def web_search(query: str) -> str:
    """互联网搜索工具，用于搜索互联网上的信息
    
    Args:
        query: 搜索关键词
    
    Returns:
        搜索结果
    """
    try:
        response = zai_client.web_search.web_search(
            search_engine="search_std",
            search_query=query,
        )
        if response.search_results:
            return "\n\n".join([result.content for result in response.search_results])
        else:
            return "没有搜索到结果"
    except Exception as e:
        logger.error(f"搜索失败: {e}")
        return f"搜索失败: {e}"


class SearchArgs(BaseModel):
    query: str = Field(description="搜索关键词")

@tool('web_search2', args_schema = SearchArgs, description = "互联网搜索工具，用于搜索互联网上的信息")
def web_search2(args: SearchArgs) -> str:
    return f"Searching the web for {args.query}"

zai_client = ZhipuAiClient(api_key=ZHIPU_API_KEY)

if __name__ == "__main__":
    print(web_search.name)
    print(web_search.description)