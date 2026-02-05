import re
from bs4 import BeautifulSoup

def clean_text(text):
    # Remove HTML
    text = BeautifulSoup(text, "html.parser").get_text()

    # Normalize spaces
    text = re.sub(r"\s+", " ", text)

    # Remove junk characters
    text = re.sub(r"[^\x00-\x7F]+", " ", text)

    return text.strip()


def preprocess_records(records):
    cleaned = []
    seen = set()

    for r in records:
        clean_conv = clean_text(r["conversation"])

        # remove duplicates
        if clean_conv in seen:
            continue

        seen.add(clean_conv)

        cleaned.append({
            **r,
            "conversation": clean_conv
        })

    return cleaned
