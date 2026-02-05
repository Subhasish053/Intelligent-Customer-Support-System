def enrich(chunks):
    enriched = []

    for c in chunks:
        enriched.append({
            "text": c["compressed"],
            "metadata": {
                "ticket_id": c["ticket_id"],
                "timestamp": c["timestamp"],
                "status": c["status"],
                "category": None,
                "sentiment": None
            }
        })

    return enriched
