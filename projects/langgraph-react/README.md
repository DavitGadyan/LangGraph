🚀 **LangGraph ReACT Agent**

A simple ReACT-style agent built with LangGraph that interleaves **Reasoning** (R) and **Action** (Act) steps to handle user queries. At each turn, the agent:

1. **Thinks** – Generates internal reasoning about the task.  
2. **Acts** – Calls out to tools or functions via `ToolNode`.  
3. **Observes** – Captures the tool’s output as new context.  
4. **Answers** – Uses both reasoning and observations to produce the final reply.

---

### 🧰 Tools Used

- **python-dotenv** – Loads environment variables (e.g. API keys).  
- **LangChain Hub** (`hwchase17/react`) – Provides the ReACT prompt template.  
- **LangChain Agents** – `create_react_agent` to wire up the R/A loop.  
- **TavilySearchResults** – A community search tool for web queries (returns top result).  
- **Custom `triple` tool** – Example tool that multiplies a number by 3.  
- **ChatOpenAI (`gpt-4o-mini`)** – The underlying LLM for reasoning and responses.

---

**Workflow Graph Preview:**

![Graph](https://github.com/DavitGadyan/LangGraph/blob/main/projects/langgraph-react/graph.png)

**Graph Explanation:**

- **start**: Entry point of the agent.  
- **agent_reason**: The agent generates its internal reasoning (R) based on the user input or tool results.  
- **act**: If the agent decides an external action is needed, it invokes a tool (Act).  
- **end**: The agent terminates when no further actions are required.

**Control Flow:**

```mermaid
stateDiagram-v2
  [*] --> start
  start --> agent_reason
  agent_reason --> act: needs tool
  act --> agent_reason: tool output
  agent_reason --> [*]: done
