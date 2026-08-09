import os
from getpass import getpass
from langchain_groq import ChatGroq
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_huggingface import HuggingFaceEmbeddings

if "GROQ_API_KEY" not in os.environ:
    os.environ["GROQ_API_KEY"] = getpass("Enter your Groq API key: ")

documents = [
    Document(page_content="LangChain provides abstractions for building LLM applications."),
    Document(page_content="RAG retrieves relevant external context before generating an answer."),
    Document(page_content="Embeddings convert text into vectors so semantic similarity can be searched."),
    Document(page_content="A retriever returns documents relevant to a user query."),
]

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector_store = InMemoryVectorStore(embedding=embeddings)
vector_store.add_documents(documents)

retriever = vector_store.as_retriever(search_kwargs={"k": 2})

llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0)

prompt = ChatPromptTemplate.from_template(
    """
    Answer using only the context below.

    Context:
    {context}

    Question:
    {question}

    If the answer is not in the context, say you do not know.
    """
)

question = "What does RAG do?"
docs = retriever.invoke(question)
context = "\n\n".join(doc.page_content for doc in docs)

chain = prompt | llm

answer = chain.invoke({
    "context": context,
    "question": question,
})

print(answer.content)
