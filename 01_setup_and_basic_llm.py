import os
from getpass import getpass
from langchain_groq import ChatGroq

if "GROQ_API_KEY" not in os.environ:
    os.environ["GROQ_API_KEY"] = getpass("Enter your Groq API key: ")

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7,
)

response = llm.invoke(
    "Explain LangChain in three simple sentences."
)

print(response.content)
