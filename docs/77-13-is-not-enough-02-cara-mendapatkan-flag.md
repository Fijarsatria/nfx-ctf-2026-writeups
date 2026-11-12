# 13 Is Not Enough — Cara Mendapatkan Flag

[← Overview](77-13-is-not-enough.md) · [Index](index.md)

> **Langkah 2/5 — Cara Mendapatkan Flag.** Empat layer: XOR 13, reverse,
> ROT13, lalu koreksi digit.
>
> **Flag:** `NFX{Y0U_R0T4T3D_TH3_L3TT3R5_N0W_F1X_TH3_D1G1T5}`
> **Status:** `VERIFIED` — metode terdokumentasi dan flag diterima platform.

## 1. Recon awal

Dari brief platform kita punya:

| Item | Nilai |
|---|---|
| Judul | `13 Is Not Enough` |
| Kategori | `Crypto` |
| Difficulty | `Easy` |
| Author | `Ariaf` |
| Format flag | `NFX{...}` |
| Ciphertext | `p5J9Y9\R;XJRF9^RG>LR5H;JJ;TR;XJR\;J:J>HRE>AvF^L` |

Panjang ciphertext **47 karakter**. Isinya campuran huruf besar/kecil, digit,
dan simbol (`\`, `^`, `>`, `;`, `:`). Karena format flag juga `NFX{...}`,
paling tidak kita tahu 5 karakter plaintext di awal (`N`, `F`, `X`, `{`) dan
1 karakter di akhir (`}`).

Judulnya jelas mengarah ke **ROT13**. Tapi “13 Is Not Enough” berarti ROT13
saja tidak cukup — masih ada layer lain.

> Gambar pada brief hanya reaction image; tidak ada payload tambahan yang
> diperlukan. Ciphertext lengkap ada di deskripsi challenge.

## 2. ROT13 dulu (dan hasilnya bukan flag)

```python
import codecs
ct = r"p5J9Y9\R;XJRF9^RG>LR5H;JJ;TR;XJR\;J:J>HRE>AvF^L"
print(codecs.decode(ct, "rot_13"))
```

Hasilnya:

```text
c5W9L9\E;KWES9^ET>YE5U;WW;GE;KWE\;W:W>UER>NiS^Y
```

Bukan flag. Berarti ROT13 bukan layer pertama, atau ada transformasi lain
sebelumnya.

## 3. Layer 1 — XOR dengan 13 (`0x0D`)

Judul menyebut angka **13**. Selain ROT13, angka 13 bisa dipakai sebagai key
XOR. Coba XOR setiap byte dengan `13` (`0x0D`):

```python
s1 = "".join(chr(ord(c) ^ 13) for c in ct)
print(s1)
```

Hasil:

```text
}8G4T4Q_6UG_K4S_J3A_8E6GG6Y_6UG_Q6G7G3E_H3L{KSA
```

Perhatikan bagian akhirnya: **`{KSA`**. Pada flag, `{` seharusnya ada di
awal dan `}` di akhir. Pola ini memberi petunjuk bahwa string harus
**dibalik**.

## 4. Layer 2 — Reverse

```python
s2 = s1[::-1]
print(s2)
```

Hasil:

```text
ASK{L3H_E3G7G6Q_GU6_Y6GG6E8_A3J_S4K_GU6_Q4T4G8}
```

Sekarang bentuknya sudah seperti flag: ada `{...}`. Prefix-nya `ASK`, dan
`ASK` adalah **ROT13 dari `NFX`**. Jadi layer berikutnya adalah ROT13.

## 5. Layer 3 — ROT13

```python
import codecs
s3 = codecs.decode(s2, "rot_13")
print(s3)
```

Hasil:

```text
NFX{Y3U_R3T7T6D_TH6_L6TT6R8_N3W_F4X_TH6_D4G4T8}
```

Hurufnya sudah membaca: `Y3U` → “YOU”, `R3T7T6D` → “ROT?T?D”, `TH6` → “TH3”,
`L6TT6R8` → “L3TT3R5”, `N3W` → “N0W”, `F4X` → “F1X”, `D4G4T8` → “D1G1T5”.
Tapi **digitnya masih salah**. Ini persis yang dikatakan flag: “YOU ROTATED
THE LETTERS, NOW FIX THE DIGITS”.

## 6. Layer 4 — “Fix the digits”

Digit yang muncul di hasil ROT13 adalah `3, 7, 6, 8, 4`. Kalau kita coba
semua pergeseran digit `0..9` (mod 10), hanya geser **-3** yang menghasilkan
kalimat leet yang benar:

| Digit lama | Digit baru (-3 mod 10) | Contoh |
|---:|---:|---|
| 3 | 0 | `Y3U` → `Y0U` |
| 7 | 4 | `R3T7T6D` → `R0T4T3D` |
| 6 | 3 | `TH6` → `TH3` |
| 8 | 5 | `L6TT6R8` → `L3TT3R5` |
| 4 | 1 | `F4X` → `F1X`, `D4G4T8` → `D1G1T5` |

```python
flag = "".join(str((int(c) - 3) % 10) if c.isdigit() else c for c in s3)
print(flag)
```

Hasil akhir:

```text
NFX{Y0U_R0T4T3D_TH3_L3TT3R5_N0W_F1X_TH3_D1G1T5}
```

## 7. Solver lengkap

```python
import codecs

ct = r"p5J9Y9\R;XJRF9^RG>LR5H;JJ;TR;XJR\;J:J>HRE>AvF^L"

s1 = "".join(chr(ord(c) ^ 13) for c in ct)          # XOR 13
s2 = s1[::-1]                                        # reverse
s3 = codecs.decode(s2, "rot_13")                     # ROT13
flag = "".join(str((int(c) - 3) % 10) if c.isdigit() else c for c in s3)

print(flag)
# NFX{Y0U_R0T4T3D_TH3_L3TT3R5_N0W_F1X_TH3_D1G1T5}
```

Ringkasan transformasi:

```text
ciphertext : p5J9Y9\R;XJRF9^RG>LR5H;JJ;TR;XJR\;J:J>HRE>AvF^L
XOR 0x0D   : }8G4T4Q_6UG_K4S_J3A_8E6GG6Y_6UG_Q6G7G3E_H3L{KSA
reverse    : ASK{L3H_E3G7G6Q_GU6_Y6GG6E8_A3J_S4K_GU6_Q4T4G8}
ROT13      : NFX{Y3U_R3T7T6D_TH6_L6TT6R8_N3W_F4X_TH6_D4G4T8}
digit -3   : NFX{Y0U_R0T4T3D_TH3_L3TT3R5_N0W_F1X_TH3_D1G1T5}
```

## 8. Verifikasi platform

Flag di atas disubmit lewat form challenge di platform NFX CTF 2026 dan
diterima:

![Validasi platform — CORRECT, BUT ALREADY SOLVED.](assets/13-is-not-enough/00b-platform-validation.png)

*Screenshot asli platform: `CORRECT, BUT ALREADY SOLVED.`*

### Evidence langkah ini

![Terminal evidence — solver 13 Is Not Enough](assets/13-is-not-enough/term-11-solver.png)

*Output solver asli: ciphertext, XOR 13, reverse, ROT13, dan digit -3.*
