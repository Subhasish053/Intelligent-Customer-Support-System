def chunk_text(text, max_chars=1000):
    chunks = []
    start = 0

    while start < len(text):
        end = start + max_chars
        chunk = text[start:end].strip()
        if chunk:
            chunks.append(chunk)
        start = end

    return chunks


def chunk_records(records):
    all_chunks = []

    for r in records:
        chunks = chunk_text(r["conversation"])

        for c in chunks:
            all_chunks.append({
                "ticket_id": r["ticket_id"],
                "timestamp": r["timestamp"],
                "status": r["status"],
                "chunk": c
            })

    return all_chunks
