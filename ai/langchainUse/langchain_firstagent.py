# -*- coding: utf-8 -*-
import os
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain.tools import tool

model = ChatOpenAI(
    model = "qwen3-max",
    api_key= os.getenv("ALI-AI-KEY"),
    base_url= "https://dashscope.aliyuncs.com/compatible-mode/v1"
)

def get_weather(city: str) -> str:
    """获取指定城市的天气"""
    return f"{city} 天气总是晴朗！"

agent = create_agent(
    model=model,
    tools=[get_weather],
    system_prompt="你是一个乐于助人的助手",
)

# 执行代理
result = agent.invoke(
    {"messages": [{"role": "user", "content": "旧金山天气如何？"}]}
)


print(result)