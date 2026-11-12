# 13 Is Not Enough — Cara Mendapatkan Flag

[← Overview](77-13-is-not-enough.md) · [Index](index.md)

> **Langkah 2/5 — Cara Mendapatkan Flag.**
>
> **Flag:** `NFX{Y0U_R0T4T3D_TH3_L3TT3R5_N0W_F1X_TH3_D1G1T5}`
> **Status:** `VERIFIED` (flag), metode `UNVERIFIED`

## Ciphertext

```text
p5J9Y9\R;XJRF9^RG>LR5H;JJ;TR;XJR\;J:J>HRE>AvF^L
```

## Catatan jujur: ROT13+ROT5 belum cocok

Judul challenge (“13 Is Not Enough”) mengarah ke ROT13 + ROT5. Namun jika
keduanya diterapkan ke ciphertext:

```text
c0W4L4\E;KWES4^ET>YE0U;WW;GE;KWE\;W:W>UER>NiS^Y
```

Hasilnya **bukan** flag. Jadi masih ada layer/transform lain yang belum
direproduksi.

Flag yang diterima platform:

```text
NFX{Y0U_R0T4T3D_TH3_L3TT3R5_N0W_F1X_TH3_D1G1T5}
```

## Yang perlu dilengkapi

- Cari transformasi persis yang memetakan ciphertext → flag
  (bandingkan dengan known plaintext; cek substitusi/affine/Vigenère).
- Setelah ketemu, tulis recipe/langkahnya di sini.
- Jangan mengklaim “ROT13+ROT5” sebagai metode final tanpa output yang cocok.

## Bukti submit

Gunakan log API asli, bukan screenshot mockup.
