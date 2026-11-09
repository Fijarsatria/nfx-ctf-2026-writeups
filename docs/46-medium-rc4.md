# Medium RC4

| Field | Nilai |
|---|---|
| Event | `umum_Extend` |
| Kategori | `Reverse` |
| Difficulty | `Medium` |
| Poin | `100` |
| Author | `cypera` |
| Solves | `26` |
| Flag | `NFX{rc4_1s_s1mpl3_but_d34dly_1n_r3v3rs1ng}` |
| Status | `VERIFIED` |

[← Kembali ke Index](index.md)

## Ringkasan

## TL;DR

- Binary `medium_rc4` adalah ELF x86-64 PIE, stripped, dan meminta flag lewat `argv[1]`.
- Program mengecek panjang input tepat `42` byte, lalu menjalankan **RC4** dengan key hardcoded `n0t_s3cur3_k3y_2026`.
- Ciphertext 42 byte disimpan di `.rodata` pada alamat `0x2060`; hasil enkripsi input dibandingkan dengan `memcmp`.
- Karena RC4 simetris, dekripsi memakai rutin yang sama dengan enkripsi. Cukup ekstrak key + ciphertext, jalankan RC4, selesai.
- Flag: `NFX{rc4_1s_s1mpl3_but_d34dly_1n_r3v3rs1ng}`.

## Navigasi Halaman

- [Recon](46-medium-rc4-01-recon.md)
- [Analisis](46-medium-rc4-02-analisis.md)
- [Eksploitasi / Solver](46-medium-rc4-03-eksploitasi-solver.md)
- [Flag](46-medium-rc4-04-flag.md)
- [Bukti / Evidence](46-medium-rc4-05-bukti-evidence.md)
- [Referensi](46-medium-rc4-06-referensi.md)
