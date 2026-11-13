# Easy JS Obfuscation

<div class="nx-challenge-head"><span class="nx-chip">Track Mahasiswa NF · Reverse</span><span class="nx-chip">Easy</span><span class="nx-chip">260 poin</span><span class="nx-badge nx-badge-verified">VERIFIED</span></div>


| Field | Nilai |
|---|---|
| Event | `umum/mahasiswa_nf` |
| Kategori | `Reverse` |
| Difficulty | `Easy` |
| Poin | `260` |
| Author | `cypera` |
| Flag | `NFX{j4v4scr1pt_0bfusc4t3d_but_st1ll_r34d4bl3}` |
| Status | `VERIFIED` |
[← Kembali ke Index](index.md)


## TL;DR

- **Flag:** `NFX{j4v4scr1pt_0bfusc4t3d_but_st1ll_r34d4bl3}`
- **Baca langkah lengkap:** [Cara Mendapatkan Flag](60-easy-js-obfuscation-04-flag.md)

## Challenge Brief (platform)

![00-challenge-platform.png](assets/easy-js-obfuscation/00-challenge-platform.png)

*Challenge brief asli di platform NFX CTF 2026.*

## Alur & Titik Penting

| # | Langkah | Titik penting | Buka |
|---:|---|---|---|
| 1 | Recon | Di dalamnya ada fungsi: | [Buka](60-easy-js-obfuscation-01-recon.md) |
| 2 | Analisis | Prosesnya: XOR 0x33 per byte, lalu reverse. | [Buka](60-easy-js-obfuscation-02-analisis.md) |
| 3 | Solver | NFX{j4v4scr1pt_0bfusc4t3d_but_st1ll_r34d4bl3} | [Buka](60-easy-js-obfuscation-03-solver.md) |
| 4 | Flag | NFX{j4v4scr1pt_0bfusc4t3d_but_st1ll_r34d4bl3} | [Buka](60-easy-js-obfuscation-04-flag.md) |
| 5 | Bukti / Evidence | arsip screenshot dan transkrip | [Buka](60-easy-js-obfuscation-05-bukti-evidence.md) |
| 6 | Referensi | — | [Buka](60-easy-js-obfuscation-06-referensi.md) |

## Cerita singkat

Jadi ceritanya gini. Flag-nya disembunyiin di array angka JavaScript. Tiap angka di-XOR dengan `0x33`, lalu hasilnya dibalik. Ada dua array: satu flag asli, satu decoy. Kita tinggal decode array yang benar.

<div class="nx-evidence-preview"><a href="60-easy-js-obfuscation-05-bukti-evidence.html"><img src="assets/easy-js-obfuscation/00b-terminal-evidence.png" alt="Pratinjau evidence Easy JS Obfuscation" loading="lazy"></a><span>Pratinjau evidence. Buka halaman <a href="60-easy-js-obfuscation-05-bukti-evidence.html">Evidence / Bukti</a> untuk semua screenshot dan transkrip.</span></div>

## Navigasi Halaman

<div class="nx-page-grid">
<a class="nx-page-card" href="60-easy-js-obfuscation-01-recon.html"><b>Recon</b><span>Enumerasi target dan bukti awal</span></a>
<a class="nx-page-card" href="60-easy-js-obfuscation-02-analisis.html"><b>Analisis</b><span>Membaca alur dan akar masalah</span></a>
<a class="nx-page-card" href="60-easy-js-obfuscation-03-solver.html"><b>Solver</b><span>Langkah exploit dan solver</span></a>
<a class="nx-page-card" href="60-easy-js-obfuscation-04-flag.html"><b>Flag</b><span>Flag dan verifikasi platform</span></a>
<a class="nx-page-card" href="60-easy-js-obfuscation-05-bukti-evidence.html"><b>Bukti / Evidence</b><span>Screenshot, transkrip, dan artefak</span></a>
<a class="nx-page-card" href="60-easy-js-obfuscation-06-referensi.html"><b>Referensi</b><span>Sumber dan bacaan lanjutan</span></a>
</div>
