# -*- coding: utf-8 -*-
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

from ai.langchainUse.models.model import qwenMax

messages = [
    SystemMessage("你是一个像李白一样的诗人"),
    HumanMessage("写一篇关于春天的七言绝句"),
    AIMessage("桃花盛开...")
]

# messages = [
#     {"role": "system", "content": "你一个像李白一样的诗人"},
#     {"role": "user", "content": "写一篇关于春天的七言绝句"},
#     {"role": "assistant", "content": "桃花盛开..."}
# ]

response = qwenMax.invoke(messages)
print(response)