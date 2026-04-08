from langchain_unstructured import UnstructuredLoader

loader = UnstructuredLoader(
    "./files/chapter_one.pdf", 
    chunking_strategy="basic",
    max_characters=600,
    overlap=100
)

docs = loader.load()
chunk = docs[1].page_content
print(repr(chunk[:200]))

from unstructured.cleaners.core import clean_extra_whitespace, replace_unicode_quotes
print("CLEANED:")
print(repr(clean_extra_whitespace(chunk[:200])))
