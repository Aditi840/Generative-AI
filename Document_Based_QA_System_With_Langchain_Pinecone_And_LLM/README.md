**Document Processing & Retrieval with LangChain**

**Overview**

This project leverages LangChain, Pinecone, and Hugging Face models to load, process, and retrieve documents efficiently. It enables text embedding, vector search, and context-aware query answering.

**Installation**

Ensure you have the necessary dependencies installed:

pip install --upgrade langchain openai unstructured sentence-transformers pinecone-client transformers langchain-community

pip install detectron2@git+https://github.com/facebookresearch/detectron2.git@v0.6#egg=detectron2
apt-get install poppler-utils
from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Pinecone
from transformers import pipeline

**API Keys**

Ensure your OpenAI and Pinecone API keys are set in your environment before running the code.

**Notes**

Replace placeholder API keys with your actual credentials.
Ensure you have sufficient system resources for model execution.

**License**

This project is open-source. Modify and use as needed!


