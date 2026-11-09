# Stay

| Field | Nilai |
|---|---|
| Event | `umum_Extend` |
| Kategori | `Misc` |
| Difficulty | `Medium` |
| Poin | `340` |
| Author | `Kesatria Baja Ringan` |
| Solves | `9` |
| Flag | `NFX{st4y_w1th_m3_1n_th3_d4rk}` |
| Status | `VERIFIED` |

[← Kembali ke Index](index.md)

## Ringkasan

## TL;DR

- Tidak ada attachment: payload ada di **teks lirik pada deskripsi challenge**.
- Di antara huruf-huruf lirik disisipkan **176 karakter zero-width** dari
  empat jenis code point.
- Setiap karakter membawa **2 bit**; 176 × 2 = 352 bit = **44 byte**.
- 44 byte itu adalah Base64:
  `KDkvOC8VFBJVFTMeXxMOPgFfNl8JORUEXzYKUxQKEQ==`.
- Setelah Base64 decode (33 byte) dan XOR dengan key `falling`, muncul
  `NXCTF{st4y_w1th_m3_1n_th3_d4rk}`.
- Flag platform: `NFX{st4y_w1th_m3_1n_th3_d4rk}`.

## Navigasi Halaman

- [Recon](30-stay-01-recon.md)
- [Analisis](30-stay-02-analisis.md)
- [Eksploitasi / Solver](30-stay-03-eksploitasi-solver.md)
- [Flag](30-stay-04-flag.md)
- [Bukti / Evidence](30-stay-05-bukti-evidence.md)
- [Referensi](30-stay-06-referensi.md)
