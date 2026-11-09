# Dokodemo Door — Evidence / Bukti

[← Overview](28-dokodemo-door.md) · [Index](index.md)


## Arsip Evidence

> Semua file di bawah berasal dari folder `assets/dokodemo-door/`. Screenshot ditempel langsung; file teks/script ditautkan.

### Screenshot

![04-page-image.jpg](assets/dokodemo-door/04-page-image.jpg)

### Transkrip / file pendukung

- [`01-solve-output.txt`](assets/dokodemo-door/01-solve-output.txt)
- [`02-extracted-text.txt`](assets/dokodemo-door/02-extracted-text.txt)
- [`03-decrypted.pdf`](assets/dokodemo-door/03-decrypted.pdf)
- [`extract_text.py`](assets/dokodemo-door/extract_text.py)
- [`solve_dokodemo.py`](assets/dokodemo-door/solve_dokodemo.py)

## Tabel Evidence

Semua bukti berada di `writeups/assets/dokodemo-door/`.

| Bukti | File | Keterangan |
|---|---|---|
| Output solver | `01-solve-output.txt` | Panjang key, key, header/trailer, hash |
| Teks PDF | `02-extracted-text.txt` | Hasil decode content stream, termasuk flag |
| PDF terdekripsi | `03-decrypted.pdf` | File asli setelah XOR |
| Gambar halaman | `04-page-image.jpg` | Gambar yang tertanam di PDF |
| Solver | `solve_dokodemo.py` | Script crib-drag yang dijalankan |
| Ekstraktor teks | `extract_text.py` | Decoder ASCII85 + Flate + operator `Tj` |
