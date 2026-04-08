from langchain_unstructured import UnstructuredLoader
from langchain_ollama import OllamaEmbeddings
from langchain_classic.vectorstores import Chroma
from langchain_community.vectorstores.utils import filter_complex_metadata

loader = UnstructuredLoader(
    "./files/chapter_one.pdf",
    chunking_strategy="basic",
    max_characters=2400,
    overlap=300
)

docs = loader.load()

for doc in docs:
    doc.page_content = doc.page_content.replace('\n\n', ' ').replace('\n', ' ')

docs = filter_complex_metadata(docs)

embedders = OllamaEmbeddings(model="llama3.1")
vectorstores = Chroma.from_documents(docs, embedders, collection_name="test_search_123")

results = vectorstores.similarity_search("where does winston live", k=3)
for i, r in enumerate(results):
    print(f"RES {i}: LEN={len(r.page_content)}")
    print(f"TEXT: {r.page_content[:200]}")
    if "Victory Mansions" in r.page_content or "victory mansions" in r.page_content.lower():
        print(">>> FOUND VICTORY MANSIONS IN THIS CHUNK!")
    print("-" * 50)
