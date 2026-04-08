try:
    from langchain.embeddings import CacheBackedEmbeddings
    print("Found in langchain.embeddings")
except ImportError:
    pass

try:
    from langchain_core.embeddings import CacheBackedEmbeddings
    print("Found in langchain_core.embeddings")
except ImportError:
    pass

try:
    from langchain_community.embeddings import CacheBackedEmbeddings
    print("Found in langchain_community.embeddings")
except ImportError:
    pass

try:
    from langchain_classic.embeddings import CacheBackedEmbeddings
    print("Found in langchain_classic.embeddings")
except ImportError:
    pass
