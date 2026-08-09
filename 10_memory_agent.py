import os
from getpass import getpass
from langchain_groq import ChatGroq
from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver

if "GROQ_API_KEY" not in os.environ:
    os.environ["GROQ_API_KEY"] = getpass("Enter your Groq API key: ")

model = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.4,
)

checkpointer = InMemorySaver()

agent = create_agent(
    model=model,
    tools=[],
    system_prompt="You are a helpful tutor. Remember the conversation within this thread.",
    checkpointer=checkpointer,
)

config = {"configurable": {"thread_id": "student-1"}}

first = agent.invoke(
    {"messages": [{"role": "user", "content": "My name is Alex and I am learning LangChain."}]},
    config=config,
)

second = agent.invoke(
    {"messages": [{"role": "user", "content": "What am I learning?"}]},
    config=config,
)

print(second["messages"][-1].content)
