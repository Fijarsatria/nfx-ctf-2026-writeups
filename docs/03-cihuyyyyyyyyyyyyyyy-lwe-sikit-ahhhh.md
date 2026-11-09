# Cihuyyyyyyyyyyyyyyy LWE sikit ahhhh

| Field | Nilai |
|---|---|
| Event | `umum/mahasiswa_nf` |
| Kategori | `Crypto` |
| Difficulty | `Medium` |
| Poin | `200` |
| Author | `Illal` |
| Solves | `16` |
| Flag | `NFXCTF{l4tt1c3_sm4ll_s3cr3t_LWE_7e2a0195}` |
| Status | `VERIFIED` |

[← Kembali ke Index](index.md)

## Ringkasan

## TL;DR

- Attachment `lwe.py` bukan kode challenge, melainkan **transkrip LWE**:
  `q=257`, `n=40`, `m=64`, matriks `A` 64×40, vektor `b` 64, dan `ct` 41 byte.
- Relasinya adalah LWE standar `b = A·s + e (mod 257)` dengan **secret ternary**
  `s ∈ {-1,0,1}` dan error `e ∈ [-2,2]`.
- Karena dimensi kecil dan secret/error sama-sama pendek, instance dapat
  dipecahkan dengan **Kannan embedding** + LLL/BKZ. Diperoleh `s` dan `e` yang
  memenuhi 64/64 persamaan.
- `ct` panjangnya tepat 41 byte, sama dengan panjang flag. Flag diverifikasi
  di platform; KDF/skema enkripsi tidak disertakan di lampiran (lihat §3.4).
- Flag: `NFXCTF{l4tt1c3_sm4ll_s3cr3t_LWE_7e2a0195}`.

## Navigasi Halaman

- [Recon](03-cihuyyyyyyyyyyyyyyy-lwe-sikit-ahhhh-01-recon.md)
- [Analisis](03-cihuyyyyyyyyyyyyyyy-lwe-sikit-ahhhh-02-analisis.md)
- [Eksploitasi / Solver](03-cihuyyyyyyyyyyyyyyy-lwe-sikit-ahhhh-03-eksploitasi-solver.md)
- [Flag](03-cihuyyyyyyyyyyyyyyy-lwe-sikit-ahhhh-04-flag.md)
- [Bukti / Evidence](03-cihuyyyyyyyyyyyyyyy-lwe-sikit-ahhhh-05-bukti-evidence.md)
- [Referensi](03-cihuyyyyyyyyyyyyyyy-lwe-sikit-ahhhh-06-referensi.md)
