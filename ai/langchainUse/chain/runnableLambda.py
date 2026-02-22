from langchain_core.runnables import RunnableLambda, chain, RunnableParallel
from langchain_core.prompts import ChatPromptTemplate
from operator import itemgetter
from langchain_core.output_parsers import StrOutputParser

from ai.langchainUse.models.model import qwenMax

template = ChatPromptTemplate.from_template("{a} + {b}是多少？")

def length(t):
    return len(t)

def mul(t1, t2):
    return len(t1) * len(t2)

@chain
def mul_length(d):
    return mul(d["t1"], d["t2"])

chain1 = template | qwenMax

chain2 = (
    {
        "a": itemgetter("name") | RunnableLambda(length),
        "b": {"t1": itemgetter("name"), "t2": itemgetter("sex")} | mul_length,
    }
    | chain1
    | StrOutputParser()
)

print(chain2.invoke({"name": "张三", "sex": "男"}))
print('-' * 100)