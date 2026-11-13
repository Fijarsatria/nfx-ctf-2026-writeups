# Baby Strings

<div class="nx-challenge-head"><span class="nx-chip">Track Mahasiswa NF · Reverse</span><span class="nx-chip">Baby</span><span class="nx-chip">200 poin</span><span class="nx-badge nx-badge-verified">VERIFIED</span></div>


| Field | Nilai |
|---|---|
| Event | `umum/mahasiswa_nf` |
| Kategori | `Reverse` |
| Difficulty | `Baby` |
| Poin (snapshot) | `200` |
| Author | `cypera` |
| Tools | strings |
| Flag | `NFX{str1ngs_4r3_y0ur_b3st_fr13nd}` |
| Status | `VERIFIED` |
| Snapshot | 2026-11-13 |

[← Kembali ke Index](index.md)


## TL;DR

- **Flag:** `NFX{str1ngs_4r3_y0ur_b3st_fr13nd}`
- **Baca langkah lengkap:** [Cara Mendapatkan Flag](53-baby-strings-04-flag.md)

## Challenge Brief (platform)

![00-challenge-platform.png](assets/baby-strings/00-challenge-platform.png)

*Challenge brief asli di platform NFX CTF 2026.*

## Alur & Titik Penting

| # | Langkah | Titik penting | Buka |
|---:|---|---|---|
| 1 | Recon | file baby_strings | [Buka](53-baby-strings-01-recon.md) |
| 2 | Analisis | Flag muncul langsung sebagai string biasa. | [Buka](53-baby-strings-02-analisis.md) |
| 3 | Solver | NFX{str1ngs_4r3_y0ur_b3st_fr13nd} | [Buka](53-baby-strings-03-solver.md) |
| 4 | Flag | NFX{str1ngs_4r3_y0ur_b3st_fr13nd} | [Buka](53-baby-strings-04-flag.md) |
| 5 | Bukti / Evidence | arsip screenshot dan transkrip | [Buka](53-baby-strings-05-bukti-evidence.md) |
| 6 | Referensi | — | [Buka](53-baby-strings-06-referensi.md) |

## Cerita singkat

Jadi ceritanya gini. Kita dikasih satu binary ELF kecil bernama `baby_strings`. Programnya cuma minta flag, lalu membandingkan input kita dengan flag yang tersimpan di dalam binary. Karena flagnya tidak dienkripsi, kita bisa langsung intip pakai `strings`.

<div class="nx-evidence-preview"><a href="53-baby-strings-05-bukti-evidence.html"><img src="assets/baby-strings/00b-terminal-evidence.png" alt="Pratinjau evidence Baby Strings" loading="lazy"></a><span>Pratinjau evidence. Buka halaman <a href="53-baby-strings-05-bukti-evidence.html">Evidence / Bukti</a> untuk semua screenshot dan transkrip.</span></div>

## Navigasi Halaman

<div class="nx-page-grid">
<a class="nx-page-card" href="53-baby-strings-01-recon.html"><b>Recon</b><span>Enumerasi target dan bukti awal</span></a>
<a class="nx-page-card" href="53-baby-strings-02-analisis.html"><b>Analisis</b><span>Membaca alur dan akar masalah</span></a>
<a class="nx-page-card" href="53-baby-strings-03-solver.html"><b>Solver</b><span>Langkah exploit dan solver</span></a>
<a class="nx-page-card" href="53-baby-strings-04-flag.html"><b>Flag</b><span>Flag dan verifikasi platform</span></a>
<a class="nx-page-card" href="53-baby-strings-05-bukti-evidence.html"><b>Bukti / Evidence</b><span>Screenshot, transkrip, dan artefak</span></a>
<a class="nx-page-card" href="53-baby-strings-06-referensi.html"><b>Referensi</b><span>Sumber dan bacaan lanjutan</span></a>
</div>
