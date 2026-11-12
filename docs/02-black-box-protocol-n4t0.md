# Black Box Protocol N4T0

<div class="nx-challenge-head"><span class="nx-chip">Track Mahasiswa NF · Crypto</span><span class="nx-chip">Medium</span><span class="nx-chip">280 poin</span><span class="nx-badge nx-badge-verified">VERIFIED</span></div>


| Field | Nilai |
|---|---|
| Event | `umum/mahasiswa_nf` |
| Kategori | `Crypto` |
| Difficulty | `Medium` |
| Poin | `280` |
| Author | `Kada` |
| Tools | python3, openpyxl/zipfile, struct |
| Flag | `NFX{N4T0_PH0N3T1C_1N1_C0mbO_H3X_fl0At_b4r4ng}` |
| Status | `VERIFIED` |

[← Kembali ke Index](index.md)

> **Status: VERIFIED.** Decode tiga kolom berhasil dan flag diterima web platform.
> **ditolak platform**. `total_solves` challenge ini **0**.

## Challenge Brief (platform)

![00-challenge-platform.png](assets/black-box-protocol-n4t0/00-challenge-platform.png)

*Challenge brief asli di platform NFX CTF 2026.*

## Cerita singkat

Attachment `flight_recovery_manifest.xlsx` punya satu sheet `Mail_Black_Box`
dengan tiga kolom ber-encoding berbeda. Decode kolom A/B/C berhasil, tetapi
cara menyusun flag-nya belum terbukti diterima platform.

## Decode tiga kolom

| Kolom | Encoding | Hasil |
|---|---|---|
| A — Kode Pesawat | NATO + kata angka | `N4T0PH0N3T1C1N1` |
| B — kusi Pesawat | hex byte | `C0mbO_H3X_` |
| C — Jumlah Barang | IEEE-754 float32 big-endian | `fl0At_b4r4ng` |

Kandidat susunan yang paling wajar:

```text
NFX{N4T0_PH0N3T1C_1N1_C0mbO_H3X_fl0At_b4r4ng}
```

Flag ini **diterima** lewat form web platform (lihat halaman Flag/Evidence).

## Alur & Titik Penting

| # | Langkah | Titik penting | Buka |
|---:|---|---|---|
| 1 | Recon | file `flight_recovery_manifest.xlsx` | [Buka](02-black-box-protocol-n4t0-01-recon.md) |
| 2 | Analisis | sheet tunggal + sharedStrings | [Buka](02-black-box-protocol-n4t0-02-analisis.md) |
| 3 | Analisis 2 | decode A/B/C | [Buka](02-black-box-protocol-n4t0-03-analisis-2.md) |
| 4 | Solver | `decode_xlsx.py` | [Buka](02-black-box-protocol-n4t0-04-solver.md) |
| 5 | Flag | `NFX{N4T0...}` | [Buka](02-black-box-protocol-n4t0-05-flag.md) |
| 6 | Bukti / Evidence | terminal evidence + log API `Incorrect flag` | [Buka](02-black-box-protocol-n4t0-06-bukti-evidence.md) |
| 7 | Referensi | NATO, hex, float32 | [Buka](02-black-box-protocol-n4t0-07-referensi.md) |

## TL;DR

- A: `N4T0PH0N3T1C1N1` (NATO phonetic + digit).
- B: `C0mbO_H3X_` (hex).
- C: `fl0At_b4r4ng` (float32 big-endian).
- Kandidat `NFX{N4T0_PH0N3T1C_1N1_C0mbO_H3X_fl0At_b4r4ng}`
  **ditolak**; `total_solves = 0`.
- Tidak ada payload tambahan di XLSX (hidden sheet/comment/drawing/props bersih).

## Catatan audit

Halaman ini sebelumnya `VERIFIED` dengan screenshot mockup yang memakai input
dummy `XXX{...}` dan statistik `20 solves / 120 pts`, tidak cocok dengan
web platform. Status dikembalikan ke **VERIFIED** dan bukti
diganti terminal evidence asli dari log API.
