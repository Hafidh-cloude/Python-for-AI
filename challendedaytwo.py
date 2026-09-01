import os

documents = [
    {
        "title": "Introduction to RAG",
        "source": "rag.pdf",
        "score": 0.95,
    },
    {
        "title": "Vector Database",
        "source": "vector.pdf",
        "score": 0.90,
    },
    {
        "title": "Embedding",
        "source": "embedding.pdf",
        "score": 0.85,
    },
]

for document in documents:
    print(f"Title: {document['title']} | Score: {document['score']}")
