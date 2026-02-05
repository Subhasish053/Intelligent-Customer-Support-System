# 🤖 Intelligent Customer Support Knowledge Base System

An AI-powered customer support automation platform built using a Retrieval-Augmented Generation (RAG) pipeline.

This system ingests historical Zendesk support tickets, builds an intelligent vector knowledge base, and provides automated responses, smart routing, sentiment detection, escalation handling, performance metrics, and a Streamlit dashboard for real-time interaction.

The project demonstrates how modern AI systems can significantly improve customer support efficiency, reduce response time, and lower operational costs.

---

## 📌 Problem Statement

Customer support teams handle thousands of tickets daily, often repeating similar solutions and manually routing issues.

This project aims to:

• Build an intelligent knowledge base from historical tickets  
• Automate customer responses using AI  
• Compress long conversation threads efficiently  
• Classify and prioritize tickets  
• Route issues to the correct teams  
• Predict resolution complexity  
• Provide analytics and performance metrics  

---

## 🚀 Key Features

### 📥 Data Ingestion
- Zendesk ticket history ingestion via API
- Supports large-scale ticket datasets

### 🧠 Knowledge Base Creation
- Text preprocessing & cleaning
- Intelligent chunking of conversations
- Context compression (ScaleDown-style architecture)
- Embedding generation using Sentence Transformers
- FAISS vector database for fast similarity search

### 🔍 Retrieval-Augmented Generation (RAG)
- Query embedding
- Relevant ticket retrieval
- Context-aware answer generation using local LLM (Mistral)

### 🤖 AI Automation Layer
- Auto-response suggestions
- Confidence scoring
- Ticket categorization
- Sentiment analysis
- Escalation detection
- Ticket routing
- Resolution difficulty prediction

### 📊 Dashboard & Analytics
- Streamlit web interface
- Real-time AI chat
- Performance metrics (time saved, cost reduction, escalations)
- Knowledge article generation

---

## 🏗️ System Architecture

Zendesk Tickets / Documents
↓
Preprocessing & Cleaning
↓
Chunking + Compression
↓
Embedding Generation
↓
FAISS Vector Database
↓
RAG Retrieval
↓
Local LLM (Mistral via LM Studio)
↓
AI Responses + Automation
↓
Streamlit Dashboard & Metrics



---

## 📁 Project Structure

Intelligent-Customer-Support-System/
│
├── pipeline1/ # Knowledge base creation
│ ├── zendesk_loader.py
│ ├── preprocess.py
│ ├── chunker.py
│ ├── compressor.py
│ ├── embedder.py
│ ├── vectorstore.py
│ └── run_pipeline.py
│
├── pipeline2/ # AI & automation layer
│ ├── rag_chat.py
│ ├── rag_retriever.py
│ ├── local_llm.py
│ ├── categorizer.py
│ ├── sentiment_escalation.py
│ ├── routing_resolution.py
│ ├── metrics.py
│ └── article_generator.py
│
├── dashboard/
│ └── app.py # Streamlit UI
│
├── requirements.txt
├── .gitignore
└── README.md


---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/Subhasish053/Intelligent-Customer-Support-System.git
cd Intelligent-Customer-Support-System

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Configure Environment Variables

Create a .env file:

ZENDESK_API_TOKEN=your_api_token
ZENDESK_EMAIL=your_email
ZENDESK_SUBDOMAIN=your_company

4️⃣ Build Knowledge Base
python pipeline1/run_pipeline.py


⚠️ The FAISS vector database is generated locally and not included in the repository.

5️⃣ Run AI Assistant (CLI)
python pipeline2/rag_chat.py

6️⃣ Launch Dashboard
streamlit run dashboard/app.py
