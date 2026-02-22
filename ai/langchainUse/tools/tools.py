from langchain.agents import create_agent
from langchain_core.tools import tool

from ai.langchainUse.models.model import qwenMax

@tool
def search_database(query: str, limit: int = 10) -> str:
    """在客户的数据库中搜索匹配查询的记录
    Args:
        query: 要查找的搜索词
        limit:  返回的最大结果数
    """
    return f"这个查询:'{query}',找到了{limit}条结果"

@tool("web_search")
def search_web(query: str) -> str:
    """Search the web for the answer to the user's question."""
    return f"这个查询:'{query}',找到了10条结果"

@tool("calculator",description="计算器")
def calculator(expression: str) -> str:
    """计算给定的数学表达式"""
    return str(eval(expression))

from pydantic import BaseModel, Field
from typing import Literal

class WeatherInput(BaseModel):
    city: str = Field(..., description="要查询的城市名称")
    unit: Literal["celsius", "fahrenheit"] = Field(
        default="celsius", description="温度单位"
    )
    include_forecast: bool = Field(
        default=False, description="包含五天天气预报"
    )

@tool(args_schema=WeatherInput)
def get_weather(city: str, unit: str, include_forecast: bool) -> str:
    """获取指定城市的天气信息"""
    temp = 22 if unit == "celsius" else 72
    return f"{city}的天气是晴天，温度是{temp}度，单位: {unit[0].upper()}"
    if include_forecast:
        return f"{city}的5天预报是：\n{get_weather(city, unit)}"

agent = create_agent(qwenMax,tools=[search_web,get_weather])
response = agent.invoke({"messages": [{"role": "user", "content": "哈尔滨的天气如何？"}]})
print(response)