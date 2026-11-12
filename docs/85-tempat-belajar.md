# Tempat Belajar

<div class="nx-challenge-head"><span class="nx-chip">Track Mahasiswa NF · Osint</span><span class="nx-chip">Easy</span><span class="nx-chip">300 poin</span><span class="nx-badge nx-badge-open">OPEN</span></div>


| Field | Nilai |
|---|---|
| Event | `umum/mahasiswa_nf` |
| Kategori | `Osint` |
| Difficulty | `Easy` |
| Poin | `300` |
| Author | `Kada` |
| Tools | exiftool, curl, python3 |
| Flag | **OPEN / CANDIDATE — base64 ditolak** |
| Status | `OPEN` |

[← Kembali ke Index](index.md)

> **Status: OPEN.** Kandidat base64 sudah ditemukan, tetapi **ditolak platform**.
> Flag yang diterima kemungkinan ada di DM Instagram `@dihlearn.id` dan belum
> berhasil diakses (login dijegal reCAPTCHA).

## Challenge Brief (platform)

![00-challenge-platform.png](assets/tempat-belajar/00-challenge-platform.png)

*Challenge brief asli di platform NFX CTF 2026.*

## Cerita singkat

Poster “Digital Hour Learning” (`office.png`) metadata-nya membocorkan
`Title: Dih Office`, `Author: Kada`, dan `Comment: 3%4TD'aPBA*Z,QPN`.
Nama “Dih” mengarah ke Instagram `@dihlearn.id`; akun karier
`@career.dihlearn.id` punya dua post yang menyembunyikan base64 di bagian atas
gambar. Base64 itu decode ke kandidat flag—tetapi platform menolaknya.

## Alur & Titik Penting

| # | Langkah | Titik penting | Buka |
|---:|---|---|---|
| 1 | Jejak Awal | metadata `office.png` + Instagram Dihlearn | [Buka](85-tempat-belajar-01-jejak-awal.md) |
| 2 | Cara Mendapatkan Flag | base64 post karier → kandidat (ditolak) | [Buka](85-tempat-belajar-02-cara-mendapatkan-flag.md) |
| 3 | Flag | **OPEN / CANDIDATE** | [Buka](85-tempat-belajar-03-flag.md) |
| 4 | Bukti / Evidence | terminal evidence: API `Incorrect flag` | [Buka](85-tempat-belajar-04-bukti-evidence.md) |
| 5 | Referensi | OSINT Instagram, base64 artifact | [Buka](85-tempat-belajar-05-referensi.md) |

## TL;DR

- `office.png` metadata: `Author=Kada`, `Title=Dih Office`,
  `Comment=3%4TD'aPBA*Z,QPN` (decoy/password, bukan flag).
- Instagram `@dihlearn.id` (poster) dan `@career.dihlearn.id` (dua post
  base64).
- Fragmen base64:
  - `TkZYe09wM25fUzB1cmMzX`
  - `1BsNHRGMG1fRDFoTDNybl9KNFIhfQ`
- Gabung + decode:
  `NFX{Op3n_S0urc3_Pl4tF0m_D1hL3rn_J4R!}`.
- Varian corrected (`Pl4tF0rm`, `D1hL34rn`, `S0urc1`) juga **ditolak**.
- `total_solves` challenge = **1** (bukan akun kita). Flag accepted belum
  ditemukan; kemungkinan ada di DM Instagram.

## Catatan audit

Halaman ini sebelumnya berstatus `VERIFIED` dan mengklaim
`CORRECT, BUT ALREADY SOLVED`, padahal screenshot evidence-nya sendiri
menampilkan **`INCORRECT FLAG`**. Audit 2026-11-12 mengubah status ke
**OPEN/CANDIDATE** dan memisahkan artefak dari klaim verifikasi.
