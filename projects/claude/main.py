#!/usr/bin/env python3
# claude_react_fixed_string_arg.py

import os, getpass
from dotenv import load_dotenv

# 1) Load your Anthropic API key
load_dotenv()
if "ANTHROPIC_API_KEY" not in os.environ:
    os.environ["ANTHROPIC_API_KEY"] = getpass.getpass("Enter your Anthropic API key: ")
KEY = os.environ["ANTHROPIC_API_KEY"]

# 2) Import Claude
from langchain_anthropic.chat_models import ChatAnthropic

# 3) ReACT imports
from langchain import hub
from langchain.agents import initialize_agent, AgentType
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import tool

# 4) Pull the ReACT prompt
react_prompt: PromptTemplate = hub.pull("hwchase17/react")

# 5) Define your tool to accept a string
@tool
def triple(num: str) -> float:
    """Triple a number provided as a string (e.g. "4")."""
    return 3 * float(num)

tools = [triple]

# 6) Instantiate Opus 4.0
llm = ChatAnthropic(
    anthropic_api_key=KEY,
    model="claude-opus-4-0",
    temperature=0.0,
)

# 7) Build the agent with parsing retries
agent = initialize_agent(
    llm=llm,
    tools=tools,
    agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    agent_kwargs={"prompt": react_prompt},
    handle_parsing_errors=True,
)

# 8) Test
if __name__ == "__main__":
    question = "Triple 4, then triple that result again."
    result = agent.invoke({"input": question})
    print("\nAgent response:\n", result)
