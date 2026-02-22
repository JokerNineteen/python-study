import bs4
from langchain_community.document_loaders import WebBaseLoader, Docx2txtLoader, TextLoader, PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter,CharacterTextSplitter

web_path = "https://www.news.cn/politics/20260222/cbdd06c843524a93911348b631cb4583/c.html"

loader = WebBaseLoader(
    web_path=[web_path],
    bs_kwargs=dict(parse_only = bs4.SoupStrainer(class_=("main-left left","title")))
)
docs = loader.load()
print(docs)
print('-' * 100)
exit()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50,
    separators=["\n\n", "\n", "(?<=\. )", " ", ""],
)

loader = TextLoader("../data/test.txt",encoding="utf-8")
docs = loader.load()
print()
print('-' * 100)
exit()

loader = Docx2txtLoader("../data/test.docx")
docs = loader.load()
print(docs)
print('-' * 100)
exit()

loader = PyMuPDFLoader("../data/证券行业.pdf")
docs = loader.load()
print(docs)
print('-' * 100)
exit()