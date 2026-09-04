from pathlib import Path

folder = Path("documents")

# List kosong untuk menyimpan file yang berhasil dibaca
successful_files = []

for file in folder.rglob("*.txt"):
    try:
        with open(file, "rb") as f:
            data = f.read()
        print(f"Found document: {file} ")

        # Memasukkan file ke dalam list
        successful_files.append(file)
    except Exception as e:
        print(e)

print(f"Total dokumen: {len(successful_files)}")
