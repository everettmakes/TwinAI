

# Twin AI - combines LLAMA llm and Langchain.

*A Retrieval-Augmented Generation (RAG) system powered by LLaMA 3.2 and Ollama.*

---

> “Sometimes I experience mild existential angst.
> So I built an **AI twin** — to help me maintain a sense of identity and creativity.”

---

<div align="center">
  <img src="https://raw.githubusercontent.com/github/explore/main/topics/llm/llm.png" width="160" alt="LLM icon" />
  <img src="https://raw.githubusercontent.com/github/explore/main/topics/python/python.png" width="160" alt="Python logo" />
</div>

---

## 🪶 Overview

**Lama-RAG-AI-Twin** is a lightweight, local-first **AI persona project** that combines:

* 🦙 **LLaMA 3.2** (via [Ollama](https://ollama.ai/))
* 🔍 **LangChain RAG pipeline**
* 💾 **Chroma vector store**
* 📄 **Custom document embeddings**

---

## 🧩 Architecture

```
User Query
   ↓
RAG Pipeline (LangChain / LlamaIndex)
   ├─ Retriever → Vector Database (Chroma)
   │     └─ Embeddings of your curated documents
   └─ LLM → Generates responses using retrieved context + prompt
   ↓
Response to User
```

<div align="center">
  <img src="/Users/josh/Documents/personal/code/TwinAI/twin-ai/c0bb024c-b1a0-488e-a899-664d0f2a5ac6.png" width="700" alt="Architecture diagram (placeholder)" />
  <p><i>(Architecture diagram)</i></p>
</div>

---

## ⚙️ Setup Instructions

### 🪄 1. Create and Activate Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 🦙 2. Pull Ollama Models

Make sure you have [Ollama](https://ollama.ai/) installed and running locally.

```bash
ollama pull llama3.2
ollama pull mxbai-embed-large
```

---

### 📦 3. Install Requirements

```bash
pip install -r ./requirements.txt
```

### 🚀 5. Run the App

```bash
python main.py
```

---

## 🧩 Core Components

| Component     | Description                         |
| ------------- | ----------------------------------- |
| **LangChain** | Orchestrates the RAG pipeline       |
| **Ollama**    | Runs local LLaMA 3.2 and embeddings |
| **Chroma**    | Persistent vector database          |

---

## 🪪 License

This project uses [LLaMA 3.2](https://www.llama.com/llama3_2/license/), which is subject to Meta’s license terms.

---

## 🧰 Example Extensions

You can easily extend this project to:

* 💬 Power your **personal knowledge chatbot**
* 📚 Create a **document-aware assistant**
* 🧍‍♂️ Build a **personal AI twin** that mirrors your writing style
* 🧾 Analyze reviews or sentiment dynamically
* 🌐 Wrap it with **Streamlit** or **Gradio** for a full web interface

---

<div align="center">

✨ *Build your twin. Train your context.
Let your data speak with your voice.* ✨

</div>

---
