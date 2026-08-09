import os
from getpass import getpass
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

if "GROQ_API_KEY" not in os.environ:
    os.environ["GROQ_API_KEY"] = getpass("Enter your Groq API key: ")

llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.7)

prompt = ChatPromptTemplate.from_template(
    "Write a short LinkedIn post explaining {topic}."
)

chain = prompt | llm | StrOutputParser()

result = chain.invoke({"topic": "LangChain LCEL"})

print(result)
