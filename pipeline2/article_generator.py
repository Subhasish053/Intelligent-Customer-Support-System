from local_llm import generate_answer


def generate_article(ticket_text):

    prompt = f"""
Convert this support ticket into a helpful knowledge base article.

Include:
- Title
- Problem
- Solution steps

Ticket:
{ticket_text}
"""

    article = generate_answer(prompt)

    return article
