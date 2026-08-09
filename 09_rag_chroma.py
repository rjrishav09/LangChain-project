import os
from getpass import getpass
from langchain_groq import ChatGroq
from langchain_core.documents import Document
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

if "GROQ_API_KEY" not in os.environ:
    os.environ["GROQ_API_KEY"] = getpass("Enter your Groq API key: ")

documents = [
    Document(page_content="LangChain is a framework for building applications powered by language models."),
    Document(page_content="Chroma is a vector store that can be used for semantic search."),
    Document(page_content="RAG combines retrieval with generation to ground model responses in external data."),
]

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector_store = Chroma(
    collection_name="langchain_course",
    embedding_function=embeddings,
    persist_directory="./chroma_db",
)

vector_store.add_documents(documents)

results = vector_store.similarity_search(
    "What is RAG?",
    k=2,
)

for doc in results:
    print("-", doc.page_content)
