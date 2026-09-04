from pathlib import Path

folder = Path("documents")

for file in folder.rglob("*.txt"):
    try:
        with open(file, "rb") as f:
            data = f.read()

        print(f"Berhasil membaca: {file}")

    except Exception as e:
        print(f"Gagal membaca {file}: {e}")
