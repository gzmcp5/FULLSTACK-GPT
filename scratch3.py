from langchain_unstructured import UnstructuredLoader
# we use chunking_strategy
loader = UnstructuredLoader("./files/chapter_one.pdf", chunking_strategy="basic", max_characters=600)
docs = loader.load()
for i, doc in enumerate(docs[:5]):
    print(f"CHUNK {i} LENGTH:", len(doc.page_content))
    print(repr(doc.page_content[:150] + "..."))
