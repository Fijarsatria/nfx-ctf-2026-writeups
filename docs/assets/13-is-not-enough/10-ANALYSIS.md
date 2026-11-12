# 13 Is Not Enough — analisis transformasi (final)

Ciphertext dari brief:

```text
p5J9Y9\R;XJRF9^RG>LR5H;JJ;TR;XJR\;J:J>HRE>AvF^L
```

Flag yang diterima platform:

```text
NFX{Y0U_R0T4T3D_TH3_L3TT3R5_N0W_F1X_TH3_D1G1T5}
```

Panjang ciphertext dan flag sama-sama **47 karakter**. Ini bukan ROT13+ROT5
langsung. Setelah dicoba, ada empat layer:

| Layer | Operasi | Hasil |
|---:|---|---|
| 1 | XOR setiap byte dengan `0x0D` (`13`) | `}8G4T4Q_6UG_K4S_J3A_8E6GG6Y_6UG_Q6G7G3E_H3L{KSA` |
| 2 | Reverse string | `ASK{L3H_E3G7G6Q_GU6_Y6GG6E8_A3J_S4K_GU6_Q4T4G8}` |
| 3 | ROT13 huruf | `NFX{Y3U_R3T7T6D_TH6_L6TT6R8_N3W_F4X_TH6_D4G4T8}` |
| 4 | Digit digeser `-3` mod 10 | `NFX{Y0U_R0T4T3D_TH3_L3TT3R5_N0W_F1X_TH3_D1G1T5}` |

## Kenapa langkahnya begitu?

1. **XOR 13.** Judul menyebut 13, dan ciphertext penuh simbol. XOR `0x0D`
   adalah percobaan termurah. Hasilnya berakhiran `{KSA`.
2. **Reverse.** `{KSA` yang berada di akhir adalah petunjuk bahwa string
   harus dibalik: setelah reverse muncul `ASK{...}`.
3. **ROT13.** `ASK` adalah ROT13 dari `NFX`. Setelah ROT13, semua huruf
   membaca, tetapi angka masih aneh (`Y3U`, `R3T7T6D`, ...).
4. **Digit -3.** Flag sendiri berbunyi “YOU ROTATED THE LETTERS, NOW FIX THE
   DIGITS”. Angka pada hasil ROT13 adalah `3,7,6,8,4`; untuk membentuk
   leetspeak yang benar (`0,4,3,5,1`) semuanya digeser -3 mod 10.

## Solver

```python
import codecs

ct = r"p5J9Y9\R;XJRF9^RG>LR5H;JJ;TR;XJR\;J:J>HRE>AvF^L"
s1 = "".join(chr(ord(c) ^ 13) for c in ct)
s2 = s1[::-1]
s3 = codecs.decode(s2, "rot_13")
flag = "".join(str((int(c) - 3) % 10) if c.isdigit() else c for c in s3)
print(flag)
```

Output:

```text
NFX{Y0U_R0T4T3D_TH3_L3TT3R5_N0W_F1X_TH3_D1G1T5}
```

## Catatan

- ROT13+ROT5 saja **tidak** cukup; ciphertext harus di-XOR 13 dan dibalik
  lebih dulu.
- Gambar pada brief hanya gambar meme/reaction; tidak ada payload tambahan
  yang diperlukan. Ciphertext lengkap ada di deskripsi challenge.
- Flag diverifikasi lewat form web platform: `CORRECT, BUT ALREADY SOLVED.`
