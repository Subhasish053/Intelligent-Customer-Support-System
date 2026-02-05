import requests
import os

SCALEDOWN_API_KEY = os.getenv("SCALEDOWN_API_KEY")
URL = "https://api.scaledown.xyz/compress/raw/"

THRESHOLD = 1200


def scaledown_compress(text):
    headers = {
        "x-api-key": SCALEDOWN_API_KEY,
        "Content-Type": "application/json"
    }

    payload = {
        "context": text,
        "prompt": "Compress this support conversation keeping key issue and resolution",
        "scaledown": {"rate": "auto"}
    }

    res = requests.post(URL, headers=headers, json=payload)
    return res.json()["compressed_prompt"]


def compress_chunks(chunks):
    output = []

    for c in chunks:
        original = c["chunk"]

        if len(original) > THRESHOLD:
            compressed = scaledown_compress(original)
        else:
            compressed = original

        output.append({
            **c,
            "original": original,
            "compressed": compressed
        })

    return output

