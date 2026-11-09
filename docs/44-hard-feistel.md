# Hard Feistel

| Field | Nilai |
|---|---|
| Event | `umum_Extend` |
| Kategori | `Reverse` |
| Difficulty | `Hard` |
| Poin | `230` |
| Author | `cypera` |
| Solves | `19` |
| Tools | python3, pwntools, checksec, gdb, objdump, readelf, strings, sage |
| Flag | `NFX{f315t3l_n3tw0rk_16_r0und5_r3v3rs3d}` |
| Status | `VERIFIED` |

[← Kembali ke Index](index.md)

## Ringkasan

## TL;DR

- `hard_feistel` memvalidasi flag 39 byte dari `argv[1]` dan memprosesnya sebagai 10 blok 32-bit.
- Setiap blok dipecah menjadi `L` dan `R` 16-bit, lalu melewati **16 ronde Feistel**.
- Fungsi ronde: `F(R,K) = (((R * 0x9e3779b1) mod 2^32) >> 5) XOR ((K * 257) & 0xffff)`.
- 16 round key 16-bit tertanam di `.rodata` `0x2060`; ciphertext 40 byte di `.data` `0x4020`.
- Output tiap blok adalah `big-endian(L16) || big-endian(R16)`, jadi dekripsi cukup membalik urutan ronde tanpa menginversi `F`.
- Flag: `NFX{f315t3l_n3tw0rk_16_r0und5_r3v3rs3d}`.

## Navigasi Halaman

- [Recon](44-hard-feistel-01-recon.md)
- [Analisis](44-hard-feistel-02-analisis.md)
- [Eksploitasi / Solver](44-hard-feistel-03-eksploitasi-solver.md)
- [Flag](44-hard-feistel-04-flag.md)
- [Bukti / Evidence](44-hard-feistel-05-bukti-evidence.md)
- [Referensi](44-hard-feistel-06-referensi.md)
