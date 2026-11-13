# Easy Bash Layers

<div class="nx-challenge-head"><span class="nx-chip">Track Mahasiswa NF · Reverse</span><span class="nx-chip">Easy</span><span class="nx-chip">260 poin</span><span class="nx-badge nx-badge-verified">VERIFIED</span></div>


| Field | Nilai |
|---|---|
| Event | `umum/mahasiswa_nf` |
| Kategori | `Reverse` |
| Difficulty | `Easy` |
| Poin (snapshot) | `260` |
| Author | `cypera` |
| Flag | `NFX{b4sh_l4y3rs_w1ll_n0t_st0p_m3}` |
| Status | `VERIFIED` |
| Snapshot | 2026-11-13 |

[← Kembali ke Index](index.md)


## TL;DR

- **Flag:** `NFX{b4sh_l4y3rs_w1ll_n0t_st0p_m3}`
- **Baca langkah lengkap:** [Cara Mendapatkan Flag](59-easy-bash-layers-04-flag.md)

## Challenge Brief (platform)

![00-challenge-platform.png](assets/easy-bash-layers/00-challenge-platform.png)

*Challenge brief asli di platform NFX CTF 2026.*

## Alur & Titik Penting

| # | Langkah | Titik penting | Buka |
|---:|---|---|---|
| 1 | Recon | Bagian pengecekannya: | [Buka](59-easy-bash-layers-01-recon.md) |
| 2 | Analisis | Urutan encode: base64 → reverse → ROT13. | [Buka](59-easy-bash-layers-02-analisis.md) |
| 3 | Solver | NFX{b4sh_l4y3rs_w1ll_n0t_st0p_m3} | [Buka](59-easy-bash-layers-03-solver.md) |
| 4 | Flag | NFX{b4sh_l4y3rs_w1ll_n0t_st0p_m3} | [Buka](59-easy-bash-layers-04-flag.md) |
| 5 | Bukti / Evidence | arsip screenshot dan transkrip | [Buka](59-easy-bash-layers-05-bukti-evidence.md) |
| 6 | Referensi | — | [Buka](59-easy-bash-layers-06-referensi.md) |

## Cerita singkat

Jadi ceritanya gini. Kita dikasih script Bash kecil. Dia mengecek flag dengan tiga lapis: base64, dibalik, lalu ROT13. Karena semua lapisannya reversibel, kita tinggal balik urutannya: ROT13 dulu, balik lagi, lalu decode base64.

<div class="nx-evidence-preview"><a href="59-easy-bash-layers-05-bukti-evidence.html"><img src="assets/easy-bash-layers/00b-terminal-evidence.png" alt="Pratinjau evidence Easy Bash Layers" loading="lazy"></a><span>Pratinjau evidence. Buka halaman <a href="59-easy-bash-layers-05-bukti-evidence.html">Evidence / Bukti</a> untuk semua screenshot dan transkrip.</span></div>

## Navigasi Halaman

<div class="nx-page-grid">
<a class="nx-page-card" href="59-easy-bash-layers-01-recon.html"><b>Recon</b><span>Enumerasi target dan bukti awal</span></a>
<a class="nx-page-card" href="59-easy-bash-layers-02-analisis.html"><b>Analisis</b><span>Membaca alur dan akar masalah</span></a>
<a class="nx-page-card" href="59-easy-bash-layers-03-solver.html"><b>Solver</b><span>Langkah exploit dan solver</span></a>
<a class="nx-page-card" href="59-easy-bash-layers-04-flag.html"><b>Flag</b><span>Flag dan verifikasi platform</span></a>
<a class="nx-page-card" href="59-easy-bash-layers-05-bukti-evidence.html"><b>Bukti / Evidence</b><span>Screenshot, transkrip, dan artefak</span></a>
<a class="nx-page-card" href="59-easy-bash-layers-06-referensi.html"><b>Referensi</b><span>Sumber dan bacaan lanjutan</span></a>
</div>
