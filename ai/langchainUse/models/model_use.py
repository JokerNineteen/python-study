# -*- coding: utf-8 -*-
from langchain.agents import create_agent
from langchain.agents.middleware import wrap_model_call, ModelRequest, ModelResponse
from langgraph.checkpoint.memory import InMemorySaver

import model
from langchain_openai import ChatOpenAI

basic_model = model.qwenPlus
advanced_mode = model.qwenMax

@wrap_model_call
def dynamic_model_selection(request: ModelRequest, handler) -> ModelResponse:
    message_count = len(request.state["messages"])
    if message_count > 5:
        model = basic_model
    else:
        model = advanced_mode

    return handler(request.override(model=model))

checkpointer = InMemorySaver()
config = {"configurable": {"thread_id": 1}}

agent = create_agent(
    model = basic_model,
    tools = [],
    middleware=[dynamic_model_selection],
    checkpointer=checkpointer,
    system_prompt="你是一个乐于助人的助手",
)

for _ in range(5):
    response = agent.invoke(
        {"messages": [{"role": "user", "content": "新年是几月几号？"}]},
        config=config)
    print(response)