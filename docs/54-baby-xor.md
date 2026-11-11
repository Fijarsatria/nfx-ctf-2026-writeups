# Baby XOR

<div class="nx-challenge-head"><span class="nx-chip">Track Mahasiswa NF · Reverse</span><span class="nx-chip">Baby</span><span class="nx-chip">260 poin</span><span class="nx-badge nx-badge-verified">VERIFIED</span></div>


| Field | Nilai |
|---|---|
| Event | `umum/mahasiswa_nf` |
| Kategori | `Reverse` |
| Difficulty | `Baby` |
| Poin | `260` |
| Author | `cypera` |
| Tools | objdump |
| Flag | `NFX{x0r_1s_fun_but_n0t_s3cur3}` |
| Status | `VERIFIED` |

[← Kembali ke Index](index.md)

## Challenge Brief (platform)

![00-challenge-platform.png](assets/baby-xor/00-challenge-platform.png)

*Challenge brief asli di platform NFX CTF 2026.*

## Alur & Titik Penting

| # | Langkah | Titik penting | Buka |
|---:|---|---|---|
| 1 | Recon | file baby_xor | [Buka](54-baby-xor-01-recon.md) |
| 2 | Analisis | Byte 14 1c 02 21 ... | [Buka](54-baby-xor-02-analisis.md) |
| 3 | Solver | NFX{x0r_1s_fun_but_n0t_s3cur3} | [Buka](54-baby-xor-03-solver.md) |
| 4 | Flag | NFX{x0r_1s_fun_but_n0t_s3cur3} | [Buka](54-baby-xor-04-flag.md) |
| 5 | Bukti / Evidence | arsip screenshot dan transkrip | [Buka](54-baby-xor-05-bukti-evidence.md) |
| 6 | Referensi | — | [Buka](54-baby-xor-06-referensi.md) |

## Cerita singkat

Jadi ceritanya gini. Kali ini flagnya tidak muncul sebagai plaintext. Binary menyimpan byte-byte hasil XOR dengan satu kunci 8-bit. Karena kuncinya cuma 0–255, kita bisa coba semua kemungkinan sampai keluar format `NFX{`.

<div class="nx-evidence-preview"><a href="54-baby-xor-05-bukti-evidence.html"><img src="assets/baby-xor/00b-submit-platform.png" alt="Pratinjau evidence Baby XOR" loading="lazy"></a><span>Pratinjau evidence. Buka halaman <a href="54-baby-xor-05-bukti-evidence.html">Evidence / Bukti</a> untuk semua screenshot dan transkrip.</span></div>

## Navigasi Halaman

<div class="nx-page-grid">
<a class="nx-page-card" href="54-baby-xor-01-recon.html"><b>Recon</b><span>Enumerasi target dan bukti awal</span></a>
<a class="nx-page-card" href="54-baby-xor-02-analisis.html"><b>Analisis</b><span>Membaca alur dan akar masalah</span></a>
<a class="nx-page-card" href="54-baby-xor-03-solver.html"><b>Solver</b><span>Langkah exploit dan solver</span></a>
<a class="nx-page-card" href="54-baby-xor-04-flag.html"><b>Flag</b><span>Flag dan verifikasi platform</span></a>
<a class="nx-page-card" href="54-baby-xor-05-bukti-evidence.html"><b>Bukti / Evidence</b><span>Screenshot, transkrip, dan artefak</span></a>
<a class="nx-page-card" href="54-baby-xor-06-referensi.html"><b>Referensi</b><span>Sumber dan bacaan lanjutan</span></a>
</div>
