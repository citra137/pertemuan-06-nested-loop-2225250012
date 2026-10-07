n = int(input("n: "))

# Counter menghitung pasangan yang memenuhi syarat.
count = 0

# Kedua loop memeriksa pasangan i dan j dari 1 sampai n.
for i in range(1, n + 1):
    for j in range(1, n + 1):
        # Tambahkan counter jika i + j tidak melebihi n.
        if i + j <= n:
            count += 1

# Tampilkan banyak pasangan yang memenuhi syarat.
print(f"Banyak pasangan = {count}")