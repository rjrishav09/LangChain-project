import os
from getpass import getpass
from pydantic import BaseModel, Field
from langchain_groq import ChatGroq
from langchain.agents import create_agent
from langchain_core.tools import tool

if "GROQ_API_KEY" not in os.environ:
    os.environ["GROQ_API_KEY"] = getpass("Enter your Groq API key: ")

@tool
def calculate_discount(price: float, discount_percent: float) -> float:
    """Calculate the final price after applying a percentage discount."""
    return round(price - (price * discount_percent / 100), 2)

class AssistantPlan(BaseModel):
    answer: str = Field(description="Final helpful answer")
    action: str = Field(description="Recommended next action")

model = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.3,
)

agent = create_agent(
    model=model,
    tools=[calculate_discount],
    system_prompt=(
        "You are a practical AI assistant. "
        "Use tools when calculations are needed. "
        "Keep answers concise and useful."
    ),
)

result = agent.invoke({
    "messages": [
        {
            "role": "user",
            "content": "A course costs 5000 with a 15% discount. Tell me the final price and what I should do next."
        }
    ]
})

print(result["messages"][-1].content)

print("\nCapstone idea:")
print("Extend this assistant with RAG, a database tool, web search, structured output, and LangGraph orchestration.")
