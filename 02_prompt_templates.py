import os
from getpass import getpass
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

if "GROQ_API_KEY" not in os.environ:
    os.environ["GROQ_API_KEY"] = getpass("Enter your Groq API key: ")

llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.7)

prompt = ChatPromptTemplate.from_template(
    """
    You are a helpful teacher.
    Explain {topic} to a {audience}.
    Give one simple example.
    """
)

chain = prompt | llm

result = chain.invoke({
    "topic": "Retrieval-Augmented Generation",
    "audience": "beginner",
})

print(result.content)
