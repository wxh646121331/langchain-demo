
import datetime
from langchain_core.tools import Tool
import logging

logger = logging.getLogger(__name__)

@Tool(name='get_date', parse_docstring = True)
def get_date() -> str:
    """ 获取日期工具
    Args:
        None
    Returns:
        str 日期
    """
    return datetime.date.today().strftime("%Y-%m-%d")   