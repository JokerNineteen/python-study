from ai.langchainUse.models.model import qwenMax

from langchain.agents import create_agent
# 导入摘要中间件类，用于在代理处理过程中添加摘要功能
from langchain.agents.middleware import SummarizationMiddleware

agent = create_agent(
    model = qwenMax,
    tools = [],
    middleware=[
        SummarizationMiddleware(
        model=qwenMax,
        trigger=('tokens',4000),
            keep=('message_v1',20),
            summary_prompt="请总结以下对话内容，并返回一个总结：{text}",
        ),
    ],
)