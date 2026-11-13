# Tempat Belajar

<div class="nx-challenge-head"><span class="nx-chip">Track Mahasiswa NF · Osint</span><span class="nx-chip">Easy</span><span class="nx-chip">300 poin</span><span class="nx-badge nx-badge-verified">VERIFIED</span></div>


| Field | Nilai |
|---|---|
| Event | `umum/mahasiswa_nf` |
| Kategori | `Osint` |
| Difficulty | `Easy` |
| Poin (snapshot) | `300` |
| Author | `Kada` |
| Tools | exiftool, python3, browser |
| Flag | `NFX{Op3n_S0urc3_Pl4tF0m_D1hL3rn_J4Ya}` |
| Status | `VERIFIED` |
| Metode | **PARTIAL** — Flag accepted; provenance teks J4Ya dari artefak Instagram/DM belum ditunjukkan penuh. |
| Snapshot | 2026-11-13 |

[← Kembali ke Index](index.md)

## Challenge Brief (platform)

![00-challenge-platform.png](assets/tempat-belajar/00-challenge-platform.png)

*Challenge brief asli di platform NFX CTF 2026.*

## Cerita singkat

Poster “Digital Hour Learning” (`office.png`) metadata-nya membocorkan
`Title: Dih Office`, `Author: Kada`, dan `Comment: 3%4TD'aPBA*Z,QPN`.
Nama “Dih” mengarah ke Instagram `@dihlearn.id`. Dari media sosial itu ada teks
Base64 yang kalau didekode menghasilkan flag. Flag sudah disubmit lewat web
platform dan diterima.

## Alur & Titik Penting

| # | Langkah | Titik penting | Buka |
|---:|---|---|---|
| 1 | Jejak Awal | metadata `office.png` + Instagram Dihlearn | [Buka](85-tempat-belajar-01-jejak-awal.md) |
| 2 | Cara Mendapatkan Flag | teks Base64 di IG → decode | [Buka](85-tempat-belajar-02-cara-mendapatkan-flag.md) |
| 3 | Flag | `NFX{Op3n_S0urc3_Pl4tF0m_D1hL3rn_J4Ya}` | [Buka](85-tempat-belajar-03-flag.md) |
| 4 | Bukti / Evidence | screenshot submit web `CORRECT` | [Buka](85-tempat-belajar-04-bukti-evidence.md) |
| 5 | Referensi | OSINT Instagram, base64 | [Buka](85-tempat-belajar-05-referensi.md) |

## TL;DR

- `office.png` metadata: `Author=Kada`, `Title=Dih Office`,
  `Comment=3%4TD'aPBA*Z,QPN` (decoy/password, bukan flag).
- Instagram `@dihlearn.id` mengarah ke teks Base64.
- Decode Base64 menghasilkan:
  `NFX{Op3n_S0urc3_Pl4tF0m_D1hL3rn_J4Ya}`.
- Flag disubmit lewat form web platform dan diterima.
- Kandidat lama `..._J4R!` memang **ditolak**; yang benar memakai `J4Ya`.

## Catatan audit

Halaman ini sempat `OPEN` karena kandidat Base64 lama (`..._J4R!`) ditolak.
Setelah teks Base64 yang benar dari Instagram didekode, flag
`..._J4Ya` diterima platform. Status dikoreksi menjadi `VERIFIED` pada
2026-11-13.

<div class="nx-evidence-preview"><a href="85-tempat-belajar-04-bukti-evidence.html"><img src="assets/tempat-belajar/00b-platform-validation.png" alt="Submit web Tempat Belajar" loading="lazy"></a><span>Screenshot submit web: <code>CORRECT, BUT ALREADY SOLVED.</code></span></div>

## Navigasi Halaman

- [Jejak Awal](85-tempat-belajar-01-jejak-awal.md)
- [Cara Mendapatkan Flag](85-tempat-belajar-02-cara-mendapatkan-flag.md)
- [Flag](85-tempat-belajar-03-flag.md)
- [Bukti / Evidence](85-tempat-belajar-04-bukti-evidence.md)
- [Referensi](85-tempat-belajar-05-referensi.md)
