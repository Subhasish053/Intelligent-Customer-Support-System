from embedder import embed_text

vec = embed_text("Payment failed but money deducted")

print(len(vec))
print(vec[:5])
