# LangChain: Basic to Advanced with Groq

A teaching-friendly LangChain curriculum using Python and Groq. The project starts with LLM basics and progresses through prompts, LCEL, sequential workflows, structured output, tools, agents, RAG, memory, streaming, and LangGraph.

## Learning path

1. `01_setup_and_basic_llm.py` — setup, API key, ChatGroq, invoke
2. `02_prompt_templates.py` — reusable prompt templates
3. `03_lcel_chains.py` — LCEL pipelines with `|`
4. `04_sequential_workflow.py` — multi-step sequential workflow
5. `05_structured_output.py` — Pydantic structured responses
6. `06_tools.py` — create custom tools with `@tool`
7. `07_agents.py` — tool-using agents with `create_agent`
8. `08_rag_inmemory.py` — document retrieval + RAG using an in-memory vector store
9. `09_rag_chroma.py` — persistent Chroma vector store
10. `10_memory_agent.py` — short-term conversational memory with an agent checkpointer
11. `11_streaming.py` — streaming model output
12. `12_langgraph_intro.py` — a small explicit LangGraph workflow
13. `13_capstone_ai_assistant.py` — capstone combining model + tools + structured output

## Prerequisites

- Python 3.10+
- A Groq API key
- Basic Python knowledge
- Optional: Google Colab

## Install

```bash
pip install -U -r requirements.txt
```

Set your key as an environment variable:

```bash
export GROQ_API_KEY="your_key"
```

Windows PowerShell:

```powershell
$env:GROQ_API_KEY="your_key"
```

Google Colab:

```python
import os
from getpass import getpass
os.environ["GROQ_API_KEY"] = getpass("Enter Groq API key: ")
```

Never commit a real API key to GitHub.

## Recommended teaching order

Teach one file at a time. After each lesson, change the example instead of only running it. For example, replace the product example with a resume assistant, customer-support bot, travel assistant, or study assistant.

## Architecture

```text
Python
  |
  +--> LangChain model interface
  |       |
  |       +--> ChatGroq
  |
  +--> Prompt templates
  |
  +--> LCEL / Runnables
  |
  +--> Tools
  |
  +--> Agents
  |
  +--> Retrieval / RAG
  |
  +--> LangGraph
```

## Important note about LangChain versions

LangChain changes quickly. This repository intentionally uses the modern package split and LCEL/agent APIs. If an API changes, check the official LangChain documentation before changing the teaching material.

Official documentation:
- LangChain: https://docs.langchain.com/
- ChatGroq integration: https://docs.langchain.com/oss/python/integrations/chat/groq
- Agents: https://docs.langchain.com/oss/python/langchain/agents
- Retrieval: https://docs.langchain.com/oss/python/langchain/retrieval
- Chroma: https://docs.langchain.com/oss/python/integrations/vectorstores/chroma

## GitHub

This repository is designed to be pushed to GitHub. Keep secrets out of source code. Use `.env.example` as a template and `.gitignore` to prevent accidental secret commits.
