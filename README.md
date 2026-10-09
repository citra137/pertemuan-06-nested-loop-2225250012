# Pertemuan 06: Nested Loop dalam Python

## Identitas
- Nama: Aulia Citra Aljazeera Jan's
- NIM: 2225250012
- Kelas: 3F
- Program Studi: S1 Pendidikan Matematika
- Mata Kuliah: Algoritma dan Pemrograman
- Dosen Pengampu: Dr. Aan Hendrayana, S.Si., M.Pd.

## Tujuan
Menggunakan nested loop untuk menampilkan pasangan indeks,
membentuk pola, menjumlahkan nilai, dan menghitung banyak
pasangan yang memenuhi kondisi tertentu.

## Cara Menjalankan

Buka terminal VS Code pada folder utama proyek, lalu jalankan salah satu perintah berikut:

```powershell
py latihan/01_pasangan_indeks.py
py latihan/02_pola_segitiga.py
py latihan/03_jumlah_per_baris.py
py latihan/04_hitung_pasangan.py
py tugas/tabel_perkalian_dan_statistik.py
```

Jalankan setiap perintah secara terpisah. Jika program meminta nilai n, masukkan bilangan bulat sesuai pengujian.

## Algoritma Tugas 3: Tabel Perkalian dan Statistik

1. Membaca bilangan bulat n.
2. Meminta input kembali selama n kurang dari atau sama dengan nol.
3. Mengatur total_semua dan count_genap menjadi nol sebelum kedua loop.
4. Menjalankan loop luar dengan i dari 1 sampai n untuk menentukan baris.
5. Mengatur total_baris menjadi nol pada awal setiap baris.
6. Menjalankan loop dalam dengan j dari 1 sampai n untuk menentukan kolom.
7. Menghitung hasil = i * j, kemudian menampilkannya.
8. Menambahkan hasil ke total_baris dan total_semua.
9. Menambahkan count_genap sebesar satu jika hasil habis dibagi dua.
10. Menampilkan jumlah setiap baris setelah loop dalam selesai.
11. Menampilkan total keseluruhan dan banyak hasil genap setelah kedua loop selesai.

Loop luar mengatur baris, sedangkan loop dalam mengatur kolom.
total_baris menyimpan jumlah pada satu baris dan direset setiap berganti baris.
total_semua menyimpan jumlah seluruh hasil perkalian.
count_genap menghitung banyak hasil perkalian yang genap.

## Hasil Pengujian Latihan

| Program | Input | Hasil yang Diharapkan | Hasil Aktual | Status |
|---|---|---|---|---|
| Latihan 1 | Tanpa input | 12 pasangan, count = 12 | 12 pasangan, count = 12 | Lulus |
| Latihan 2 | n = 1 | 1 baris, berisi 1 bintang | 1 baris, berisi 1 bintang | Lulus |
| Latihan 2 | n = 3 | 3 baris, berisi 1, 2, dan 3 bintang | 3 baris, berisi 1, 2, dan 3 bintang | Lulus |
| Latihan 2 | n = 5 | 5 baris, berisi 1 sampai 5 bintang | 5 baris, berisi 1 sampai 5 bintang | Lulus |
| Latihan 3 | Tanpa input | Jumlah baris: 6, 12, 18, 24 | Jumlah baris: 6, 12, 18, 24 | Lulus |
| Latihan 4 | n = 2 | 1 pasangan memenuhi syarat | 1 pasangan memenuhi syarat | Lulus |
| Latihan 4 | n = 3 | 3 pasangan memenuhi syarat | 3 pasangan memenuhi syarat | Lulus |
| Latihan 4 | n = 5 | 10 pasangan memenuhi syarat | 10 pasangan memenuhi syarat | Lulus |

## Hasil Pengujian Tugas 3

| Input | Hasil yang Diharapkan | Hasil Aktual | Status |
|---|---|---|---|
| n = 1 | Jumlah baris: 1; total: 1; hasil genap: 0 | Jumlah baris: 1; total: 1; hasil genap: 0 | Lulus |
| n = 2 | Jumlah baris: 3, 6; total: 9; hasil genap: 3 | Jumlah baris: 3, 6; total: 9; hasil genap: 3 | Lulus |
| n = 3 | Jumlah baris: 6, 12, 18; total: 36; hasil genap: 5 | Jumlah baris: 6, 12, 18; total: 36; hasil genap: 5 | Lulus |
| 0, -2, lalu 2 | Input 0 dan -2 diminta ulang; input 2 menghasilkan total 9 dan 3 hasil genap | Input 0 dan -2 diminta ulang; input 2 menghasilkan total 9 dan 3 hasil genap | Lulus |

Seluruh kasus pengujian di atas menghasilkan keluaran sesuai dengan hasil yang diharapkan.

## Tracing Latihan 4 untuk n = 3

Nilai awal count = 0. Setiap pasangan diperiksa menggunakan kondisi i + j <= 3.

| Langkah | i | j | i + j | Kondisi Terpenuhi? | count Setelah Pemeriksaan |
|---|---|---|---|---|---|
| 1 | 1 | 1 | 2 | Ya | 1 |
| 2 | 1 | 2 | 3 | Ya | 2 |
| 3 | 1 | 3 | 4 | Tidak | 2 |
| 4 | 2 | 1 | 3 | Ya | 3 |
| 5 | 2 | 2 | 4 | Tidak | 3 |
| 6 | 2 | 3 | 5 | Tidak | 3 |
| 7 | 3 | 1 | 4 | Tidak | 3 |
| 8 | 3 | 2 | 5 | Tidak | 3 |
| 9 | 3 | 3 | 6 | Tidak | 3 |

Dari sembilan pasangan yang diperiksa, tiga memenuhi kondisi:
(1, 1), (1, 2), dan (2, 1). Nilai akhir count adalah 3.

## Tracing Tugas 3 untuk n = 2

Nilai awal total_semua = 0 dan count_genap = 0.
total_baris direset menjadi 0 pada awal setiap baris.
Nilai dalam tabel dicatat setelah hasil perkalian diproses.

| i | j | hasil | total_baris | total_semua | count_genap |
|---|---|---|---|---|---|
| 1 | 1 | 1 | 1 | 1 | 0 |
| 1 | 2 | 2 | 3 | 3 | 1 |
| 2 | 1 | 2 | 2 | 5 | 2 |
| 2 | 2 | 4 | 6 | 9 | 3 |

Saat i berubah menjadi 2, total_baris direset menjadi 0.
total_semua dan count_genap tetap menyimpan hasil sebelumnya.
Hasil akhirnya adalah jumlah baris 3 dan 6, total keseluruhan 9,
serta 3 hasil perkalian genap.

## Analisis Efisiensi

Untuk input positif n, loop luar berjalan n kali dan loop dalam
berjalan n kali pada setiap iterasi loop luar. Jadi, badan loop
dalam dijalankan sebanyak n × n = n² kali.

Contohnya, n = 1 menghasilkan 1 pasangan,
n = 2 menghasilkan 4 pasangan, dan
n = 3 menghasilkan 9 pasangan.

Pada setiap pasangan, hasil perkalian dihitung satu kali.
Nilai tersebut langsung digunakan untuk tampilan tabel,
jumlah baris, total keseluruhan, dan pemeriksaan hasil genap.
Dengan demikian, tidak diperlukan loop tambahan untuk
menghitung ulang statistik.

Ketika n membesar, bagian loop dalam melakukan paling banyak
operasi karena dijalankan sebanyak n² kali.

## Refleksi

Kesalahan nested loop yang ditemukan adalah kesalahan dalam menentukan lokasi inisialisasi akumulator.

Pada perhitungan jumlah setiap baris, variabel total_baris harus direset pada awal setiap iterasi loop luar sebelum loop dalam berjalan. Jika total_baris tidak direset, maka nilai dari baris sebelumnya akan ikut terbawa sehingga jumlah setiap baris menjadi tidak sesuai.

Perbaikannya adalah menempatkan total_baris = 0 di dalam loop luar sebelum loop dalam. Sementara itu, total_semua tidak boleh direset setiap baris karena digunakan untuk menyimpan jumlah seluruh hasil perkalian. Oleh karena itu, total_semua harus diinisialisasi sebelum kedua loop.