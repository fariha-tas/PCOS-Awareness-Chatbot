# PCOS Awareness Chatbot

A beginner-friendly **RAG-based chatbot** that answers questions about PCOS (Polycystic Ovary Syndrome) using your own documents as a knowledge base.

## This is a very small level project that uses simple information text files (from Wikipedia and Mayo Clinic) as knowledge.

This chatbot is built using:
- [LangChain](https://www.langchain.com/) – for building the retrieval and chain logic
- [FAISS](https://github.com/facebookresearch/faiss) – for storing and searching embeddings
- [HuggingFace Transformers](https://huggingface.co/) – for generating natural language answers
- [PyPDF / Text Loaders](https://pypdf.readthedocs.io/) – for loading documents
- [Sentence-Transformers](https://www.sbert.net/) – for embedding documents

> ⚠️ **Note:** This chatbot is for educational purposes and awareness only. It does **not provide medical advice**.

---

## Installation (Google Colab)

1. Open [Google Colab](https://colab.research.google.com/).
2. Clone this repository or upload your notebook.
3. Install dependencies:

```python
!pip install -q langchain==0.1.20 langchain-community==0.0.38 langchain-text-splitters==0.0.1 faiss-cpu sentence-transformers pypdf transformers
