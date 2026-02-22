from langchain.messages import HumanMessage
from langchain_core.messages import AIMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

from ai.langchainUse.messages.prompt_template import result
from ai.langchainUse.models.model import qwenMax

human_message = HumanMessage("写一首关于春天的七言绝句")

human_message = HumanMessage(content=[
    {"type": "text", "text": "你好"},
    {"type": "image_url","image_url": {"url": "https://example.com/image.png"}}
])

human_message = HumanMessage(content_blocks=[
    {"type": "text", "text": "你好"},
    {"type": "image", "url": "https://example.com/image.png"}
])

# anthrophic格式
message = AIMessage(
    content=[
    {"type": "thinking", "thinking": "你好","signature": "三疯"},
    {"type": "text","text": "三疯"}
    ],
    response_metadata={"model_provider": "authropic"}
)
# print(message.content_blocks)

prompt = ChatPromptTemplate([
    ("system","把用户输入的中文翻译成{language}"),
    ("human","{text}")
])

parser = StrOutputParser()

_chain = prompt | qwenMax | parser

result = _chain.invoke(
    {"language": "英文", "text": "我喜欢美女"}
)
print("result:",result)