# 13 Is Not Enough — Referensi

[← Overview](77-13-is-not-enough.md) · [Index](index.md)

> **Langkah 5/5 — Referensi.** XOR, reverse, ROT13, dan rotasi digit.
>
> **Titik penting:** `13` bukan hanya ROT13; dipakai juga sebagai key XOR.
>
> **Selesai.** Kembali ke [Overview](77-13-is-not-enough.md).

## Transformasi yang dipakai

| Layer | Nama | Penjelasan singkat |
|---:|---|---|
| 1 | XOR `0x0D` | Setiap byte di-XOR dengan 13 (`0x0D`). |
| 2 | Reverse | Urutan string dibalik. |
| 3 | ROT13 | Huruf A–Z/a–z digeser 13 posisi. |
| 4 | Digit `-3` | Digit 0–9 digeser mundur 3 posisi (mod 10). |

## Kenapa ROT13+ROT5 langsung gagal?

ROT13 hanya mengubah huruf; ROT5 hanya mengubah digit. Kalau keduanya
diterapkan langsung ke ciphertext, hasilnya:

```text
c0W4L4\E;KWES4^ET>YE0U;WW;GE;KWE\;W:W>UER>NiS^Y
```

Bukan flag. Ciphertext ini masih ter-XOR 13 dan ter-reverse. Setelah dua
layer itu dibuka, baru ROT13 masuk akal (prefix `ASK` → `NFX`).

## Bacaan lanjutan

- ROT13 — Caesar cipher dengan shift 13.
- ROT5 / ROT18 — rotasi digit dan kombinasi ROT13+ROT5.
- XOR cipher — operasi bitwise yang simetris (`a ^ k ^ k = a`).
- Leetspeak — substitusi angka ke huruf (0=O, 1=I/L, 3=E, 4=A, 5=S).
