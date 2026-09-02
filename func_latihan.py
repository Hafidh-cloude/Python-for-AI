def greet(name):
    return f"Halo, {name}!"


# Memanggil
pesan = greet("Dunia")
print(pesan)


# AI CONTEXT
def create_prompt(question):
    return f"Jawab pertanyaan ini: {question}"


prompt = create_prompt("Apa itu RAG?")
print(prompt)
