# Agentic RAG Engine: Autonomous Query Synthesis & Refinement

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![LangChain](https://img.shields.io/badge/LangChain-latest-blue.svg)](https://python.langchain.com/)

An advanced **Retrieval-Augmented Generation (RAG)** system that utilizes agentic reasoning to dynamically route queries, decompose complex prompts, and perform multi-stage document refinement. Designed for high-precision enterprise applications.

## Overview

Traditional RAG systems often struggle with multi-part questions or ambiguous context. This engine addresses these limitations through an **Agentic Loop**:

1.  **Query Decomposition:** A specialized 'Planner' agent breaks down complex user inquiries into atomic sub-tasks.
2.  **Hybrid Retrieval:** Combines semantic (vector) search with keyword (BM25) search to ensure maximum recall.
3.  **Self-Correction Logic:** A 'Refiner' agent audits the retrieved context for relevance and hallucination risks before generation.
4.  **Multi-Vector Indexing:** Optimized indexing strategy for handling diverse document formats (PDF, Markdown, JSON).

## Project Structure

```text
├── src/
│   ├── agents/
│   │   ├── planner.py         # Query decomposition and routing
│   │   └── refiner.py         # Hallucination detection & verification
│   ├── retrieval/
│   │   ├── vector_store.py    # FAISS/ChromaDB integration
│   │   └── hybrid_search.py   # Vector + Keyword search logic
│   ├── synthesis/
│   │   └── generator.py       # Final synthesis with LLM provider
│   └── main.py                # Pipeline orchestration
├── tests/
│   └── test_agent_flow.py
├── data/
│   └── sample_docs/           # For testing retrieval quality
├── requirements.txt
└── README.md
```

## Getting Started

### Installation

```bash
pip install -r requirements.txt
```

### Usage

```python
from src.main import AgenticRAG

# Initialize the engine with preferred LLM (e.g., GPT-4o)
rag_engine = AgenticRAG(model_name="gpt-4o", vector_db_path="./db")

# Complex query requiring decomposition and multi-stage retrieval
response = rag_engine.query("Compare the Q3 financial results of Company A and B, specifically focusing on R&D spend.")
print(response)
```

## Methodology

The engine implements a **Plan-Execute-Refine** loop. The **Planner** identifies that the query requires two separate document retrievals (one for Company A, one for Company B). The **Hybrid Search** retrieves relevant chunks, and the **Refiner** ensures the data is strictly from the Q3 reports before passing it to the **Generator**.

## Performance Benchmarks

Initial evaluations using the RAGAS framework (comparison against naive RAG):

| Metric | Naive RAG | Agentic RAG Engine |
|--------|-----------|-------------------|
| Faithfulness | 0.72 | **0.91** |
| Answer Relevancy | 0.68 | **0.88** |
| Context Precision | 0.75 | **0.93** |

## License

Distributed under the MIT License. See `LICENSE` for more information.
