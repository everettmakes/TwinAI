# Lama-RAG-AI-Twin
Sometimes I experience mild existential angst. Thus, having an AI twin will help me maintain a sense of identity - making the world a better place. Since this is built upon llama, here is the license for llama3.2 - https://www.llama.com/llama3_2/license/


User Query
   ↓
Frontend Chat Interface (Web app: Streamlit/Gradio)
   ↓
RAG Pipeline (LangChain / LlamaIndex)
   ├─ Retriever → Vector Database (Pinecone, Weaviate, or FAISS)
   │     └─ Embeddings of your curated documents
   └─ LLM → Generates responses using retrieved context + prompt
   ↓
Response to User


----- MAKE AND ACTIVATE VIRTUAL ENVIRONMENT -----
make venv:
python3 -m venv venv

activate:
. venv/bin/activate

----- PULL OLLAMA MODELS -----
ollama pull llama3.2
ollama pull mxbai-embed-large

----- INSTALL REQUIREMENTS -----
pip3 install -r ./requirements.txt