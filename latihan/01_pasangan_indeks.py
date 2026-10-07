# Counter menghitung banyak pasangan.
count = 0

# Loop luar mengatur i dari 1 sampai 3.
for i in range(1, 4):
    # Loop dalam mengatur j dari 1 sampai 4.
    for j in range(1, 5):
        print(i, j)
        count += 1

# Tampilkan banyak pasangan setelah semua iterasi selesai.
print(f"Banyak pasangan = {count}")