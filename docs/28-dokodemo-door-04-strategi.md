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

![04-page-image.jpg](assets/dokodemo-door/04-page-image.jpg)

*Evidence — `04-page-image.jpg`.*
