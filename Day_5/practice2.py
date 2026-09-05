class Students:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Menambahkan method
    def introduce(self):
        return f"Hallo, saya {self.name} dan umur saya {self.age}"


student = Students("Hafidh", 12)

intro_myself = student.introduce()
print(intro_myself)
