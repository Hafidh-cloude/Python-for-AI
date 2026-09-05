from pathlib import Path


class PDFLoader:
    def __init__(self, folder_path):
        # Menyimpan folder_path ke atribut objek
        self.folder_path = folder_path

    def load(self):
        # Ubah string folder_path menjadi objek Path
        folder = Path(self.folder_path)

        # Validasi folder
        if not folder.exists():
            print(f"FOLDER '{self.folder_path}' tidak ditemukan")
            return []

        # List kosong untuk menampung hasil
        documents = []

        # Mencari semua file .pdf
        for file in folder.rglob("*.pdf"):
            # Menambahkan file ke dalam list document
            documents.append(file)
        # Mengembalikan list yang sudah terisi
        return documents


loader = PDFLoader("../Day_4/documents")
documents = loader.load()

print(f"Total: {len(documents)}")
