# Image Metadata

<div class="nx-challenge-head"><span class="nx-chip">Track Mahasiswa NF · Forensics</span><span class="nx-chip">Easy</span><span class="nx-chip">220 poin</span><span class="nx-badge nx-badge-verified">VERIFIED</span></div>


| Field | Nilai |
|---|---|
| Event | `umum/mahasiswa_nf` |
| Kategori | `Forensics` |
| Difficulty | `Easy` |
| Poin (snapshot) | `220` |
| Author | `Candelena` |
| Flag | `NFXCTF{h4shc4t_cr4ck1ng_z1p_succ3ssfu11y}` |
| Status | `VERIFIED` |
| Snapshot | 2026-11-13 |

[← Kembali ke Index](index.md)


## TL;DR

- **Flag:** `NFXCTF{h4shc4t_cr4ck1ng_z1p_succ3ssfu11y}`
- **Baca langkah lengkap:** [Cara Mendapatkan Flag](57-image-metadata-04-flag.md)

## Challenge Brief (platform)

![00-challenge-platform.png](assets/image-metadata/00-challenge-platform.png)

*Challenge brief asli di platform NFX CTF 2026.*

## Alur & Titik Penting

| # | Langkah | Titik penting | Buka |
|---:|---|---|---|
| 1 | Recon Artefak | file evidence.png | [Buka](57-image-metadata-01-recon-artefak.md) |
| 2 | Analisis Artefak | ZIP mulai di offset 31197. | [Buka](57-image-metadata-02-analisis-artefak.md) |
| 3 | Pemulihan Artefak | NFXCTF{h4shc4t_cr4ck1ng_z1p_succ3ssfu11y} | [Buka](57-image-metadata-03-pemulihan-artefak.md) |
| 4 | Flag | NFXCTF{h4shc4t_cr4ck1ng_z1p_succ3ssfu11y} | [Buka](57-image-metadata-04-flag.md) |
| 5 | Bukti / Evidence | arsip screenshot dan transkrip | [Buka](57-image-metadata-05-bukti-evidence.md) |
| 6 | Referensi | — | [Buka](57-image-metadata-06-referensi.md) |

## Cerita singkat

Jadi ceritanya gini. Kita dikasih satu gambar `evidence.png`. Kalau dilihat biasa, ya cuma gambar. Tapi setelah dicek, ada ZIP yang nyempil di belakang file PNG. ZIP-nya berisi `passwords.txt` dan `flag.txt` yang dikunci password. Kita tinggal coba daftar password itu sampai ketemu yang cocok.

<div class="nx-evidence-preview"><a href="57-image-metadata-05-bukti-evidence.html"><img src="assets/image-metadata/00b-terminal-evidence.png" alt="Pratinjau evidence Image Metadata" loading="lazy"></a><span>Pratinjau evidence. Buka halaman <a href="57-image-metadata-05-bukti-evidence.html">Evidence / Bukti</a> untuk semua screenshot dan transkrip.</span></div>

## Navigasi Halaman

<div class="nx-page-grid">
<a class="nx-page-card" href="57-image-metadata-01-recon-artefak.html"><b>Recon Artefak</b><span>Enumerasi target dan bukti awal</span></a>
<a class="nx-page-card" href="57-image-metadata-02-analisis-artefak.html"><b>Analisis Artefak</b><span>Membaca alur dan akar masalah</span></a>
<a class="nx-page-card" href="57-image-metadata-03-pemulihan-artefak.html"><b>Pemulihan Artefak</b><span>Baca bagian ini</span></a>
<a class="nx-page-card" href="57-image-metadata-04-flag.html"><b>Flag</b><span>Flag dan verifikasi platform</span></a>
<a class="nx-page-card" href="57-image-metadata-05-bukti-evidence.html"><b>Bukti / Evidence</b><span>Screenshot, transkrip, dan artefak</span></a>
<a class="nx-page-card" href="57-image-metadata-06-referensi.html"><b>Referensi</b><span>Sumber dan bacaan lanjutan</span></a>
</div>
