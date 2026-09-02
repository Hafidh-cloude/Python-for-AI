# DISKON BELANJA

# Tanpa menggunakan function

diskon = 0.1
min_purchase = 50000

print("=== Tanpa menggunakan function ===")
total_1 = 100000
if total_1 > min_purchase:
    bayar_1 = total_1 - (total_1 * diskon)
    print(f"Total belanja: {bayar_1}")
else:
    print(f"Total belanja: {total_1}")

total_2 = 190000
if total_2 > min_purchase:
    bayar_2 = total_2 - (total_2 * diskon)
    print(f"Total belanja: {bayar_2}")
else:
    print(f"Total belanja: {total_2}")

total_3 = 40000
if total_3 > min_purchase:
    bayar_3 = total_3 - (total_3 * diskon)
    print(f"Total belanja: {bayar_3}")
else:
    print(f"Total belanja: {total_3}")


# Menggunakan function
print("\n=== Menggunakan function ===")


# Buat fanction 1 kali
def hitung_diskon(total_belanja):
    if total_belanja > min_purchase:
        return total_belanja - (total_belanja * diskon)
    else:
        return total_belanja


# Pangil fanction berkali-kali
print(f"Pelanggan 1 bayar: {hitung_diskon(200000)}")
print(f"Pelanggan 2 bayar: {hitung_diskon(45000)}")
print(f"Pelanggan 3 bayar: {hitung_diskon(100000)}")
print(f"Pelanggan 4 bayar: {hitung_diskon(50000)}")
