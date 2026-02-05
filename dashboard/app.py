import streamlit as st
import sys

from metrics import calculate_metrics


metrics = calculate_metrics()

st.subheader("📊 Performance Metrics")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Tickets Processed", metrics["tickets_processed"])
col2.metric("Time Saved (min)", metrics["time_saved_minutes"])
col3.metric("Cost Saved ($)", metrics["cost_saved_dollars"])
col4.metric("Escalated Cases", metrics["escalated_cases"])


sys.path.append("../pipeline2")

from rag_chat import ask


st.set_page_config(page_title="AI Support Dashboard", layout="wide")

st.title("🤖 Intelligent Customer Support System")

st.markdown("Ask questions based on customer tickets")

query = st.text_input("Enter customer question:")

if st.button("Get AI Response"):

    if query:
        answer, confidence = ask(query)

        st.subheader("📨 AI Response")
        st.write(answer)

        st.metric("Confidence", f"{confidence:.2f}%")

    else:
        st.warning("Please enter a question")
        
        
'''
HOW TO RUN THIS FILE:

cd dashboard
streamlit run app.py

'''
