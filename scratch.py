from langchain_unstructured import UnstructuredLoader
from langchain_classic.text_splitter import CharacterTextSplitter
import json

splitter = CharacterTextSplitter.from_tiktoken_encoder(
    separator="\n",
    chunk_size=600,
    chunk_overlap=100,
)

loader = UnstructuredLoader("./files/chapter_one.pdf", mode="single")
docs = loader.load_and_split(text_splitter=splitter)

for i, doc in enumerate(docs[:5]):
    print(f"CHUNK {i} LENGTH:", len(doc.page_content))
    print(repr(doc.page_content[:150] + "..."))

