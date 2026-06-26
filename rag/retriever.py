from rag.embeddings import model
from rag.vector_store import collection


def retrieve(query):

    embedding = model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[embedding],
        n_results=3
    )

    return results["documents"][0]