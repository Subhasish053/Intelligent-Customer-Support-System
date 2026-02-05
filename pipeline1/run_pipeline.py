from zendesk_loader import load_from_zendesk
from preprocess import preprocess_records
from chunker import chunk_records
from compressor import compress_chunks
from metadata import enrich
from embedder import embed_records
from vectorstore import FaissStore

def run():

    print("👉 Loading Zendesk data...")
    records = load_from_zendesk()
    print("Loaded:", len(records))

    print("👉 Preprocessing...")
    cleaned = preprocess_records(records)
    print("After clean:", len(cleaned))

    print("👉 Chunking...")
    chunks = chunk_records(cleaned)
    print("Total chunks:", len(chunks))

    print("👉 Compressing...")
    compressed = compress_chunks(chunks)

    print("👉 Enriching metadata...")
    enriched = enrich(compressed)

    print("👉 Generating embeddings...")
    embedded = embed_records(enriched)
    print("Embeddings created:", len(embedded))

    print("👉 Creating FAISS store...")
    dim = len(embedded[0]["vector"])
    store = FaissStore(dim)

    for e in embedded:
        store.add(e["vector"], {
            "text": e["text"],
            "metadata": e["metadata"]
        })

    print("👉 Saving FAISS store...")
    store.save("faiss_store.pkl")

    print("✅ Knowledge base built successfully!")


if __name__ == "__main__":
    run()

#running 