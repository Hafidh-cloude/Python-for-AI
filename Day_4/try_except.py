# Menangani error / Error handling

# with open("data.txt", "r") as file:
#     text = file.read()  # Akan error karena data.txt tidak ada

# Memakai try / except
try:
    with open("data.txt", "r") as file:
        text = file.read()

# except FileNotFoundError:
#     print("File tidak ditemukan")

# except Exception as e
except Exception as e:
    print(e)
