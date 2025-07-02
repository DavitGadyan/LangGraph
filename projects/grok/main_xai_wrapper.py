#!/usr/bin/env python3
# main_xai_wrapper_fixed3.py

import os
import getpass
from dotenv import load_dotenv

# 1) Load your xAI/Grok API key
load_dotenv()
if "GROQ_API_KEY_X" not in os.environ:
    os.environ["GROQ_API_KEY_X"] = getpass.getpass("Enter your xAI/Grok API key: ")
KEY = os.environ["GROQ_API_KEY_X"]

# 2) Initialize the xAI SDK client (no scheme in host!)
from xai_sdk import Client as XAIClient
from xai_sdk.chat import system as xai_system, user as xai_user

xai = XAIClient(api_host="api.x.ai", api_key=KEY)

# 3) LangChain imports
from langchain.chat_models.base import BaseChatModel
from langchain.schema import ChatResult, ChatGeneration, AIMessage, SystemMessage, HumanMessage
from typing import List, Optional, Any, ClassVar

# 4) Define the LangChain ChatModel wrapper around xAI/Grok
class XAIChatModel(BaseChatModel):
    model_name: ClassVar[str] = "grok-3-mini"  # default Grok model

    @property
    def _llm_type(self) -> str:
        return "xai-grok"

    def _generate(
        self,
        messages: List[Any],            # List of SystemMessage, HumanMessage, etc.
        stop: Optional[List[str]] = None,
        **kwargs: Any
    ) -> ChatResult:
        # Create a new xAI chat session
        chat = xai.chat.create(
            model=self.model_name,
            temperature=kwargs.get("temperature", 0.0),
        )

        # Append each message to xAI chat
        for msg in messages:
            if isinstance(msg, SystemMessage):
                chat.append(xai_system(msg.content))
            elif isinstance(msg, HumanMessage):
                chat.append(xai_user(msg.content))
            else:
                # fallback for other message types
                chat.append(xai_user(msg.content))

        # Sample a completion
        resp = chat.sample()
        text = resp.content

        # Wrap result in LangChain types
        ai_msg = AIMessage(content=text)
        generation = ChatGeneration(message=ai_msg)
        return ChatResult(generations=[generation], llm_output={"raw": resp})

    async def _agenerate(self, *args, **kwargs):
        raise NotImplementedError("Async not supported yet")
