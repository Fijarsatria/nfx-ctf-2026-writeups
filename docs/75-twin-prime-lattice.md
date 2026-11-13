# Twin Prime Lattice

<div class="nx-challenge-head"><span class="nx-chip">Track Mahasiswa NF · Crypto</span><span class="nx-chip">Easy</span><span class="nx-chip">100 poin</span><span class="nx-badge nx-badge-verified">VERIFIED</span></div>


| Field | Nilai |
|---|---|
| Event | `umum/mahasiswa_nf` |
| Kategori | `Crypto` |
| Author | `rio` |
| Difficulty | `Easy` |
| Poin (snapshot) | `100` |
| Flag | `NXCTF{tw1n_pr1m3s_m33t_l4tt1c3_c0pp3r5m1th_af6854ba29a3}` |
| Status | `VERIFIED` |
| Snapshot | 2026-11-13 |

[← Kembali ke Index](index.md)


## TL;DR

- **Flag:** `NXCTF{tw1n_pr1m3s_m33t_l4tt1c3_c0pp3r5m1th_af6854ba29a3}`
- **Baca langkah lengkap:** [Cara Mendapatkan Flag](75-twin-prime-lattice-02-cara-mendapatkan-flag.md)

## Challenge Brief (platform)

![00-challenge-platform.png](assets/twin-prime-lattice/00-challenge-platform.png)

*Challenge brief asli di platform NFX CTF 2026.*

## Alur & Titik Penting

| # | Langkah | Titik penting | Buka |
|---:|---|---|---|
| 1 | Recon | `output.txt`: N, e, c. | [Buka](75-twin-prime-lattice-01-recon.md) |
| 2 | Cara Mendapatkan Flag | Fermat factorization, bukan lattice. | [Buka](75-twin-prime-lattice-02-cara-mendapatkan-flag.md) |
| 3 | Flag | NXCTF{tw1n_pr1m3s_m33t_l4tt1c3_c0pp3r5m1th_af6854ba29a3} | [Buka](75-twin-prime-lattice-03-flag.md) |
| 4 | Bukti / Evidence | arsip screenshot dan transkrip | [Buka](75-twin-prime-lattice-04-bukti-evidence.md) |
| 5 | Referensi | Fermat factorization, RSA twin primes. | [Buka](75-twin-prime-lattice-05-referensi.md) |

## Cerita singkat

Dua faktor RSA berdekatan. Fermat dari `isqrt(N)` memulihkan `p` dan `q`, lalu ciphertext didekripsi biasa. Prefix flag `NXCTF`.

<div class="nx-evidence-preview"><a href="75-twin-prime-lattice-04-bukti-evidence.html"><img src="assets/twin-prime-lattice/00b-terminal-evidence.png" alt="Pratinjau evidence Twin Prime Lattice" loading="lazy"></a><span>Pratinjau evidence. Buka halaman <a href="75-twin-prime-lattice-04-bukti-evidence.html">Evidence / Bukti</a> untuk semua screenshot dan transkrip.</span></div>

## Navigasi Halaman

<div class="nx-page-grid">
<a class="nx-page-card" href="75-twin-prime-lattice-01-recon.html"><b>Recon</b><span>Enumerasi target dan bukti awal</span></a>
<a class="nx-page-card" href="75-twin-prime-lattice-02-cara-mendapatkan-flag.html"><b>Cara Mendapatkan Flag</b><span>Flag dan verifikasi platform</span></a>
<a class="nx-page-card" href="75-twin-prime-lattice-03-flag.html"><b>Flag</b><span>Flag dan verifikasi platform</span></a>
<a class="nx-page-card" href="75-twin-prime-lattice-04-bukti-evidence.html"><b>Bukti / Evidence</b><span>Screenshot, transkrip, dan artefak</span></a>
<a class="nx-page-card" href="75-twin-prime-lattice-05-referensi.html"><b>Referensi</b><span>Sumber dan bacaan lanjutan</span></a>
</div>
