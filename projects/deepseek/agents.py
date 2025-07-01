import abc
from dataclasses import dataclass
from ollama import AsyncClient

@dataclass
class Message:
    content: str

class Agent(abc.ABC):
    @abc.abstractmethod
    async def handle(self, message: Message) -> Message:
        ...

class DeepSeekAgent(Agent):
    def __init__(self, model: str = "deepseek-r1:8b", host: str = "http://localhost:11435"):
        self.client = AsyncClient(host=host)
        self.model = model

    async def handle(self, message: Message) -> Message:
        response = await self.client.chat(
            model=self.model,
            messages=[{"role": "user", "content": message.content}],
        )
        return Message(content=response["message"]["content"])

async def run_agents_pipeline(text: str) -> str:
    """
    Entry point for your FastAPI app. You can extend this to
    run multiple agents in series or in parallel.
    """
    # 1) wrap the input text in a Message
    msg = Message(content=text)

    # 2) pick your agent(s) — here just DeepSeekAgent for now
    agent = DeepSeekAgent()

    # 3) run it
    out_msg = await agent.handle(msg)
    
    # 4) return the raw string
    return out_msg.content
