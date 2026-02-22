# -*- coding: utf-8 -*-
import os
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent

qwenMax = ChatOpenAI(
    model = "qwen3-max",
    api_key= os.getenv("ALI-AI-KEY"),
    base_url= "https://dashscope.aliyuncs.com/compatible-mode/v1"
)

qwenPlus = ChatOpenAI(
    model = "qwen3.5-plus",
    api_key= os.getenv("ALI-AI-KEY"),
    base_url= "https://dashscope.aliyuncs.com/compatible-mode/v1"
)