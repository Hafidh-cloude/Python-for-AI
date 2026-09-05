from pathlib import Path

folder = Path("documents")

# List untuk menghitung dengan len()

all_file = []
file_valid = []
file_corrupt = []

for file in folder.rglob("*"):
    # Mencari file txt dan csv
    if file.is_file() and file.suffix in [".txt", ".csv"]:
        all_file.append(file)

        try:
            # Baca isi teks
            with open(file, "r", encoding="utf-8") as f:
                text_content = f.read()

            # Cek kata "LUNAS" dalam file
            if "lunas" in text_content.lower():
                print(f"Berhasil, file valid: {file.name}")
                file_valid.append(file)
            else:
                print(f"Rejected, tidak ada status LUNAS: {file.name}")
                file_corrupt.append(file)

        except Exception as e:
            print(f"Error, gagal membaca {file.name}: {e}")
            file_corrupt.append(file)

# Cetak rangkuman menggunakan len()

print("\n===Rangkuman Hasil===")
print(f"Total file ditemukan {len(all_file)}")
print(f"Total file valid {len(file_valid)}")
print(f"Total file bermasalah {len(file_corrupt)}")
