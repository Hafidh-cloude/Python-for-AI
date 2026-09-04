from pathlib import Path

folder = Path("documents")

# Cek folder ada (True) atau tidak (False)
print(folder.exists())
# Mencari file
for file in folder.iterdir():
    print(file)
# Mencari PDF/txt/lainnya termasuk subfolder
for file2 in folder.rglob("*.txt"):
    print(file2)
