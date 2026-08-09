import os
from getpass import getpass
from langchain_groq import ChatGroq

if "GROQ_API_KEY" not in os.environ:
    os.environ["GROQ_API_KEY"] = getpass("Enter your Groq API key: ")

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7,
)

for chunk in llm.stream("Explain LangChain in a simple paragraph."):
    print(chunk.content, end="", flush=True)

print()
