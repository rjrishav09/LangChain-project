from typing import TypedDict
from langgraph.graph import StateGraph, START, END

class State(TypedDict):
    text: str
    result: str

def uppercase(state: State):
    return {"result": state["text"].upper()}

def add_prefix(state: State):
    return {"result": "LANGCHAIN: " + state["result"]}

graph = StateGraph(State)

graph.add_node("uppercase", uppercase)
graph.add_node("add_prefix", add_prefix)

graph.add_edge(START, "uppercase")
graph.add_edge("uppercase", "add_prefix")
graph.add_edge("add_prefix", END)

app = graph.compile()

result = app.invoke({
    "text": "learning langchain",
    "result": "",
})

print(result["result"])
