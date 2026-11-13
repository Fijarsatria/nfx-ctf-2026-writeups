# NexaRewards

<div class="nx-challenge-head"><span class="nx-chip">Track Mahasiswa NF · Web</span><span class="nx-chip">Easy</span><span class="nx-chip">100 poin</span><span class="nx-badge nx-badge-verified">VERIFIED</span></div>


| Field | Nilai |
|---|---|
| Event | `umum/mahasiswa_nf` |
| Kategori | `Web` |
| Author | `Ariaf` |
| Difficulty | `Easy` |
| Poin | `100` |
| Flag | `NFX{r4c3_c0nd1t10n_g1ft_c4rd_d0ubl3_sp3nd}` |
| Status | `VERIFIED` |
[← Kembali ke Index](index.md)


## TL;DR

- **Flag:** `NFX{r4c3_c0nd1t10n_g1ft_c4rd_d0ubl3_sp3nd}`
- **Baca langkah lengkap:** [Cara Mendapatkan Flag](70-nexarewards-02-cara-mendapatkan-flag.md)

## Challenge Brief (platform)

![00-challenge-platform.png](assets/nexarewards/00-challenge-platform.png)

*Challenge brief asli di platform NFX CTF 2026.*

## Alur & Titik Penting

| # | Langkah | Titik penting | Buka |
|---:|---|---|---|
| 1 | Recon | Login + kode `NEXA-RACE-60`. | [Buka](70-nexarewards-01-recon.md) |
| 2 | Cara Mendapatkan Flag | Race di `/redeem`, lalu beli `audit-report`. | [Buka](70-nexarewards-02-cara-mendapatkan-flag.md) |
| 3 | Flag | NFX{r4c3_c0nd1t10n_g1ft_c4rd_d0ubl3_sp3nd} | [Buka](70-nexarewards-03-flag.md) |
| 4 | Bukti / Evidence | arsip screenshot dan transkrip | [Buka](70-nexarewards-04-bukti-evidence.md) |
| 5 | Referensi | Race condition, double spend, parallel requests. | [Buka](70-nexarewards-05-referensi.md) |

## Cerita singkat

Login `employee@nexarewards.test`, redeem `NEXA-RACE-60` sepuluh kali secara paralel, lalu beli item `audit-report`.

<div class="nx-evidence-preview"><a href="70-nexarewards-04-bukti-evidence.html"><img src="assets/nexarewards/00b-terminal-evidence.png" alt="Pratinjau evidence NexaRewards" loading="lazy"></a><span>Pratinjau evidence. Buka halaman <a href="70-nexarewards-04-bukti-evidence.html">Evidence / Bukti</a> untuk semua screenshot dan transkrip.</span></div>

## Navigasi Halaman

<div class="nx-page-grid">
<a class="nx-page-card" href="70-nexarewards-01-recon.html"><b>Recon</b><span>Enumerasi target dan bukti awal</span></a>
<a class="nx-page-card" href="70-nexarewards-02-cara-mendapatkan-flag.html"><b>Cara Mendapatkan Flag</b><span>Flag dan verifikasi platform</span></a>
<a class="nx-page-card" href="70-nexarewards-03-flag.html"><b>Flag</b><span>Flag dan verifikasi platform</span></a>
<a class="nx-page-card" href="70-nexarewards-04-bukti-evidence.html"><b>Bukti / Evidence</b><span>Screenshot, transkrip, dan artefak</span></a>
<a class="nx-page-card" href="70-nexarewards-05-referensi.html"><b>Referensi</b><span>Sumber dan bacaan lanjutan</span></a>
</div>
