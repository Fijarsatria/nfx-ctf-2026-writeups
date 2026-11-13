# Notulen Senin Pagi

<div class="nx-challenge-head"><span class="nx-chip">Track Mahasiswa NF · Misc</span><span class="nx-chip">Baby</span><span class="nx-chip">100 poin</span><span class="nx-badge nx-badge-verified">VERIFIED</span></div>


| Field | Nilai |
|---|---|
| Event | `umum/mahasiswa_nf` |
| Kategori | `Misc` |
| Author | `Syahril` |
| Difficulty | `Baby` |
| Poin (snapshot) | `100` |
| Tools | exiftool |
| Flag | `NFX{M4kHLuK_T4k_K4s4T_M4T4}` |
| Status | `VERIFIED` |
| Metode | **FULL** — metode utama berhasil direproduksi. |
| Snapshot | 2026-11-13 |

[← Kembali ke Index](index.md)


## TL;DR

- **Flag:** `NFX{M4kHLuK_T4k_K4s4T_M4T4}`
- **Metode:** **FULL** — metode utama berhasil direproduksi.
- **Baca langkah lengkap:** [Cara Mendapatkan Flag](62-notulen-senin-pagi-02-cara-mendapatkan-flag.md)

## Challenge Brief (platform)

![00-challenge-platform.png](assets/notulen-senin-pagi/00-challenge-platform.png)

*Challenge brief asli di platform NFX CTF 2026.*

## Alur & Titik Penting

| # | Langkah | Titik penting | Buka |
|---:|---|---|---|
| 1 | Recon | PDF satu halaman, metadata bersih. | [Buka](62-notulen-senin-pagi-01-recon.md) |
| 2 | Cara Mendapatkan Flag | `pdftotext` membaca teks putih. | [Buka](62-notulen-senin-pagi-02-cara-mendapatkan-flag.md) |
| 3 | Flag | NFX{M4kHLuK_T4k_K4s4T_M4T4} | [Buka](62-notulen-senin-pagi-03-flag.md) |
| 4 | Bukti / Evidence | arsip screenshot dan transkrip | [Buka](62-notulen-senin-pagi-04-bukti-evidence.md) |
| 5 | Referensi | PDF text layer, metadata, hidden text. | [Buka](62-notulen-senin-pagi-05-referensi.md) |

## Cerita singkat

Flag tertulis di PDF dengan warna yang tidak kelihatan. `pdftotext` tetap membacanya; mata tidak.

<div class="nx-evidence-preview"><a href="62-notulen-senin-pagi-04-bukti-evidence.html"><img src="assets/notulen-senin-pagi/00b-terminal-evidence.png" alt="Pratinjau evidence Notulen Senin Pagi" loading="lazy"></a><span>Pratinjau evidence. Buka halaman <a href="62-notulen-senin-pagi-04-bukti-evidence.html">Evidence / Bukti</a> untuk semua screenshot dan transkrip.</span></div>

## Navigasi Halaman

<div class="nx-page-grid">
<a class="nx-page-card" href="62-notulen-senin-pagi-01-recon.html"><b>Recon</b><span>Enumerasi target dan bukti awal</span></a>
<a class="nx-page-card" href="62-notulen-senin-pagi-02-cara-mendapatkan-flag.html"><b>Cara Mendapatkan Flag</b><span>Flag dan verifikasi platform</span></a>
<a class="nx-page-card" href="62-notulen-senin-pagi-03-flag.html"><b>Flag</b><span>Flag dan verifikasi platform</span></a>
<a class="nx-page-card" href="62-notulen-senin-pagi-04-bukti-evidence.html"><b>Bukti / Evidence</b><span>Screenshot, transkrip, dan artefak</span></a>
<a class="nx-page-card" href="62-notulen-senin-pagi-05-referensi.html"><b>Referensi</b><span>Sumber dan bacaan lanjutan</span></a>
</div>
