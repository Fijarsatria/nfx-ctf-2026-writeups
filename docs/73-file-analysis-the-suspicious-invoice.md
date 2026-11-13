# File Analysis: The Suspicious Invoice

<div class="nx-challenge-head"><span class="nx-chip">Track Mahasiswa NF · Forensics</span><span class="nx-chip">Easy</span><span class="nx-chip">100 poin</span><span class="nx-badge nx-badge-verified">VERIFIED</span></div>


| Field | Nilai |
|---|---|
| Event | `umum/mahasiswa_nf` |
| Kategori | `Forensics` |
| Author | `Zer0` |
| Difficulty | `Easy` |
| Poin (snapshot) | `100` |
| Tools | exiftool |
| Flag | `NFX{zip_t1221_cdn-jarvis-update.example_jarvis-ir-case-2026-0211}` |
| Status | `VERIFIED` |
| Snapshot | 2026-11-13 |

[← Kembali ke Index](index.md)


## TL;DR

- **Flag:** `NFX{zip_t1221_cdn-jarvis-update.example_jarvis-ir-case-2026-0211}`
- **Baca langkah lengkap:** [Cara Mendapatkan Flag](73-file-analysis-the-suspicious-invoice-02-cara-mendapatkan-flag.md)

## Challenge Brief (platform)

![00-challenge-platform.png](assets/file-analysis-the-suspicious-invoice/00-challenge-platform.png)

*Challenge brief asli di platform NFX CTF 2026.*

## Alur & Titik Penting

| # | Langkah | Titik penting | Buka |
|---:|---|---|---|
| 1 | Recon Artefak | DOCX = ZIP, ada `attachedTemplate`. | [Buka](73-file-analysis-the-suspicious-invoice-01-recon-artefak.md) |
| 2 | Cara Mendapatkan Flag | T1221 + domain + case ID. | [Buka](73-file-analysis-the-suspicious-invoice-02-cara-mendapatkan-flag.md) |
| 3 | Flag | NFX{zip_t1221_cdn-jarvis-update.example_jarvis-ir-case-2026-0211} | [Buka](73-file-analysis-the-suspicious-invoice-03-flag.md) |
| 4 | Bukti / Evidence | arsip screenshot dan transkrip | [Buka](73-file-analysis-the-suspicious-invoice-04-bukti-evidence.md) |
| 5 | Referensi | File carving, ZIP extraction, IOC. | [Buka](73-file-analysis-the-suspicious-invoice-05-referensi.md) |

## Cerita singkat

DOCX adalah ZIP. `settings.xml.rels` menunjuk template eksternal (T1221). Flag disusun dari tipe file, teknik, domain, dan case ID di metadata.

<div class="nx-evidence-preview"><a href="73-file-analysis-the-suspicious-invoice-04-bukti-evidence.html"><img src="assets/file-analysis-the-suspicious-invoice/00b-terminal-evidence.png" alt="Pratinjau evidence File Analysis: The Suspicious Invoice" loading="lazy"></a><span>Pratinjau evidence. Buka halaman <a href="73-file-analysis-the-suspicious-invoice-04-bukti-evidence.html">Evidence / Bukti</a> untuk semua screenshot dan transkrip.</span></div>

## Navigasi Halaman

<div class="nx-page-grid">
<a class="nx-page-card" href="73-file-analysis-the-suspicious-invoice-01-recon-artefak.html"><b>Recon Artefak</b><span>Enumerasi target dan bukti awal</span></a>
<a class="nx-page-card" href="73-file-analysis-the-suspicious-invoice-02-cara-mendapatkan-flag.html"><b>Cara Mendapatkan Flag</b><span>Flag dan verifikasi platform</span></a>
<a class="nx-page-card" href="73-file-analysis-the-suspicious-invoice-03-flag.html"><b>Flag</b><span>Flag dan verifikasi platform</span></a>
<a class="nx-page-card" href="73-file-analysis-the-suspicious-invoice-04-bukti-evidence.html"><b>Bukti / Evidence</b><span>Screenshot, transkrip, dan artefak</span></a>
<a class="nx-page-card" href="73-file-analysis-the-suspicious-invoice-05-referensi.html"><b>Referensi</b><span>Sumber dan bacaan lanjutan</span></a>
</div>
