# 🚀 LangGraph Project Showcase


| Model / Provider             | Open-Source? | Size            | Licensing / Pricing               | Native Func-Call | LangChain Integration                   | LangGraph Integration                   | Multi-Agent Suitability             | Cost (High-End/Reasoning) $/1K-tk | Cost (Std/Ordinary) $/1K-tk | Pros                                                                          | Cons                                                                             |
|------------------------------|--------------|-----------------|-----------------------------------|------------------|-----------------------------------------|------------------------------------------|------------------------------------|-------------------------------|-----------------------------|-------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| **DeepSeek-R1**              | Yes          | 8 B (Qwen3)     | MIT (self-hosted; zero cost)      | No               | ✅ via `langchain-ollama`               | ✅ via custom wrappers                  | Moderate                            | 0.00                          | 0.00                        | • Offline, zero-cost<br>• Lightweight, fits mid-range GPUs                    | • No native func-call<br>• Needs JSON-wrapper & prompt engineering               |
| **Mistral 7B/8×**            | Yes          | 7 B / 8 B       | Apache 2.0 (self-hosted)          | No               | ✅ via `langchain-mistral` or generic   | ✅ via wrapper                          | Moderate                            | 0.00                          | 0.00                        | • Strong perf per param<br>• Good instruction-following                      | • No built-in func-call<br>• Quantization required for small GPUs               |
| **Qwen-Turbo/Max**           | Partially*   | 7 B–34 B        | API: free tier + usage fees       | **Yes** (API)    | ✅ via `langchain-qwen`                 | ✅ via Qwen-Agent                       | High                                | ~0.004                        | ~0.002                      | • Native func-calling via cloud API<br>• Competitive benchmarks             | • Self-hosting loses native func-call<br>• API costs can add up                 |
| **OpenRouter-Hosted**        | Partially*   | Varies          | API usage fees                    | **Yes** (API)    | ✅ via `langchain`’s OpenRouter wrapper | ✅ via wrapper                          | High                                | ~0.006                        | ~0.002                      | • Aggregates many models<br>• Unified “ChatGPT-style” API                    | • Dependent on third-party uptime & fees                                       |
| **Frontier Alpha/Beta**      | Yes          | 1.3 B–20 B      | Apache 2.0                        | No               | ✅ via `langchain-frontier`             | ✅ via wrapper                          | Moderate                            | 0.00                          | 0.00                        | • Ultra-fast CPU inference via ggml<br>• Modular quantization                | • Early stage; fewer prebuilt tools<br>• No native func-call                   |
| **OpenAI ChatGPT (GPT-4)**   | No           | ≈175 B          | Subscr. + per-token fees          | **Yes**          | ✅ first-class via `langchain`          | ✅ first-class via LangGraph’s OpenAI   | Very High                           | ~0.045                        | ~0.002                      | • Best-in-class reasoning<br>• Native func-call & safety tools               | • Closed-source<br>• Higher latency & cost                                     |
| **Google Gemini (Cloud)**    | No           | 1 B–100 B+     | Google Cloud billing              | **Yes**          | ✅ via `langchain-googlegemini`         | ✅ via wrapper                          | High                                | ~0.030                        | ~0.002                      | • Multimodal (text+vision)<br>• Native func-call                             | • Closed-source<br>• Complex pricing                                           |
| **Grok (X by Meta)**         | No           | ≈175 B?         | Free tier (X Premium)             | No               | ✅ via generic OpenAI client            | ✅ via wrapper                          | Moderate                            | 0.00                          | 0.00                        | • Integrated into X platform<br>• Free for social use                        | • Limited API docs<br>• No native func-call                                    |
| **Azure OpenAI Service**     | No           | GPT-3.5–GPT-4   | Azure subscr. + usage              | **Yes**          | ✅ via `langchain`’s Azure integration  | ✅ via LangGraph’s OpenAI               | Very High                           | ~0.045                        | ~0.002                      | • Enterprise SLAs<br>• MS ecosystem integration                               | • Locked to Azure<br>• Same closed-source limits                               |
| **Anthropic Claude 2/3**      | No           | 70 B–100 B+     | Pay-as-you-go API                  | **Yes**          | ✅ via `langchain-anthropic`            | ✅ via wrapper                          | High                                | ~0.030                        | ~0.009                      | • Strong safety guardrails<br>• Good func-call                               | • Closed-source<br>• Higher cost per call than cheaper alternatives            |

\* “Partially”: checkpoint is open-source, but only the hosted/cloud API offers native function-calling; self-hosting requires a wrapper.  


A curated list of example projects built with **LangGraph**, demonstrating common patterns for LLM-driven workflows.

- **🔍 RAG Agent (Retrieval-Augmented Generation)**  
  A pipeline that ingests external data (e.g. news, prices), stores embeddings in a vectorstore, rewrites user queries, and returns context-aware answers via a LangGraph state machine.

- **🤖 ReACT Agent**  
  A “Reason & Act” loop that alternates internal reasoning steps with tool invocations. Ideal for tasks that require on-the-fly API calls, custom functions, or search tools.

- **🤖 Deekseek**  

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
