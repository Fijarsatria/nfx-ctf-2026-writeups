# 13 Is Not Enough — analisis transformasi (2026-11-13)

Flag accepted:

```text
NFX{Y0U_R0T4T3D_TH3_L3TT3R5_N0W_F1X_TH3_D1G1T5}
```

Ciphertext brief:

```text
p5J9Y9\R;XJRF9^RG>LR5H;JJ;TR;XJR\;J:J>HRE>AvF^L
```

Keduanya 47 karakter.

## Hasil percobaan

Semua ini dijalankan dan **tidak** menghasilkan flag:

- ROT13, ROT5, ROT13+ROT5, ROT5+ROT13, ROT47
- Atbash, reverse
- affine atas printable ASCII 95 (`a,b` semua kombinasi yang coprime)
- affine atas alfabet 26/36/37 karakter
- keyboard fisik QWERTY ↔ Dvorak ↔ Colemak (per baris, bukan concat)
- kombinasi ROT13/ROT5 dengan layout keyboard
- rail fence 2–24 rel
- columnar transposition lebar 2–23
- XOR/add dengan key: `13`, `thirteen`, `rot13`, `rot5`, `notenough`,
  `digits`, `letters`, `NFX`, `1337`, `fix`, `key`
- Vigenère atas printable/alfanumerik dengan key di atas
- PRNG Python `random.Random(13)` / `"13"` / `1337`, XOR dan add

ROT13+ROT5 menghasilkan:

```text
c0W4L4\E;KWES4^ET>YE0U;WW;GE;KWE\;W:W>UER>NiS^Y
```

Itu bukan flag.

## Yang bisa disimpulkan

- Flag accepted, tetapi **transformasi persisnya belum ditemukan**.
- Ciphertext tidak monoalfabetik: satu karakter ciphertext memetakan ke
  beberapa karakter flag (contoh `J` → `X/W/3/T`).
- Tidak ada bukti bahwa ciphertext adalah encoding langsung dari flag.
  Bisa jadi ciphertext adalah pesan petunjuk terpisah, dan flag adalah
  jawaban meta dari judul/deskripsi.
- Jangan menulis "ROT13+ROT5" sebagai metode final. Tulis apa adanya:
  **metode belum direproduksi**.

## File

- `attempts.py` — semua percobaan di atas (bisa dijalankan ulang)
- `ciphertext.txt` — ciphertext dan target
