from rag_retriever import search_kb
from local_llm import generate_answer

from categorizer import categorize_ticket

from sentiment_escalation import analyze_sentiment, detect_escalation

from routing_resolution import route_ticket, predict_resolution




def build_prompt(query, retrieved_chunks):
    context = "\n\n".join([r["text"] for r in retrieved_chunks])

    return f"""
Use the following support data to answer the question.

Context:
{context}

Question:
{query}

Write a professional support response and end with:

Best regards,
Subhasish Mahapatro
Customer Support Team
GIET University


Answer clearly and accurately.
"""

# OLD CODE 

'''def ask(query):
    chunks, scores = search_kb(query)

    prompt = build_prompt(query, chunks)
    answer = generate_answer(prompt)

    # Confidence
    confidence = max(0, 100 - scores[0] * 10)

    # Category
    category = categorize_ticket(chunks[0]["text"])

    # Sentiment
    sentiment = analyze_sentiment(chunks[0]["text"])

    # Escalation
    escalation = detect_escalation(sentiment, chunks[0]["text"])

    print(f"Category: {category}")
    print(f"Sentiment: {sentiment}")
    print(f"Escalation Status: {escalation}")

    return answer, confidence'''
    
def ask(query):
    chunks, scores = search_kb(query)

    prompt = build_prompt(query, chunks)
    answer = generate_answer(prompt)

    # Confidence
    confidence = max(0, 100 - scores[0] * 10)

    # Category
    category = categorize_ticket(chunks[0]["text"])

    # Sentiment
    sentiment = analyze_sentiment(chunks[0]["text"])

    # Escalation
    escalation = detect_escalation(sentiment, chunks[0]["text"])

    # Routing
    team = route_ticket(category, escalation)

    # Resolution Prediction
    resolution = predict_resolution(chunks[0]["text"])

    print(f"Category: {category}")
    print(f"Sentiment: {sentiment}")
    print(f"Escalation Status: {escalation}")
    print(f"Routed To: {team}")
    print(f"Predicted Resolution: {resolution}")

    return answer, confidence





if __name__ == "__main__":
    while True:
        q = input("\nAsk a question (type exit to quit): ")

        if q.lower() == "exit":
            break

        answer, confidence = ask(q)

        print("\n--- AI ANSWER ---")
        print(answer)
        print(f"\nConfidence: {confidence:.2f}%")

        '''print("\n--- SOURCES ---")
        for s in sources:
            print(s["metadata"])'''
            
            
'''
TO RUN THE FILE:

cd F:\1st_Rag_project\pipeline2
python rag_chat.py

🧾 General Understanding

Try these first:

• What is this support ticket about?
• Can you summarize the customer’s issue?
• What problem is the customer facing?
• What did the customer request in this ticket?

🛠️ Resolution & Guidance

Customer is very frustrated and wants immediate fix

• How should the support team respond to this ticket?
• What steps can be taken to solve this issue?
• What is the best solution for the customer’s problem?
• How can we assist the customer effectively?

📧 Auto-Response Style (professional)

• Write a professional reply for this ticket
• Draft a support response to the customer
• Provide a polite resolution message
• How should we reply to this customer inquiry?

📊 When you add more tickets later (real power)

These will work even better as KB grows:

• Have we seen similar issues before?
• How were similar tickets resolved?
• What is the common solution for this type of problem?
• What patterns exist in customer issues?

🚨 Advanced (future when you scale)

• Which tickets need urgent attention?
• Are customers satisfied with resolutions?
• What are the most common problems reported?

'''
