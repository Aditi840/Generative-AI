# -*- coding: utf-8 -*-
"""Document_Based_QA_System_With_Langchain_Pinecone_And_LLM.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ZjPEuOhz-12yRY6w8Q8-Gvv8QJQuziQn

# **1.Importing Libraries**
"""

!pip install --upgrade langchain openai -q

#!pip install senetence_transformers -q

import os
os.environ["OPENAI_API_KEY"] = "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"

!pip install unstructured -q
!pip install unstructured[local-inference] -q
!pip install detectron2@git+https://github.com/facebookresearch/detectron2.git@v0.6#egg=detectron2 -q

!apt-get install poppler-utils

pip install -U langchain-community

"""# **2.Loading Documents from a Directory Using LangChain**"""

from langchain.document_loaders import DirectoryLoader

directory = '/content/Data'

def load_docs(directory):
  loader = DirectoryLoader(directory)
  documents = loader.load()
  return documents

documents = load_docs(directory)
len(documents)

"""This code, loads all documents from a specified directory using LangChain’s DirectoryLoader."""

from langchain.text_splitter import RecursiveCharacterTextSplitter

def split_docs(documents, chunk_size=1000, chunk_overlap=20):
  text_splitter = RecursiveCharacterTextSplitter(chunk_size = chunk_size, chunk_overlap = chunk_overlap)
  docs = text_splitter.split_documents(documents)
  return docs

docs = split_docs(documents)
print(len(docs))

"""This code splits long documents into smaller chunks using LangChain’s RecursiveCharacterTextSplitter. Each chunk is 1000 characters long, with 20 characters overlapping for better context retention. The total number of chunks is printed. 🚀"""

print(docs[0].page_content)

# requires for open ai embedding
!pip install tiktoken -q

pip install -U sentence-transformers

"""# **3.Generating Text Embeddings with Hugging Face**"""

from sentence_transformers import SentenceTransformer

from langchain.embeddings import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2") # Lightweight and effective
query_result = embeddings.embed_query("Hello world")

print(len(query_result))  # Should return 384 (dimension size)

"""This code converts text into numerical embeddings using the all-MiniLM-L6-v2 model from Hugging Face. The embed_query() function generates a 384-dimensional embedding vector for the input "Hello world", and its length is printed."""

!pip install pinecone-client -q

pip install --upgrade pinecone-client

"""# **4.Setting Up and Using Pinecone for Vector Search**"""

import os
from pinecone import Pinecone, ServerlessSpec
from langchain.vectorstores import Pinecone as LangchainPinecone

# Set API key
api_key = "pcsk_383QVa_8xuhVYke5EmDwZnTuNKm3Qzv4aaUPn7ehmk5nYowQJRmgP46KBZXPVNSBV7urkZ"  # Replace with your actual Pinecone API key
os.environ["PINECONE_API_KEY"] = api_key  #  Ensure the key is available globally

# Initialize Pinecone
pc = Pinecone(api_key=api_key)

# Define the index name
index_name = "langchain-demo"

# Ensure the index exists
if index_name not in pc.list_indexes().names():
    pc.create_index(
        name=index_name,
        dimension=384,  # Ensure this matches your embedding model's output dimensions
        metric="cosine",
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"
        )
    )

# Connect to the existing index
index = pc.Index(index_name)  # Use index reference

# Ensure docs and embeddings are defined before using them
if "docs" not in locals() or "embeddings" not in locals():
    raise ValueError("Error: 'docs' or 'embeddings' is not defined!")

# initialize Langchain's Pinecone wrapper
vectorstore = LangchainPinecone.from_documents(
    documents=docs,
    embedding=embeddings,
    index_name=index_name
)

"""This code initializes Pinecone, creates an index (langchain-demo) if it doesn't exist, and connects it to LangChain for vector storage. It ensures docs and embeddings are defined before storing them in Pinecone for efficient similarity search."""

def get_similar_docs(query, k=2, score=False):
    if score:
        similar_docs = vectorstore.similarity_search_with_score(query, k=k)  #  Using vectorstore
    else:
        similar_docs = vectorstore.similarity_search(query, k=k)
    return similar_docs

query = "How does India's historical narrative differ from Western historiography"
similar_docs = get_similar_docs(query, score=True)
similar_docs

"""This function searches for the most relevant documents based on a query using Pinecone’s vector database. It returns the top k similar documents, optionally including similarity scores. The query searches for differences between India’s and Western historiography."""

from langchain.llms import OpenAI

# model_name = "text-davinci-003"
model_name = "gpt-3.5-turbo"
# model_name = "gpt-4"
llm = OpenAI(model_name=model_name)

pip install transformers langchain

from huggingface_hub import login
login("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")

"""# **5.Generating Context-Aware Answers with Mistral-7B and LangChain**"""

from transformers import pipeline
from langchain.chains import LLMChain
from langchain.llms import HuggingFacePipeline


from transformers import pipeline

# Load the model with authentication
hf_pipeline = pipeline(
    "text-generation",
    model="mistralai/Mistral-7B-Instruct-v0.2",
    token="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"  # Use your token here
)



#  Wrap in LangChain
llm = HuggingFacePipeline(pipeline=hf_pipeline)

from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

# Definining a prompt template
prompt = PromptTemplate(
    input_variables=["context", "question"],
    template="Use the following context to answer the question:\n\nContext: {context}\n\nQuestion: {question}\n\nAnswer:"
)

#  Load QA chain with prompt
chain = LLMChain(llm=llm, prompt=prompt)

def get_answer(query):
    similar_docs = get_similar_docs(query)  # Ensure `get_similar_docs()` works
    # print(similar_docs)
    context = "\n".join([doc.page_content for doc in similar_docs])  # Extract text from retrieved docs
    answer = chain.run(context=context, question=query)  # Pass context and question
    return answer

query = "How does India's historical narrative differ from Western historiography?"
response = get_answer(query)

print(response)

"""This code loads the Mistral-7B-Instruct model using Hugging Face, integrates it into LangChain, and sets up a QA pipeline. It retrieves similar documents for a given query, extracts relevant context, and generates a context-aware answer using the model."""

query = "What role did foreign conquests play in shaping India's political and social structure"
get_answer(query)

"""**Conclusion:**

This system leverages Hugging Face’s Mistral-7B-Instruct model, Pinecone for vector-based search, and LangChain for structured AI processing to create an intelligent knowledge retrieval system. The pipeline loads and processes text data, splits it into meaningful chunks, converts text into embeddings, and efficiently stores them in Pinecone for rapid similarity search. When a query is submitted, the system retrieves the most relevant documents, extracts key information, and generates a context-aware response using an LLM. By implementing optimized document filtering, response length control, and memory-efficient model loading, the system ensures smooth performance. This approach is ideal for automated customer support, academic research, enterprise knowledge management, and AI-driven assistants, making information retrieval more accurate and efficient.
"""

