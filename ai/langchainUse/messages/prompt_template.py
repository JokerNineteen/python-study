from langchain_core.prompts import ChatPromptTemplate

from ai.langchainUse.models.model import qwenMax

prompt = ChatPromptTemplate([
    ("system","把用户输入的中文翻译成{language}"),
    ("human","{text}")
])

prompt = prompt.format(language="英文",text="我喜欢美女")
print("prompt:",prompt)
print('-'*100)

result = qwenMax.invoke(prompt)
print("result:",result)