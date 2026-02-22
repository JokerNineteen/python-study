# -*- coding: utf-8 -*-
import os
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model = "qwen-plus",
    api_key= os.getenv("ALI-AI-KEY"),
    base_url= "https://dashscope.aliyuncs.com/compatible-mode/v1"
)
response = llm.invoke("你好，你是谁？")
print(response)