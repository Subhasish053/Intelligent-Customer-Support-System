import pickle

with open("faiss_store.pkl", "rb") as f:
    index, data = pickle.load(f)

print("Total vectors in KB:", index.ntotal)
print("Sample chunk:")
print(data[0])
