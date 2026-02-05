from local_llm import generate_answer


# -----------------------
# Ticket Routing Logic
# -----------------------

def route_ticket(category, escalation):

    if escalation == "ESCALATE":
        return "Senior Support Team"

    if category.lower() == "billing":
        return "Finance Team"

    if category.lower() == "technical issue":
        return "Technical Support Team"

    if category.lower() == "account":
        return "Account Management Team"

    return "General Support Team"


# -----------------------
# Resolution Prediction
# -----------------------

def predict_resolution(text):

    prompt = f"""
Predict how difficult this support ticket will be to resolve.

Return ONLY one word:
Easy
Medium
Complex

Ticket:
{text}
"""

    prediction = generate_answer(prompt)

    return prediction.strip()
