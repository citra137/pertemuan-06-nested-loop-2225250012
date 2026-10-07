print("Tabel Perkalian dan Statistik")
n = int(input("n: "))

# Minta input kembali sampai n positif.
while n <= 0:
    print("n harus positif.")
    n = int(input("n: "))

# Akumulator dan counter untuk seluruh tabel.
total_semua = 0
count_genap = 0

# Loop luar menentukan baris.
for i in range(1, n + 1):
    # Reset jumlah pada awal setiap baris.
    total_baris = 0

    # Loop dalam menentukan kolom.
    for j in range(1, n + 1):
        hasil = i * j
        print(f"{hasil:4}", end="")

        # Jumlahkan nilai per baris dan keseluruhan.
        total_baris += hasil
        total_semua += hasil

        # Hitung banyak hasil perkalian yang genap.
        if hasil % 2 == 0:
            count_genap += 1

    print(f"   | jumlah baris = {total_baris}")

# Statistik ditampilkan setelah seluruh tabel selesai.
print(f"Total seluruh hasil = {total_semua}")
print(f"Banyak hasil genap = {count_genap}")