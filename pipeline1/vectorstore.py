import faiss
import numpy as np
import pickle

class FaissStore:
    def __init__(self, dim):
        self.index = faiss.IndexFlatL2(dim)
        self.data = []

    def add(self, vector, record):
        self.index.add(np.array([vector]).astype("float32"))
        self.data.append(record)

    def save(self, path="faiss_store.pkl"):
        with open(path, "wb") as f:
            pickle.dump((self.index, self.data), f)
