from langchain_unstructured import UnstructuredLoader

loader = UnstructuredLoader(
    "./files/chapter_one.pdf",
    chunking_strategy="basic",
    max_characters=2400,
    overlap=300
)

docs = loader.load()
for i, d in enumerate(docs[:2]):
    print(f"CHUNK {i}:")
    print(repr(d.page_content))
