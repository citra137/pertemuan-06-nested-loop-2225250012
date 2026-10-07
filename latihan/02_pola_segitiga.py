n = int(input("n: "))

# Loop luar menentukan baris.
for i in range(1, n + 1):
    # Loop dalam mencetak i bintang pada baris ke-i.
    for j in range(i):
        print("*", end=" ")

    # Pindah baris setelah satu baris selesai.
    print()