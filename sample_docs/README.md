# RAG Pipeline with LangChain and IBM Granite

This document is part of a demonstration of Retrieval-Augmented Generation (RAG) using open-source tools and IBM Granite models. It explains the architecture and purpose of this project.

## 🔍 What is RAG?

RAG, or Retrieval-Augmented Generation, is a hybrid approach that enhances the capabilities of language models by integrating external knowledge retrieved from a vector store. It works in two stages:

1. **Retrieval**: Fetch the most relevant text chunks from a document store using vector similarity search.
2. **Generation**: Use a language model to generate answers based on both the retrieved context and the user query.

## 🛠️ Technologies Used

- **LangChain**: Orchestrates the RAG components (embedding, vector store, LLM).
- **FAISS**: Vector store for similarity search over document embeddings.
- **HuggingFace**: Used to load IBM Granite embedding and language models.
- **IBM Granite**: Enterprise-grade transformer models for embeddings and generation.
- **Python & VS Code**: Runtime and IDE for development.

## 📂 Files Used in This Project

- `state_of_the_union.txt`: A sample speech used for document retrieval.
- `README.md`: This file — describing the project.
- `rag_pipeline.py`: The main Python script that loads documents, indexes them, and answers questions.
- `.env`: Contains API keys needed for HuggingFace Hub access.

## 🚀 Example Query

Query: What is RAG architecture?

Response:
{
  "query": "What is RAG architecture?",
  "result": "RAG architecture, or Retrieval-Augmented Generation, is a method that integrates document retrieval with language generation. It enhances the accuracy of responses by anchoring them in concrete, pertinent context from external data sources, rather than relying solely on the model's internal knowledge. In this project, LangChain orchestrates the RAG components, including embedding (using IBM Granite models loaded via HuggingFace), vector store (utilizing FAISS for similarity search over document embeddings), and the language model (again, IBM Granite). The Python runtime with VS Code is used for development."
}
## 📌 Usage Note

This is a simplified pipeline to demonstrate RAG. It uses offline document embeddings and open APIs to help developers quickly prototype question-answering systems powered by retrieval and LLMs.
