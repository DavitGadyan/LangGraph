# 🚀 LangGraph Project Showcase

A curated list of example projects built with **LangGraph**, demonstrating common patterns for LLM-driven workflows.

- **🔍 RAG Agent (Retrieval-Augmented Generation)**  
  A pipeline that ingests external data (e.g. news, prices), stores embeddings in a vectorstore, rewrites user queries, and returns context-aware answers via a LangGraph state machine.

- **🤖 ReACT Agent**  
  A “Reason & Act” loop that alternates internal reasoning steps with tool invocations. Ideal for tasks that require on-the-fly API calls, custom functions, or search tools.

- **💭 Reflection Agent**  
  A two-node graph that alternates between generating content and self-critiquing it. Useful for iterative improvement of creative outputs like tweets, blog posts, or marketing copy.

- **🔄 Reflexion Agent**  
  An extended “Draft → Execute Tools → Revise” agent using structured Pydantic schemas. It drafts an answer, recommends search queries, fetches data, then revises with citations—looping until convergence.

- **🛠️ ToolExecutor Showcase**  
  A standalone demonstration of integrating external tools (e.g. web search, calculators) into LangGraph. Highlights the use of `ToolInvocation` and `ToolMessage` for seamless tool orchestration.

- **📈 Monitoring & Costing**  
  An example integration with LangSmith to log token usage, latency, and cost for each LangGraph execution, enabling real-time observability and optimization.

- **📊 Mermaid & Graphviz Visuals**  
  Utilities for rendering your LangGraph workflows as Mermaid diagrams or ASCII art—perfect for documentation, presentations, or interactive notebooks.

---

> Each template comes with ready-to-run code, prompt configurations, and environment setups. Fork any example to bootstrap your own LangGraph-powered agent!
