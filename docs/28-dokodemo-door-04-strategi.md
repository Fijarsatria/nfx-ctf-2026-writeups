# Dokodemo Door — Strategi

[← Overview](28-dokodemo-door.md) · [Index](index.md)

## 3.1 Strategi

1. Baca ciphertext.
2. Untuk setiap panjang key 1..64, turunkan byte key dari header dan trailer.
3. Tolak panjang key yang menyebabkan konflik.
4. Jika hanya tersisa ≤2 byte key yang belum diketahui, brute-force dan skor.
5. Dekripsi seluruh file, verifikasi magic PDF dan trailer.
6. Decode content stream (`ASCII85` → `Flate`) dan ambil operator `Tj`.

### Evidence langkah ini

![term-01-solve-output.png](assets/dokodemo-door/term-01-solve-output.png)

*Terminal evidence — `01-solve-output.txt` (arsip transkrip sesi solve).*

![term-02-extracted-text.png](assets/dokodemo-door/term-02-extracted-text.png)

*Terminal evidence — `02-extracted-text.txt` (arsip transkrip sesi solve).*

**Berkas mentah langkah ini:**

- [`01-solve-output.txt`](assets/dokodemo-door/01-solve-output.txt)
- [`02-extracted-text.txt`](assets/dokodemo-door/02-extracted-text.txt)
