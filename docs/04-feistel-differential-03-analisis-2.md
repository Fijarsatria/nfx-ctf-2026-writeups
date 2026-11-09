# Feistel Differential — Analisis

[← Overview](04-feistel-differential.md) · [Index](index.md)

## 2.3 Mengapa 7 pasangan cukup

Total unknown = 7 × 16 = 112 bit. Satu pasangan `(p, c1)` memberi 32 bit
output, dan pasangan keduanya memberi 32 bit tambahan. Secara informasi,
6 pasangan (384 bit observasi) seharusnya sudah lebih dari cukup, tetapi
**tidak semua bit key teramati** karena struktur Feistel: beberapa subkey
hanya memengaruhi output melalui kombinasi tertentu, sehingga model z3 masih
punya beberapa solusi yang cocok pada 6 pasangan.

Hasil empiris:

| Jumlah pasangan | Status z3 | Kecocokan pada blok 0 |
|---:|---|---:|
| 6 | SAT | 11.183 / 20.000 |
| 7 | SAT | 20.000 / 20.000 |

Dengan 7 pasangan, model terpaku ke key yang benar. Ini juga menunjukkan
bahwa "differential" di data sebenarnya tidak wajib dieksploitasi secara
statistik: known-plaintext saja sudah cukup karena key space-nya kecil.

## 2.4 Differential sebagai validasi tambahan

Walaupun solver memakai known-plaintext, struktur diferensial berguna untuk
verifikasi: untuk setiap Δ, ciphertext difference `c1 XOR c2` harus konsisten
dengan key. Solver akhir mengecek **kedua** ciphertext pada semua 280.000
baris, bukan hanya 7 baris yang dipakai menyelesaikan model.
