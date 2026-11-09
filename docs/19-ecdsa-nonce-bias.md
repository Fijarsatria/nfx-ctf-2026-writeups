# ECDSA Nonce Bias

| Field | Nilai |
|---|---|
| Event | `umum_Extend` |
| Kategori | `Crypto` |
| Difficulty | `Hard` |
| Poin | `260` |
| Author | `rio` |
| Solves | `13` |
| Tools | python3, sage, fpylll, git |
| Flag | `NXCTF{ecds4_hnp_n0nc3_b14s_8b1t_l4tt1c3_a3d2ae498097}` |
| Status | `VERIFIED` |

[← Kembali ke Index](index.md)

## Ringkasan

## TL;DR

- 200 signature ECDSA pada `secp256k1`; nonce `k` selalu `< 2^248`
  (8 bit teratas nol).
- Ini **Hidden Number Problem (HNP)**: dari
  `s = k^{-1}(h + d·r) mod n`, nonce kecil memberi
  `k_i = a_i + b_i·d mod n` dengan `a_i = h_i s_i^{-1}`,
  `b_i = r_i s_i^{-1}`, dan `k_i < B = 2^248`.
- Lattice HNP dengan 50 signature + LLL memulihkan private key `d`.
- Verifikasi: `d·G` sama dengan public key, 200/200 nonce `< 2^248`,
  dan AES-GCM tag valid.
- Flag: `NXCTF{ecds4_hnp_n0nc3_b14s_8b1t_l4tt1c3_a3d2ae498097}`.

## Navigasi Halaman

- [Recon](19-ecdsa-nonce-bias-01-recon.md)
- [Analisis](19-ecdsa-nonce-bias-02-analisis.md)
- [Eksploitasi / Solver](19-ecdsa-nonce-bias-03-eksploitasi-solver.md)
- [Flag](19-ecdsa-nonce-bias-04-flag.md)
- [Bukti / Evidence](19-ecdsa-nonce-bias-05-bukti-evidence.md)
- [Referensi](19-ecdsa-nonce-bias-06-referensi.md)
