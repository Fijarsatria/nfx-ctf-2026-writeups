# NexaCommerce

<div class="nx-challenge-head"><span class="nx-chip">Track Mahasiswa NF · Web</span><span class="nx-chip">Easy</span><span class="nx-chip">100 poin</span><span class="nx-badge nx-badge-verified">VERIFIED</span></div>


| Field | Nilai |
|---|---|
| Event | `umum/mahasiswa_nf` |
| Kategori | `Web` |
| Difficulty | `Easy` |
| Poin | `100` |
| Flag | `NFX{sql1_un10n_bas3d_4uth_byp4ss}` |
| Status | `VERIFIED` |

[← Kembali ke Index](index.md)

## Challenge Brief (platform)

![00-challenge-platform.png](assets/nexacommerce/00-challenge-platform.png)

*Challenge brief asli di platform NFX CTF 2026.*

## Alur & Titik Penting

| # | Langkah | Titik penting | Buka |
|---:|---|---|---|
| 1 | Recon | Baca brief challenge dan cek attachment/service yang diberikan. | [Buka](67-nexacommerce-01-recon.md) |
| 2 | Cara Mendapatkan Flag | NFX{sql1_un10n_bas3d_4uth_byp4ss} | [Buka](67-nexacommerce-02-cara-mendapatkan-flag.md) |
| 3 | Flag | NFX{sql1_un10n_bas3d_4uth_byp4ss} | [Buka](67-nexacommerce-03-flag.md) |
| 4 | Bukti / Evidence | arsip screenshot dan transkrip | [Buka](67-nexacommerce-04-bukti-evidence.md) |
| 5 | Referensi | SQL injection, UNION-based auth bypass. | [Buka](67-nexacommerce-05-referensi.md) |

## Cerita singkat

Login NexaCommerce bisa dilewati lewat SQL injection. Kita susun payload UNION supaya query login mengembalikan user admin.

<div class="nx-evidence-preview"><a href="67-nexacommerce-04-bukti-evidence.html"><img src="assets/nexacommerce/00b-terminal-evidence.png" alt="Pratinjau evidence NexaCommerce" loading="lazy"></a><span>Pratinjau evidence. Buka halaman <a href="67-nexacommerce-04-bukti-evidence.html">Evidence / Bukti</a> untuk semua screenshot dan transkrip.</span></div>

## Navigasi Halaman

<div class="nx-page-grid">
<a class="nx-page-card" href="67-nexacommerce-01-recon.html"><b>Recon</b><span>Enumerasi target dan bukti awal</span></a>
<a class="nx-page-card" href="67-nexacommerce-02-cara-mendapatkan-flag.html"><b>Cara Mendapatkan Flag</b><span>Flag dan verifikasi platform</span></a>
<a class="nx-page-card" href="67-nexacommerce-03-flag.html"><b>Flag</b><span>Flag dan verifikasi platform</span></a>
<a class="nx-page-card" href="67-nexacommerce-04-bukti-evidence.html"><b>Bukti / Evidence</b><span>Screenshot, transkrip, dan artefak</span></a>
<a class="nx-page-card" href="67-nexacommerce-05-referensi.html"><b>Referensi</b><span>Sumber dan bacaan lanjutan</span></a>
</div>
