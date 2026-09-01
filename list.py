documents = [
    "Laporan Tahunan Perusahaan 2023",
    "Rencana Strategis Bisnis 2024",
    "Analisis Pasar dan Tren Industri",
    "Panduan Pengembangan Produk Baru",
    "Laporan Keuangan Triwulan 1 2024",
]

# Mengambil data
print(documents[4])

# Mengubah data
documents[2] = "Analisis Pasar dan Tren Teknologi AI 2026"

# Menambahkan data
documents.append("Rencana Pemasaran Digital 2025")

# Menghapus data berdasarkan indeks
documents.remove(documents[2])

# Menghapus data berdasarkan nilai
documents.remove("Rencana Strategis Bisnis 2024")

# Mengetahui jumlah data
# print(len(documents))

for document in documents:
    print(document)
