# def greet(name):
#     return f"Halo, {name}!"


# # MemanggilW
# pesan = greet("Dunia")
# print(pesan)


# # AI CONTEXT
# def create_prompt(question):
#     return f"Jawab pertanyaan ini: {question}"


# prompt = create_prompt("Apa itu RAG?")
# print(prompt)

# Gabungan


# def validate_question(question):
#     if question == "":
#         return "False"
#     else:
#         return "True"

# print(validate_question(""))

# Mini Project


def validate_question(question):
    if question == "":
        return "Masukkan pertanyaan Anda!"
    else:
        return "Pesan diterima!"


input_qustion = input("Masukkan pertanyaan: ")

hasil = validate_question(input_qustion)

print(hasil)
