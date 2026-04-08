try:
    from langchain.storage import LocalFileStore
    print("Found in langchain.")
except ImportError:
    pass

try:
    from langchain_community.storage import LocalFileStore
    print("Found in langchain_community.")
except ImportError:
    pass

try:
    from langchain_core.stores import LocalFileStore
    print("Found in langchain_core.")
except ImportError:
    pass
    
try:
    from langchain_classic.storage import LocalFileStore
    print("Found in langchain_classic.")
except ImportError:
    pass
