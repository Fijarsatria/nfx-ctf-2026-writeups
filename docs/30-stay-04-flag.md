# Stay — Flag & Verifikasi

[← Overview](30-stay.md) · [Index](index.md)

> **Langkah 4/6 — Flag.** Plaintext hasil decode:
>
> **Titik penting:** NFX{st4y_w1th_m3_1n_th3_d4rk}
>
> **Berikutnya:** [Bukti / Evidence](30-stay-05-bukti-evidence.md)

> **Asal flag.** Flag diperoleh dari langkah exploit/solver yang terdokumentasi, lalu disubmit ke platform.  
> **Tingkat bukti metode.** Terdokumentasi. [Buka Evidence](30-stay-05-bukti-evidence.md)

> **Flag:** `NFX{st4y_w1th_m3_1n_th3_d4rk}`
> **Status:** `VERIFIED`

Plaintext hasil decode:

```text
NXCTF{st4y_w1th_m3_1n_th3_d4rk}
```

Flag platform (file `flags/wave2/Stay.txt`):

```text
NFX{st4y_w1th_m3_1n_th3_d4rk}
```

Verifikasi:

- 176 karakter → 352 bit → 44 byte, tepat.
- Base64 valid dan decode 33 byte.
- XOR `falling` menghasilkan plaintext yang dapat dibaca.
- Assertion terhadap `NXCTF{...}` PASS.
- Prefix dinormalisasi ke `NFX` sesuai flag platform.

### Terminal evidence (real)

![Terminal evidence (real)](assets/stay/00b-terminal-evidence.png)

*Terminal evidence (real).*

> **Bukti:** terminal evidence (real).

## Validasi platform (real)

![Validasi platform — CORRECT, BUT ALREADY SOLVED.](assets/stay/00b-platform-validation.png)

*Screenshot asli dari platform NFX CTF 2026. Platform menjawab
`CORRECT, BUT ALREADY SOLVED.` untuk flag ini.*
