from local_llm import generate_answer

def categorize_ticket(text):

    prompt = f"""
Classify the following support ticket into ONE category:

Categories:
- Billing
- Technical Issue
- Account
- General Inquiry
- Other

Ticket:
{text}

Return only the category name.
"""

    category = generate_answer(prompt)
    return category.strip()
