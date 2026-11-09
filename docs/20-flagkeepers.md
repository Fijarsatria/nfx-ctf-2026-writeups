# FlagKeepers

| Field | Nilai |
|---|---|
| Event | `umum_Extend` |
| Kategori | `Crypto` |
| Difficulty | `Hard` |
| Poin | `440` |
| Author | `Ariaf` |
| Solves | `4` |
| Tools | python3, sage |
| Flag | `NFX{gcm_f0rb1dd3n_4tt4ck_du4l_t4g_c0ll1s10n_m4st3r}` |
| Status | `VERIFIED` |

[← Kembali ke Index](index.md)

## Ringkasan

## TL;DR

- `app.py` memakai **satu nonce GCM global** untuk dua key berbeda
  (`key_a` untuk AUDIT, `key_b` untuk RECOVERY).
- Opsi `[2]` mencetak plaintext RECOVERY secara verbatim, sehingga keystream
  CTR untuk `key_b` dapat dihitung: `KS = CT XOR PT`.
- Semua pesan RECOVERY panjangnya sama (51 byte = 4 blok), jadi blok panjang
  GHASH saling menghilangkan pada selisih tag.
- Selisih tag menjadi sistem linear atas monomial `H²..H⁵` di GF(2¹²⁸);
  selesaikan untuk `H = AES_{key_b}(0^128)`. Setelah `H` diketahui,
  `E_{key_b}(J0) = tag XOR GHASH(H,CT)` konsisten di semua sampel.
- Forge plaintext `admin = True` + 39 spasi, hitung CT dan TAG, kirim ke
  opsi `[4]`. Setelah 14 kali opsi `[2]`, `idx = 32`, sehingga
  `msg[:idx]` memuat `admin = True`.
- Flag: `NFX{gcm_f0rb1dd3n_4tt4ck_du4l_t4g_c0ll1s10n_m4st3r}`.

## Navigasi Halaman

- [Recon](20-flagkeepers-01-recon.md)
- [Analisis](20-flagkeepers-02-analisis.md)
- [Eksploitasi / Solver](20-flagkeepers-03-eksploitasi-solver.md)
- [Flag](20-flagkeepers-04-flag.md)
- [Bukti / Evidence](20-flagkeepers-05-bukti-evidence.md)
- [Referensi](20-flagkeepers-06-referensi.md)
