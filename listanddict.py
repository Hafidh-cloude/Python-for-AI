documents = [
    {
        "title": "Introduction to RAG",
        "score": 0.95,
    },
    {
        "title": "RAG in AI Applications",
        "score": 0.90,
    },
    {
        "title": "RAG vs Traditional Methods",
        "score": 0.85,
    },
]

# Mengambil data index
print(documents[0])

# Mengambil data key
print(documents[0]["title"])

for document in documents:
    print(document["title"])
