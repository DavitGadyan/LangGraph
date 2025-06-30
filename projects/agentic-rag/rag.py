import json
import pprint
from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode
from langgraph.prebuilt import tools_condition
from langgraph.graph import MessagesState

from preprocess import generate_query_or_respond, retriever_tool, rewrite_question, generate_answer,grade_documents
from IPython.display import Image, display

from dotenv import load_dotenv

load_dotenv()


workflow = StateGraph(MessagesState)

# Define the nodes we will cycle between
workflow.add_node(generate_query_or_respond)
workflow.add_node("retrieve", ToolNode([retriever_tool]))
workflow.add_node(rewrite_question)
workflow.add_node(generate_answer)

workflow.add_edge(START, "generate_query_or_respond")

# Decide whether to retrieve
workflow.add_conditional_edges(
    "generate_query_or_respond",
    # Assess LLM decision (call `retriever_tool` tool or respond to the user)
    tools_condition,
    {
        # Translate the condition outputs to nodes in our graph
        "tools": "retrieve",
        END: END,
    },
)

# Edges taken after the `action` node is called.
workflow.add_conditional_edges(
    "retrieve",
    # Assess agent decision
    grade_documents,
)
workflow.add_edge("generate_answer", END)
workflow.add_edge("rewrite_question", "generate_query_or_respond")

# Compile
graph = workflow.compile()

# get the raw PNG bytes
png_bytes = graph.get_graph().draw_mermaid_png()

# write them out to a file
with open("diagram.png", "wb") as f:
    f.write(png_bytes)

display(Image(graph.get_graph().draw_mermaid_png()))

for chunk in graph.stream(
    {
        "messages": [
            {
                "role": "user",
                "content": "What does articles says about XRP, BTC prices? What are top stories now related to XRP< BTC, ETH, ADA, SOL or some regulations from US, provide timestamps also?",
            }
        ]
    }
):
    for node, update in chunk.items():
        print("Update from node", node)
        pprint.pprint(update["messages"][-1])
        print("\n\n")