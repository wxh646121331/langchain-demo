from dotenv import load_dotenv
import os

import pandas as pd
import pandasai as pai
from pandasai import SmartDataframe
from pandasai_openai import OpenAI

load_dotenv()

llm = OpenAI(api_token = os.getenv("SILICONFLOW_API_KEY"), 
        api_base = os.getenv("SILICONFLOW_BASE_URL"))
llm.model = "deepseek-ai/DeepSeek-V3.2-Exp"
# 设置PandasAI配置
pai.config.set({
                "llm": llm,
                "save_logs": False,
                "save_charts": False,  # 不保存生成的图表
                "open_charts": False   # 不自动打开图表（禁用显示）
            })
# 假设的原始数据
df1 = pd.DataFrame({'id': [1, 2], 'revenue': [100, 200]})
df2 = pd.DataFrame({'id': [1, 2], 'name': ['A', 'B']})
df3 = pd.DataFrame({'prod_id': [10, 20], 'price': [50, 60]})

# print(df1.name)

# 使用 SmartDataframe 包装 DataFrame，并设置自定义表名
sdf1 = SmartDataframe(df1, name="sales", config={"llm": llm})
sdf2 = SmartDataframe(df2, name="customers", config={"llm": llm})
sdf3 = SmartDataframe(df3, name="products", config={"llm": llm})

# 获取 SmartDataframe 内部 dataframe 的 name
# 方法1: 通过 table_name 属性（如果存在）
print("sdf1.table_name:", getattr(sdf1, 'table_name', 'not found'))

# 方法2: 通过 dataframe.schema.name 访问内部的 dataframe name
print("sdf1.dataframe.schema.name:", sdf1.dataframe.schema.name)
print("sdf2.dataframe.schema.name:", sdf2.dataframe.schema.name)
print("sdf3.dataframe.schema.name:", sdf3.dataframe.schema.name)

# # 使用 SmartDataframe 进行查询
# result = pai.chat("A 员工的收入是多少？ ", sdf1, sdf2, sdf3)
# original_code = getattr(result, "last_code_executed", None)
# print(original_code)
# print(result)
