# NexaSupply

<div class="nx-challenge-head"><span class="nx-chip">Track Mahasiswa NF · Web</span><span class="nx-chip">Baby</span><span class="nx-chip">100 poin</span><span class="nx-badge nx-badge-verified">VERIFIED</span></div>


| Field | Nilai |
|---|---|
| Event | `umum/mahasiswa_nf` |
| Kategori | `Web` |
| Difficulty | `Baby` |
| Poin | `100` |
| Flag | `NFX{xxe_supply_f33d_l0c4l_f1l3_r34d}` |
| Status | `VERIFIED` |

[← Kembali ke Index](index.md)

## Challenge Brief (platform)

![00-challenge-platform.png](assets/nexasupply/00-challenge-platform.png)

*Challenge brief asli di platform NFX CTF 2026.*

## Alur & Titik Penting

| # | Langkah | Titik penting | Buka |
|---:|---|---|---|
| 1 | Recon | Login supplier + `POST /import`. | [Buka](72-nexasupply-01-recon.md) |
| 2 | Cara Mendapatkan Flag | XXE `file:///flag.txt` di `<sku>`. | [Buka](72-nexasupply-02-cara-mendapatkan-flag.md) |
| 3 | Flag | NFX{xxe_supply_f33d_l0c4l_f1l3_r34d} | [Buka](72-nexasupply-03-flag.md) |
| 4 | Bukti / Evidence | arsip screenshot dan transkrip | [Buka](72-nexasupply-04-bukti-evidence.md) |
| 5 | Referensi | XXE, external entity, local file read. | [Buka](72-nexasupply-05-referensi.md) |

## Cerita singkat

Login supplier, kirim XML dengan entity `file:///flag.txt` ke `/import`, dan taruh entity itu di `<sku>` supaya muncul di response.

<div class="nx-evidence-preview"><a href="72-nexasupply-04-bukti-evidence.html"><img src="assets/nexasupply/00b-terminal-evidence.png" alt="Pratinjau evidence NexaSupply" loading="lazy"></a><span>Pratinjau evidence. Buka halaman <a href="72-nexasupply-04-bukti-evidence.html">Evidence / Bukti</a> untuk semua screenshot dan transkrip.</span></div>

## Navigasi Halaman

<div class="nx-page-grid">
<a class="nx-page-card" href="72-nexasupply-01-recon.html"><b>Recon</b><span>Enumerasi target dan bukti awal</span></a>
<a class="nx-page-card" href="72-nexasupply-02-cara-mendapatkan-flag.html"><b>Cara Mendapatkan Flag</b><span>Flag dan verifikasi platform</span></a>
<a class="nx-page-card" href="72-nexasupply-03-flag.html"><b>Flag</b><span>Flag dan verifikasi platform</span></a>
<a class="nx-page-card" href="72-nexasupply-04-bukti-evidence.html"><b>Bukti / Evidence</b><span>Screenshot, transkrip, dan artefak</span></a>
<a class="nx-page-card" href="72-nexasupply-05-referensi.html"><b>Referensi</b><span>Sumber dan bacaan lanjutan</span></a>
</div>
