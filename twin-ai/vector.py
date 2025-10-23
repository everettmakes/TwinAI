from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import json
import os

# Load personality JSON
with open("persona.json", "r") as f:
    persona = json.load(f)

embeddings = OllamaEmbeddings(model="mxbai-embed-large")

db_location = "./chroma_langchain_db"
add_documents = not os.path.exists(db_location)

if add_documents:
    documents, ids = [], []
    i = 0

    # Loop through top-level keys and values
    for key, value in persona.items():
        if isinstance(value, (str, list, dict)):
            content = json.dumps(value, indent=2)
            documents.append(Document(
                page_content=content,
                metadata={"section": key},
                id=str(i)
            ))
            ids.append(str(i))
            i += 1

# Create or load Chroma vector DB
vector_store = Chroma(
    collection_name="persona_knowledge",
    persist_directory=db_location,
    embedding_function=embeddings
)

# Add embeddings if first run
if add_documents:
    vector_store.add_documents(documents=documents, ids=ids)
    print(f"✅ Embedded {len(documents)} persona sections into vector DB.")

# Build retriever
retriever = vector_store.as_retriever(search_kwargs={"k": 5})
