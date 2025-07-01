#!/usr/bin/env python3
# deepseek_tool_binding.py

import json
from typing import Dict, Any

from langchain_ollama import OllamaLLM
from langchain.tools import tool
from langchain.tools.render import render_text_description
from langchain_core.prompts import ChatPromptTemplate

# 1. Initialize DeepSeek via Ollama
model = OllamaLLM(
    model="deepseek-r1:8b",
    base_url="http://127.0.0.1:11435",
    temperature=0.0,
)

# 2. Define tools with docstrings
@tool
def add(first_int: int, second_int: int) -> int:
    """
    Add two integers together.
    """
    return first_int + second_int

@tool
def multiply(first_int: int, second_int: int) -> int:
    """
    Multiply two integers together.
    """
    return first_int * second_int

@tool
def exponentiate(base: int, exponent: int) -> int:
    """
    Raise base to the exponent power.
    """
    return base ** exponent

tools = [add, multiply, exponentiate]

# 3. Render tool descriptions
rendered_tools = render_text_description(tools)

# 4. Build the system prompt
system_prompt = f"""You are an assistant with access to these tools:
{rendered_tools}

When you need a tool, output **only** a JSON object with two fields:
- "name": the tool name (string) or null  
- "arguments": an object with the tool’s arguments  

Ignore all internal reasoning; any extra text before or after the JSON should be discarded."""

prompt = ChatPromptTemplate.from_messages(
    [("system", system_prompt), ("user", "{input}")]
)

# 5. Simplified JSON extractor
def extract_json(text: str) -> Dict[str, Any]:
    start = text.find("{")
    end   = text.rfind("}")
    if start == -1 or end == -1 or start >= end:
        raise ValueError(f"No valid JSON object found in:\n{text!r}")
    fragment = text[start : end+1]
    return json.loads(fragment)

# 6. Dispatch helper
def tool_chain(parsed: Dict[str, Any]) -> Dict[str, Any]:
    name = parsed.get("name")
    args = parsed.get("arguments", {})
    if name is None:
        return {"name": None, "arguments": {}, "output": None}
    tool_map = {t.name: t for t in tools}
    chosen = tool_map[name]
    output = chosen.invoke(args)
    return {"name": name, "arguments": args, "output": output}

# 7. Simplified orchestration
def run_chain(input_text: str) -> Dict[str, Any]:
    # 1) Format prompt
    formatted = prompt.invoke({"input": input_text})
    # 2) Call model
    raw = model.invoke(formatted)
    # 3) Extract JSON
    parsed = extract_json(raw)
    # 4) Invoke the tool
    return tool_chain(parsed)

# 8. Utility to run queries
def query_with_tools(query: str):
    result = run_chain(query)
    print(f"User Query:  {query}")
    print(f"Tool Used:   {result['name']}")
    print(f"Arguments:   {result['arguments']}")
    print(f"Tool Output: {result['output']}")

# 9. Test
if __name__ == "__main__":
    query_with_tools("What's 3 plus 1132?")
