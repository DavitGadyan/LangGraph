# app/main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agents import run_agents_pipeline

app = FastAPI(title="LangGraph + DeepSeek API", version="0.1.0")

class Query(BaseModel):
    text: str

class Response(BaseModel):
    result: str

@app.post("/process", response_model=Response)
async def process(query: Query):
    try:
        result = await run_agents_pipeline(query.text)
        return Response(result=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
