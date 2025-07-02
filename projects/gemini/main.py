#!/usr/bin/env python3
# main.py

import os
import getpass
from dotenv import load_dotenv

# 1) Load your Google AI API key
load_dotenv()
if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter your Google AI API key: ")
GOOGLE_API_KEY = os.environ["GOOGLE_API_KEY"]

# 2) Install with:
#     pip install -U langchain-google-genai langchain-core

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_core.tools import tool
from langchain_core.pydantic_v1 import BaseModel, Field

# 3) Define a simple multiply tool
@tool(description="Multiply two numbers together.")
def multiply(a: float, b: float) -> float:
    return a * b

# 4) Instantiate the Gemini model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.0,
    max_tokens=None,
    timeout=60,
    max_retries=2,
    api_key=GOOGLE_API_KEY,
)

# 5) Bind the tool
llm_with_tools = llm.bind_tools([multiply])

def main():
    # --- Simple chat ---
    sys_msg = SystemMessage(content="You are a helpful assistant.")
    user_msg = HumanMessage(content="Hello, Gemini! Who are you?")
    resp: AIMessage = llm.invoke([sys_msg, user_msg])
    print("Chat:", resp.content)

    # --- Tool calling ---
    tc = "What is 6 multiplied by 7? Use your tool."
    tool_resp: AIMessage = llm_with_tools.invoke([sys_msg, HumanMessage(content=tc)])
    print("\nTool Call Response:", tool_resp.content)
    print("Tool Calls:", tool_resp.tool_calls)

    # --- Structured output with Pydantic ---
    class Person(BaseModel):
        name: str = Field(..., description="Person's full name")
        age: int   = Field(..., description="Age in years")

    structured = llm.with_structured_output(Person)
    person: Person = structured.invoke([HumanMessage(content="Tell me about Ada Lovelace in JSON.")])
    print("\nStructured Output:", person)

if __name__ == "__main__":
    main()
