import os
from getpass import getpass
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

if "GROQ_API_KEY" not in os.environ:
    os.environ["GROQ_API_KEY"] = getpass("Enter your Groq API key: ")

llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.7)
parser = StrOutputParser()

description_prompt = ChatPromptTemplate.from_template(
    "Create an attractive product description for: {product}"
)

slogan_prompt = ChatPromptTemplate.from_template(
    """
    Product description:
    {description}

    Create a short, memorable marketing slogan.
    """
)

description_chain = description_prompt | llm | parser
slogan_chain = slogan_prompt | llm | parser

product = "AI-powered fitness application"

description = description_chain.invoke({"product": product})
slogan = slogan_chain.invoke({"description": description})

print("DESCRIPTION:\n", description)
print("\nSLOGAN:\n", slogan)
