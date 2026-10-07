# Loop luar menentukan baris dari 1 sampai 4.
for i in range(1, 5):
    # Jumlah direset menjadi nol pada awal setiap baris.
    total_baris = 0

    # Loop dalam menghitung perkalian i dengan 1, 2, dan 3.
    for j in range(1, 4):
        total_baris += i * j

    # Tampilkan jumlah setelah satu baris selesai dihitung.
    print(f"Jumlah baris {i} = {total_baris}")