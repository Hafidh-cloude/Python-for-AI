class Document:
    def __init__(self, title, score):
        self.title = title
        self.score = score

    def show_info(self):
        return f"Title: {self.title} \nScore: {self.score}"


document = Document("Intro to RAG", 0.92)
print(document.show_info())
