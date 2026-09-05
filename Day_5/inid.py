class Document:
    def __init__(self, title, score):
        self.title = title
        self.score = score


document = Document("RAG", 0.90)
print(document.title)
print(document.score)
