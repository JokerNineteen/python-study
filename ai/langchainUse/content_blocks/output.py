# -*- coding: utf-8 -*-
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_core.output_parsers import StrOutputParser

from ai.langchainUse.models.model import qwenMax
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate([
    ("system","把用户输入的中文翻译成{language}"),
    ("human","{text}")
])

prompt = prompt.format(language="英文",text="我喜欢美女")
result = qwenMax.invoke(prompt)
print("result:",result)
print('-' * 100)

str_parser = StrOutputParser()
str_result = str_parser.invoke(result)
print("str_result:",str_result)
print('-' * 100)

print(result.content_blocks)