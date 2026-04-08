from langchain_unstructured import UnstructuredLoader
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.vectorstores.utils import filter_complex_metadata
import pprint

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

embedders = OllamaEmbeddings(model="nomic-embed-text")
vectorstores = Chroma.from_documents(docs, embedders, collection_name="nomic_test_123")

results = vectorstores.similarity_search_with_score("where does winston live", k=3)
for i, (doc, score) in enumerate(results):
    print(f"RES {i+1}: Dist={score:.4f} LEN={len(doc.page_content)}")
    print(f"TEXT: {doc.page_content[:200]}")
    if "Victory Mansions" in doc.page_content or "victory mansions" in doc.page_content.lower():
        print(">>> FOUND VICTORY MANSIONS IN THIS CHUNK!")
    print("-" * 50)
