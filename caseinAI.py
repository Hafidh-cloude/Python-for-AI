name = input("Masukkan nama Anda:")

while True:

    question = input(f"Silakan bertanya {name}: ")

    if question == "":
        print("Pertanyaan tidak boleh kosong")
    else:
        print("Pertanyaan diterima")

    choice = input("Apakah sudah selesai y/n?: ")

    if choice == "y":
        print(f"Program dihentikan, terimakasih {name}")
        break
