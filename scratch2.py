from langchain_unstructured import UnstructuredLoader
loader = UnstructuredLoader("./files/chapter_one.pdf", mode="single")
docs = loader.load()
print("docs len:", len(docs))
print("text len:", len(docs[0].page_content))
print(repr(docs[0].page_content[:200]))
