# Baby Python

<div class="nx-challenge-head"><span class="nx-chip">Track Mahasiswa NF · Reverse</span><span class="nx-chip">Baby</span><span class="nx-chip">200 poin</span><span class="nx-badge nx-badge-verified">VERIFIED</span></div>


| Field | Nilai |
|---|---|
| Event | `umum/mahasiswa_nf` |
| Kategori | `Reverse` |
| Difficulty | `Baby` |
| Poin | `200` |
| Author | `cypera` |
| Tools | python3 |
| Flag | `NFX{pyth0n_scr1pt_k1ds_4r3_n0t_s4f3}` |
| Status | `VERIFIED` |

[← Kembali ke Index](index.md)

## Challenge Brief (platform)

![00-challenge-platform.png](assets/baby-python/00-challenge-platform.png)

*Challenge brief asli di platform NFX CTF 2026.*

## Alur & Titik Penting

| # | Langkah | Titik penting | Buka |
|---:|---|---|---|
| 1 | Recon | — | [Buka](55-baby-python-01-recon.md) |
| 2 | Analisis | candidate[::-1] berarti input dibalik. | [Buka](55-baby-python-02-analisis.md) |
| 3 | Solver | python3 baby_python.py 'NFX{pyth0n_scr1pt_k1ds_4r3_n0t_s4f3}' | [Buka](55-baby-python-03-solver.md) |
| 4 | Flag | NFX{pyth0n_scr1pt_k1ds_4r3_n0t_s4f3} | [Buka](55-baby-python-04-flag.md) |
| 5 | Bukti / Evidence | arsip screenshot dan transkrip | [Buka](55-baby-python-05-bukti-evidence.md) |
| 6 | Referensi | — | [Buka](55-baby-python-06-referensi.md) |

## Cerita singkat

Jadi ceritanya gini. Kita dikasih script Python yang “mengamankan” flag dengan cara membalik urutan karakter, lalu meng-encode hasilnya ke base64. Karena prosesnya reversibel, kita tinggal decode base64 lalu balik lagi urutannya.

<div class="nx-evidence-preview"><a href="55-baby-python-05-bukti-evidence.html"><img src="assets/baby-python/00b-submit-platform.png" alt="Pratinjau evidence Baby Python" loading="lazy"></a><span>Pratinjau evidence. Buka halaman <a href="55-baby-python-05-bukti-evidence.html">Evidence / Bukti</a> untuk semua screenshot dan transkrip.</span></div>

## Navigasi Halaman

<div class="nx-page-grid">
<a class="nx-page-card" href="55-baby-python-01-recon.html"><b>Recon</b><span>Enumerasi target dan bukti awal</span></a>
<a class="nx-page-card" href="55-baby-python-02-analisis.html"><b>Analisis</b><span>Membaca alur dan akar masalah</span></a>
<a class="nx-page-card" href="55-baby-python-03-solver.html"><b>Solver</b><span>Langkah exploit dan solver</span></a>
<a class="nx-page-card" href="55-baby-python-04-flag.html"><b>Flag</b><span>Flag dan verifikasi platform</span></a>
<a class="nx-page-card" href="55-baby-python-05-bukti-evidence.html"><b>Bukti / Evidence</b><span>Screenshot, transkrip, dan artefak</span></a>
<a class="nx-page-card" href="55-baby-python-06-referensi.html"><b>Referensi</b><span>Sumber dan bacaan lanjutan</span></a>
</div>
