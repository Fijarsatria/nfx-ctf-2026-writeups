# THE BROKEN RESOURCE PARSER

<div class="nx-challenge-head"><span class="nx-chip">Track Mahasiswa NF · Pwn</span><span class="nx-chip">Easy</span><span class="nx-chip">100 poin</span><span class="nx-badge nx-badge-verified">VERIFIED</span></div>


| Field | Nilai |
|---|---|
| Event | `umum/mahasiswa_nf` |
| Kategori | `Pwn` |
| Author | `Amablex` |
| Difficulty | `Easy` |
| Poin (snapshot) | `100` |
| Flag | `NFX{Ad1o0Ssss_Br0k3nnn_fl3gg}` |
| Status | `VERIFIED` |
| Metode | **FULL** — metode utama berhasil direproduksi. |
| Snapshot | 2026-11-13 |

[← Kembali ke Index](index.md)


## TL;DR

- **Flag:** `NFX{Ad1o0Ssss_Br0k3nnn_fl3gg}`
- **Metode:** **FULL** — metode utama berhasil direproduksi.
- **Baca langkah lengkap:** [Cara Mendapatkan Flag](65-the-broken-resource-parser-02-cara-mendapatkan-flag.md)

## Challenge Brief (platform)

![00-challenge-platform.png](assets/the-broken-resource-parser/00-challenge-platform.png)

*Challenge brief asli di platform NFX CTF 2026.*

## Alur & Titik Penting

| # | Langkah | Titik penting | Buka |
|---:|---|---|---|
| 1 | Recon | ELF non-PIE, `win` di `0x4012ae`. | [Buka](65-the-broken-resource-parser-01-recon.md) |
| 2 | Cara Mendapatkan Flag | Overflow nama, offset `0x38`, ret2win. | [Buka](65-the-broken-resource-parser-02-cara-mendapatkan-flag.md) |
| 3 | Flag | NFX{Ad1o0Ssss_Br0k3nnn_fl3gg} | [Buka](65-the-broken-resource-parser-03-flag.md) |
| 4 | Bukti / Evidence | arsip screenshot dan transkrip | [Buka](65-the-broken-resource-parser-04-bukti-evidence.md) |
| 5 | Referensi | Parser bug, memory corruption. | [Buka](65-the-broken-resource-parser-05-referensi.md) |

## Cerita singkat

Binary non-PIE tanpa canary. `parse_resource` menyalin nama ke buffer 0x30 byte. Padding `0x38` lalu alamat `win` (`0x4012ae`) membaca `flag.txt`.

<div class="nx-evidence-preview"><a href="65-the-broken-resource-parser-04-bukti-evidence.html"><img src="assets/the-broken-resource-parser/00b-terminal-evidence.png" alt="Pratinjau evidence THE BROKEN RESOURCE PARSER" loading="lazy"></a><span>Pratinjau evidence. Buka halaman <a href="65-the-broken-resource-parser-04-bukti-evidence.html">Evidence / Bukti</a> untuk semua screenshot dan transkrip.</span></div>

## Navigasi Halaman

<div class="nx-page-grid">
<a class="nx-page-card" href="65-the-broken-resource-parser-01-recon.html"><b>Recon</b><span>Enumerasi target dan bukti awal</span></a>
<a class="nx-page-card" href="65-the-broken-resource-parser-02-cara-mendapatkan-flag.html"><b>Cara Mendapatkan Flag</b><span>Flag dan verifikasi platform</span></a>
<a class="nx-page-card" href="65-the-broken-resource-parser-03-flag.html"><b>Flag</b><span>Flag dan verifikasi platform</span></a>
<a class="nx-page-card" href="65-the-broken-resource-parser-04-bukti-evidence.html"><b>Bukti / Evidence</b><span>Screenshot, transkrip, dan artefak</span></a>
<a class="nx-page-card" href="65-the-broken-resource-parser-05-referensi.html"><b>Referensi</b><span>Sumber dan bacaan lanjutan</span></a>
</div>
