#!/usr/bin/env python3
# simple_grok_chat.py

import os
import getpass
from dotenv import load_dotenv

# 1) Load your xAI/Grok API key
load_dotenv()
if "GROQ_API_KEY_X" not in os.environ:
    os.environ["GROQ_API_KEY_X"] = getpass.getpass("Enter your xAI/Grok API key: ")
KEY = os.environ["GROQ_API_KEY_X"]

# 2) Import your LangChain wrapper around the xAI SDK
from main_xai_wrapper import XAIChatModel

# 3) LangChain message classes
from langchain.schema import SystemMessage, HumanMessage

# 4) Instantiate the Grok model
llm = XAIChatModel(
    model_name="grok-3-mini",  # or "grok-1", "grok-2-mini", etc.
    temperature=0.0,
)

# 5) Build a simple chat
messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="Who won the 2022 World Cup?"),
]

# 6) Invoke the model
reply = llm.invoke(messages)

# 7) Print the result
print("Grok replies:", reply.content)
