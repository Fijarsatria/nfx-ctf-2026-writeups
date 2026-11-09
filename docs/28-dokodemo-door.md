# Dokodemo Door

| Field | Nilai |
|---|---|
| Event | `umum_Extend` |
| Kategori | `Misc` |
| Difficulty | `Medium` |
| Poin | `160` |
| Author | `Kada` |
| Solves | `18` |
| Flag | `NFX{k3tuk_p1ntu_bUk4_d0kum3n_x0r}` |
| Status | `VERIFIED` |

[← Kembali ke Index](index.md)

## Ringkasan

## TL;DR

- `rahasia.pdf` bukan PDF lagi: seluruh byte di-XOR dengan **repeating key**
  sepanjang 16 byte.
- Karena PDF punya magic header `%PDF-1.4\n` dan trailer `%%EOF\n`, keduanya
  bisa dipakai sebagai *known plaintext* untuk menurunkan key.
- Key yang diperoleh: `nfx_k3tuk_p1ntu!`.
- Setelah didekripsi, file valid sebagai PDF 1.4; teks di halaman pertama
  memuat flag `NFX{k3tuk_p1ntu_bUk4_d0kum3n_x0r}`.

## Navigasi Halaman

- [Recon](28-dokodemo-door-01-recon.md)
- [Analisis](28-dokodemo-door-02-analisis.md)
- [Eksploitasi / Solver](28-dokodemo-door-03-eksploitasi-solver.md)
- [Flag](28-dokodemo-door-04-flag.md)
- [Bukti / Evidence](28-dokodemo-door-05-bukti-evidence.md)
- [Referensi](28-dokodemo-door-06-referensi.md)
