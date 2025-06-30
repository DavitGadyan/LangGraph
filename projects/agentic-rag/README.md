🚀 **Agentic-RAG: Crypto Insights Chatbot**

A smart, AI-powered retrieval-augmented generation (RAG) system that extracts the latest news and price data for five major cryptocurrencies (XRP, BTC, ADA, ETH, SOL) from CoinDesk, stores embeddings in an in-memory vectorstore, and answers user questions via a LangGraph workflow with query rewriting and semantic search.

---

### 🔧 Workflows Included

#### 📰 `data_ingestion`

- Scrapes CoinDesk for:
  - General crypto headlines: `https://www.coindesk.com/`
  - Individual price pages:  
    - XRP: `https://www.coindesk.com/price/xrp`  
    - BTC: `https://www.coindesk.com/price/btc`  
    - ADA: `https://www.coindesk.com/price/ada`  
    - ETH: `https://www.coindesk.com/price/eth`  
    - SOL: `https://www.coindesk.com/price/sol`  
- Parses and extracts articles, timestamps, and price data.
- Generates embeddings with **OpenAI GPT-4o**.
- Stores embeddings in an **in-memory vectorstore** for fast semantic retrieval.

#### 🤖 `agentic_rag`

- **Step 1:** Receive user question.
- **Step 2:** Rewrite the question for better semantic matching.
- **Step 3:** Use vectorstore to retrieve the most relevant documents.
- **Step 4:** Generate a final, coherent answer with **GPT-4o**.
- **Step 5:** Stream updates through LangGraph nodes:  
  - `generate_query_or_respond` →  
  - conditional `retrieve` (via **ToolNode**) →  
  - `grade_documents` →  
  - `rewrite_question` →  
  - `generate_answer` → END.

**Workflow Graph Preview:**

![Graph](https://github.com/DavitGadyan/LangGraph/blob/main/projects/agentic-rag/diagram.png)

---

