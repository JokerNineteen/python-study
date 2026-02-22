# -*- coding: utf-8 -*-
from langchain.agents import create_agent
from langchain.agents.middleware import dynamic_prompt, ModelRequest, ModelResponse
from typedict import TypeDict

from ai.langchainUse.models.model import qwenMax


# Agent1 = create_agent(
#     system_prompt="你一个乐于助人的助手，可以回答任何问题"
# )

class Context(TypeDict):
    user_role: str

@dynamic_prompt
def user_role_prompt(request: ModelRequest) -> ModelResponse:
    user_role = request.runtime.context.get("user_role","user")
    base_prompt = "你是一个乐于助人的助手，你可以回答任何问题"
    if user_role == "expert":
        return f"{base_prompt} 提供详细的技术回答"
    elif user_role == "beginner":
        return f"{base_prompt} 简单的解释概念，避免行话"
    return base_prompt

agent = create_agent(
    model = qwenMax,
    tools = [],
    middleware=[user_role_prompt],
    context_schema=Context,
)

response = agent.invoke(
    {"messages": [{"role": "user", "content": "解释一下什么是人工智能"}]},
    context={"user_role": "beginner"},
)

print(response)