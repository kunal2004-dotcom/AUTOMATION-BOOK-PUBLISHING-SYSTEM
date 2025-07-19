import chromadb
from chromadb.config import Settings

client = chromadb.Client(Settings())
collection = client.get_or_create_collection("book_versions")

def save_version(text, version_id, metadata={}):
    collection.add(documents=[text], ids=[version_id], metadatas=[metadata])

def semantic_search(query):
    results = collection.query(query_texts=[query], n_results=3)
    return results