🚀 **LangGraph Reflection Agent**

A looped “Reflect & Generate” agent that alternates between critiquing a draft tweet and producing an improved version, until a stopping condition is met.

---

### 🔧 Core Components

- **Reflection Prompt** (`reflection_prompt`)  
  System role: “You are a viral Twitter influencer grading a tweet. Generate critique and recommendations for the user's tweet. Always provide detailed recommendations, including requests for length, virality, style, etc.”

- **Generation Prompt** (`generation_prompt`)  
  System role: “You are a Twitter techie influencer assistant tasked with writing excellent Twitter posts. Generate the best tweet possible for the user's request. If the user provides critique, respond with a revised version of your previous attempts.”

- **LLM**  
  Uses `ChatOpenAI(model="gpt-4o-mini")` for both reflection and generation chains.

- **Custom Chains**  
  - `generate_chain = generation_prompt | llm`  
  - `reflect_chain  = reflection_prompt  | llm`

---

### 🧩 Graph Workflow

```mermaid
stateDiagram-v2
    [*] --> generate
    generate --> reflect : after each draft
    reflect --> generate : apply critique
    generate --> [*] : stop after 6 iterations
