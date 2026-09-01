name = input("Masukkan nama Anda: ")
hour = int(input("Masukkan lama belajar dalam jam: "))

if hour >= 3:
    print("Belajar sangat baik")
elif hour >= 1:
    print("Lumayan, teruskan")
else:
    print("Harus lebih konsisten")

for i in range(1, 6):
    print(f"Progres {i}")
