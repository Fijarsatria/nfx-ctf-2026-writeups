# Omah Buffer Kebak

<div class="nx-challenge-head"><span class="nx-chip">Track Mahasiswa NF · Pwn</span><span class="nx-chip">Baby</span><span class="nx-chip">100 poin</span><span class="nx-badge nx-badge-verified">VERIFIED</span></div>


| Field | Nilai |
|---|---|
| Event | `umum/mahasiswa_nf` |
| Kategori | `Pwn` |
| Difficulty | `Baby` |
| Poin | `100` |
| Tools | pwntools, checksec |
| Flag | `NFX{OmahhKUuD0Ndoll_Uw0nggG}` |
| Status | `VERIFIED` |

[← Kembali ke Index](index.md)

## Challenge Brief (platform)

![00-challenge-platform.png](assets/omah-buffer-kebak/00-challenge-platform.png)

*Challenge brief asli di platform NFX CTF 2026.*

## Alur & Titik Penting

| # | Langkah | Titik penting | Buka |
|---:|---|---|---|
| 1 | Recon | Baca brief challenge dan cek attachment/service yang diberikan. | [Buka](64-omah-buffer-kebak-01-recon.md) |
| 2 | Cara Mendapatkan Flag | NFX{OmahhKUuD0Ndoll_Uw0nggG} | [Buka](64-omah-buffer-kebak-02-cara-mendapatkan-flag.md) |
| 3 | Flag | NFX{OmahhKUuD0Ndoll_Uw0nggG} | [Buka](64-omah-buffer-kebak-03-flag.md) |
| 4 | Bukti / Evidence | arsip screenshot dan transkrip | [Buka](64-omah-buffer-kebak-04-bukti-evidence.md) |
| 5 | Referensi | Buffer overflow, checksec, pwntools cyclic. | [Buka](64-omah-buffer-kebak-05-referensi.md) |

## Cerita singkat

Binary pwn klasik: input kita bisa menimpa return address. Kita cek proteksi, cari offset, lalu susun payload untuk membuka shell atau memanggil fungsi flag.

<div class="nx-evidence-preview"><a href="64-omah-buffer-kebak-04-bukti-evidence.html"><img src="assets/omah-buffer-kebak/00b-terminal-evidence.png" alt="Pratinjau evidence Omah Buffer Kebak" loading="lazy"></a><span>Pratinjau evidence. Buka halaman <a href="64-omah-buffer-kebak-04-bukti-evidence.html">Evidence / Bukti</a> untuk semua screenshot dan transkrip.</span></div>

## Navigasi Halaman

<div class="nx-page-grid">
<a class="nx-page-card" href="64-omah-buffer-kebak-01-recon.html"><b>Recon</b><span>Enumerasi target dan bukti awal</span></a>
<a class="nx-page-card" href="64-omah-buffer-kebak-02-cara-mendapatkan-flag.html"><b>Cara Mendapatkan Flag</b><span>Flag dan verifikasi platform</span></a>
<a class="nx-page-card" href="64-omah-buffer-kebak-03-flag.html"><b>Flag</b><span>Flag dan verifikasi platform</span></a>
<a class="nx-page-card" href="64-omah-buffer-kebak-04-bukti-evidence.html"><b>Bukti / Evidence</b><span>Screenshot, transkrip, dan artefak</span></a>
<a class="nx-page-card" href="64-omah-buffer-kebak-05-referensi.html"><b>Referensi</b><span>Sumber dan bacaan lanjutan</span></a>
</div>
