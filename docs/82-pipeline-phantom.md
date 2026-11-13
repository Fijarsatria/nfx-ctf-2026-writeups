# Pipeline Phantom

<div class="nx-challenge-head"><span class="nx-chip">Track Mahasiswa NF · Misc</span><span class="nx-chip">Easy</span><span class="nx-chip">120 poin</span><span class="nx-badge nx-badge-verified">VERIFIED</span></div>


| Field | Nilai |
|---|---|
| Event | `umum/mahasiswa_nf` |
| Kategori | `Misc` |
| Author | `Ariaf` |
| Difficulty | `Easy` |
| Poin | `120` |
| Tools | git |
| Flag | `NFX{gh_4ct10ns_m4sk_byp4ss_4nd_0rph4n_c0mm1t_l34k_9f82}` |
| Status | `VERIFIED` |
[← Kembali ke Index](index.md)


## TL;DR

- **Flag:** `NFX{gh_4ct10ns_m4sk_byp4ss_4nd_0rph4n_c0mm1t_l34k_9f82}`
- **Baca langkah lengkap:** [Cara Mendapatkan Flag](82-pipeline-phantom-02-cara-mendapatkan-flag.md)

## Challenge Brief (platform)

![00-challenge-platform.png](assets/pipeline-phantom/00-challenge-platform.png)

*Challenge brief asli di platform NFX CTF 2026.*

## Alur & Titik Penting

| # | Langkah | Titik penting | Buka |
|---:|---|---|---|
| 1 | Recon | Repo `c2-deploy-pipeline`. | [Buka](82-pipeline-phantom-01-recon.md) |
| 2 | Cara Mendapatkan Flag | Log berspasi + commit yang di-revert. | [Buka](82-pipeline-phantom-02-cara-mendapatkan-flag.md) |
| 3 | Flag | NFX{gh_4ct10ns_m4sk_byp4ss_4nd_0rph4n_c0mm1t_l34k_9f82} | [Buka](82-pipeline-phantom-03-flag.md) |
| 4 | Bukti / Evidence | arsip screenshot dan transkrip | [Buka](82-pipeline-phantom-04-bukti-evidence.md) |
| 5 | Referensi | GitHub Actions log, orphan commit. | [Buka](82-pipeline-phantom-05-referensi.md) |

## Cerita singkat

CI menyembunyikan secret, tetapi log mencetaknya dengan spasi. Separuh flag ada di situ; separuh lagi ada di commit yang sudah di-revert.

<div class="nx-evidence-preview"><a href="82-pipeline-phantom-04-bukti-evidence.html"><img src="assets/pipeline-phantom/00b-terminal-evidence.png" alt="Pratinjau evidence Pipeline Phantom" loading="lazy"></a><span>Pratinjau evidence. Buka halaman <a href="82-pipeline-phantom-04-bukti-evidence.html">Evidence / Bukti</a> untuk semua screenshot dan transkrip.</span></div>

## Navigasi Halaman

<div class="nx-page-grid">
<a class="nx-page-card" href="82-pipeline-phantom-01-recon.html"><b>Recon</b><span>Enumerasi target dan bukti awal</span></a>
<a class="nx-page-card" href="82-pipeline-phantom-02-cara-mendapatkan-flag.html"><b>Cara Mendapatkan Flag</b><span>Flag dan verifikasi platform</span></a>
<a class="nx-page-card" href="82-pipeline-phantom-03-flag.html"><b>Flag</b><span>Flag dan verifikasi platform</span></a>
<a class="nx-page-card" href="82-pipeline-phantom-04-bukti-evidence.html"><b>Bukti / Evidence</b><span>Screenshot, transkrip, dan artefak</span></a>
<a class="nx-page-card" href="82-pipeline-phantom-05-referensi.html"><b>Referensi</b><span>Sumber dan bacaan lanjutan</span></a>
</div>
