import os
from getpass import getpass
from langchain_groq import ChatGroq
from langchain.agents import create_agent
from langchain_core.tools import tool

if "GROQ_API_KEY" not in os.environ:
    os.environ["GROQ_API_KEY"] = getpass("Enter your Groq API key: ")

@tool
def calculate_discount(price: float, discount_percent: float) -> float:
    """Calculate the final price after a percentage discount."""
    return round(price - (price * discount_percent / 100), 2)

model = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0,
)

agent = create_agent(
    model=model,
    tools=[calculate_discount],
    system_prompt="You are a helpful shopping assistant. Use tools when calculation is required.",
)

result = agent.invoke({
    "messages": [
        {
            "role": "user",
            "content": "A product costs 2500 and has a 20% discount. What is the final price?"
        }
    ]
})

print(result["messages"][-1].content)
