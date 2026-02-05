from local_llm import generate_answer


def analyze_sentiment(text):

    prompt = f"""
Analyze the sentiment of this support ticket.

Return ONLY one word:
Positive
Neutral
Negative

Ticket:
{text}
"""

    sentiment = generate_answer(prompt)
    return sentiment.strip()


'''def detect_escalation(sentiment, text):

    # Simple real-world rule logic

    urgent_keywords = ["urgent", "immediately", "asap", "angry", "frustrated", "complaint"]

    urgent = any(word in text.lower() for word in urgent_keywords)

    if sentiment.lower() == "negative" or urgent:
        return "ESCALATE"
    else:
        return "Normal" '''
        
def detect_escalation(sentiment, text):

    urgent_keywords = [
        "urgent",
        "immediate",
        "asap",
        "frustrated",
        "angry",
        "complaint",
        "not happy",
        "worst",
        "bad service",
        "delay",
        "escalate"
    ]

    text_lower = text.lower()

    urgent = any(word in text_lower for word in urgent_keywords)

    # Strong escalation logic
    if urgent:
        return "ESCALATE"

    if sentiment.lower() == "negative":
        return "ESCALATE"

    return "Normal"

