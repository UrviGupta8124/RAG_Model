import os
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import Replicate
from langchain.chains import RetrievalQA
from ibm_granite_community.notebook_utils import get_env_var

# Load environment variables once when the module loads
load_dotenv()

# Initialize all your static resources once here (so you don't reload every query)

# 1. Load documents
loader = TextLoader("sample_docs/state_of_the_union.txt", encoding="utf-8")
documents = loader.load()

# 2. Split into chunks
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_documents(documents)

# 3. Load embedding model
embedding_model = HuggingFaceEmbeddings(
    model_name="ibm-granite/granite-embedding-30m-english"
)

# 4. Create FAISS vector DB
vector_db = FAISS.from_documents(texts, embedding_model)

# 5. Load LLM from Replicate
llm = Replicate(
    model="ibm-granite/granite-3.3-8b-instruct",
    replicate_api_token=get_env_var("REPLICATE_API_TOKEN")
)

# 6. Create Retrieval QA chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=vector_db.as_retriever()
)


def run_query(query: str) -> str:
    """Run a query through the retrieval QA chain and return the response."""
    response = qa_chain.run(query)
    return response
