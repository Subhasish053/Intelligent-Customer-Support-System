from llama_index.embeddings.huggingface.base import HuggingFaceEmbedding

embed_model = HuggingFaceEmbedding(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

def embed_text(text: str):
    return embed_model.get_text_embedding(text)

def embed_records(records):
    embedded = []

    for r in records:
        vector = embed_text(r["text"])

        embedded.append({
            "vector": vector,
            "text": r["text"],
            "metadata": r["metadata"]
        })

    return embedded
