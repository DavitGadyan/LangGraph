#!/usr/bin/env python3
# main.py

import os
import getpass
from dotenv import load_dotenv

# 1) Load your Groq API key
load_dotenv()
if "GROQ_API_KEY" not in os.environ:
    os.environ["GROQ_API_KEY"] = getpass.getpass("Enter your Groq API key: ")

from xai_sdk import Client
from xai_sdk.chat import user,system

client = Client(
  api_host="api.x.ai",
  api_key=os.environ["GROQ_API_KEY"]
)

chat = client.chat.create(model="grok-3-mini", temperature=0)
chat.append(system("You are a PhD-level mathematician."))
chat.append(user("What is 2 + 2?"))

response = chat.sample()
print(response.content)