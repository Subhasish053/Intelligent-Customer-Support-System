import pickle
import faiss
import numpy as np
import sys

# Allow import from pipeline1
sys.path.append("../pipeline1")

from embedder import embed_text


def load_kb(path="../pipeline1/faiss_store.pkl"):
    with open(path, "rb") as f:
        index, data = pickle.load(f)
    return index, data

#OLD CODE WITHOUT CONFIDENCE SCORES
'''def search_kb(query, top_k=3):
    index, data = load_kb()

    query_vector = embed_text(query)

    D, I = index.search(
        np.array([query_vector]).astype("float32"),
        top_k
    )

    results = []
    for idx in I[0]:
        results.append(data[idx])

    return results'''


def search_kb(query, top_k=1):
    index, data = load_kb()

    query_vector = embed_text(query)

    D, I = index.search(
        np.array([query_vector]).astype("float32"),
        top_k
    )

    results = []
    scores = []

    for dist, idx in zip(D[0], I[0]):
        results.append(data[idx])
        scores.append(dist)

    return results, scores
