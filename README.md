# RAG Model with Flask and LangChain

This project is a simple Retrieval-Augmented Generation (RAG) application built using Flask and LangChain. It loads a text document, splits it into chunks, stores embeddings in a FAISS vector database, and uses an LLM to answer user queries based on the document content.

# 🚀 Features

Flask Web App for an interactive UI.

LangChain-based pipeline for document processing and query answering.

FAISS for efficient vector similarity search.

HuggingFace Embeddings with ibm-granite/granite-embedding-30m-english.

Replicate API to run the ibm-granite/granite-3.3-8b-instruct LLM.

Environment Variables managed with python-dotenv.

IBM Granite Community Utils for helper functions like get_env_var

# 📂 Project Structure
```plaintext
├── Screenshots/                # Project screenshots for documentation
├── sample_docs/                 # Sample text documents
│   └── state_of_the_union.txt
├── static/                      # Static files (CSS, images, JS)
│   └── style.css                # Stylesheet (optional)
├── templates/                   # HTML templates for Flask
│   └── index.html
├── .gitignore                   # Git ignore file
├── README.md                    # Project documentation
├── app.py                       # Flask application
├── rag_pipeline.py              # RAG pipeline with LangChain
└── requirements.txt             # Python dependencies
```

# ⚙️ Installation
### Clone the repository

```git clone https://github.com/<your-username>/<your-repo>.git```
```cd <your-repo>```

### Create a virtual environment

```python -m venv venv```
#### For Linux/Mac
```source venv/bin/activate```
#### For Windows
```venv\Scripts\activate```

### Install dependencies

```pip install -r requirements.txt```

### Set up environment variables
Create a .env file in the project root:

```REPLICATE_API_TOKEN=your_replicate_api_key```

### Running the App
```python app.py```

Open your browser and go to:
```http://127.0.0.1:5000```


# 📝 How It Works
Loads a text document from sample_docs/state_of_the_union.txt.

Splits the document into smaller chunks for processing.

Embeds the text using a HuggingFace model.

Stores embeddings in a FAISS vector database.

Uses an LLM from Replicate to generate responses for user queries.

Displays results on a Flask-powered web interface.

# 📦 Dependencies
Flask

LangChain

FAISS

HuggingFace Embeddings

Replicate API

python-dotenv

IBM Granite Community Utils  (`git+https://github.com/ibm-granite-community/utils`)

# 📜 License
This project is licensed under the MIT License. Feel free to use and modify it.
