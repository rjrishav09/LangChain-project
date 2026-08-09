import os
from getpass import getpass
from pydantic import BaseModel, Field
from langchain_groq import ChatGroq

if "GROQ_API_KEY" not in os.environ:
    os.environ["GROQ_API_KEY"] = getpass("Enter your Groq API key: ")

class ProductIdea(BaseModel):
    name: str = Field(description="Creative product or company name")
    slogan: str = Field(description="Short marketing slogan")
    target_customer: str = Field(description="Primary target customer")

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.5,
)

structured_llm = llm.with_structured_output(ProductIdea)

result = structured_llm.invoke(
    "Create a product idea for a company that makes colorful socks."
)

print(result)
print("\nName:", result.name)
print("Slogan:", result.slogan)
print("Target:", result.target_customer)
