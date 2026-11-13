# Feistel Differential

<div class="nx-challenge-head"><span class="nx-chip">Track Mahasiswa NF · Crypto</span><span class="nx-chip">Medium</span><span class="nx-chip">100 poin</span><span class="nx-badge nx-badge-verified">VERIFIED</span></div>


| Field | Nilai |
|---|---|
| Event | `umum/mahasiswa_nf` |
| Kategori | `Crypto` |
| Difficulty | `Medium` |
| Poin (snapshot) | `100` |
| Author | `Illal` |
| Solves | `23` |
| Tools | python3, sage, z3 |
| Flag | `NFXCTF{d1ff3r3nt14l_crypt0_pwn5_f31st3l_45322835}` |
| Status | `VERIFIED` |
| Snapshot | 2026-11-13 |

[← Kembali ke Index](index.md)

## Challenge Brief (platform)

![00-challenge-platform.png](assets/feistel-differential/00-challenge-platform.png)

*Challenge brief asli di platform NFX CTF 2026.*

## Cerita singkat

Jadi ceritanya gini. cipher adalah Feistel 7 ronde pada blok 32-bit (dua half 16-bit), dengan round function `F(x,k) = permute(SBOX_4nibble(x XOR k))`. Terus, `pairs.txt` berisi **280.000 pasangan diferensial**: 14 nilai input difference × 20.000 baris, masing-masing `(p, E(p), E(p XOR Δ))`. Lalu, walaupun datanya "differential", serangan paling bersih adalah **known-plaintext key recovery**: modelkan cipher di z3, minta 7 pasangan pertama, dan seluruh 112 bit round key langsung terpaku. Nah, dari situ kita bisa sampai ke flag dan bukti submit-nya.

## Alur & Titik Penting

| # | Langkah | Titik penting | Buka |
|---:|---|---|---|
| 1 | Recon | xxd flag.enc \| head | [Buka](04-feistel-differential-01-recon.md) |
| 2 | Analisis | File berisi 14 blok, masing-masing 20.000 baris, dengan header: | [Buka](04-feistel-differential-02-analisis.md) |
| 3 | Analisis | Total unknown = 7 × 16 = 112 bit. | [Buka](04-feistel-differential-03-analisis-2.md) |
| 4 | Strategi | — | [Buka](04-feistel-differential-04-strategi.md) |
| 5 | Script lengkap | Tersimpan di docs/assets/feistel-differential/solve.py: | [Buka](04-feistel-differential-05-script-lengkap.md) |
| 6 | Solver | python3 docs/assets/feistel-differential/solve.py | [Buka](04-feistel-differential-06-solver.md) |
| 7 | Flag | NFXCTF{d1ff3r3nt14l_crypt0_pwn5_f31st3l_45322835} | [Buka](04-feistel-differential-07-flag.md) |
| 8 | Bukti / Evidence | arsip screenshot dan transkrip | [Buka](04-feistel-differential-08-bukti-evidence.md) |
| 9 | Referensi | — | [Buka](04-feistel-differential-09-referensi.md) |

## TL;DR

- Cipher adalah Feistel 7 ronde pada blok 32-bit (dua half 16-bit), dengan
  round function `F(x,k) = permute(SBOX_4nibble(x XOR k))`.
- `pairs.txt` berisi **280.000 pasangan diferensial**: 14 nilai input
  difference × 20.000 baris, masing-masing `(p, E(p), E(p XOR Δ))`.
- Walaupun datanya "differential", serangan paling bersih adalah
  **known-plaintext key recovery**: modelkan cipher di z3, minta 7 pasangan
  pertama, dan seluruh 112 bit round key langsung terpaku.
- Diperoleh master key `0xfdec721297377222d7283ab5a383`, subkey
  `[a383, 3ab5, d728, 7222, 9737, 7212, fdec]`.
- Verifikasi: 280.000/280.000 baris cocok. Dekripsi `flag.enc` menghasilkan
  flag + padding PKCS#7 `03 03 03`.

<div class="nx-evidence-preview"><a href="04-feistel-differential-08-bukti-evidence.html"><img src="assets/feistel-differential/00b-terminal-evidence.png" alt="Pratinjau evidence Feistel Differential" loading="lazy"></a><span>Pratinjau evidence. Buka halaman <a href="04-feistel-differential-08-bukti-evidence.html">Evidence / Bukti</a> untuk semua screenshot dan transkrip.</span></div>

## Navigasi Halaman

<div class="nx-page-grid">
<a class="nx-page-card" href="04-feistel-differential-01-recon.html"><b>Recon</b><span>Enumerasi target dan bukti awal</span></a>
<a class="nx-page-card" href="04-feistel-differential-02-analisis.html"><b>Analisis</b><span>Membaca alur dan akar masalah</span></a>
<a class="nx-page-card" href="04-feistel-differential-03-analisis-2.html"><b>Analisis</b><span>Membaca alur dan akar masalah</span></a>
<a class="nx-page-card" href="04-feistel-differential-04-strategi.html"><b>Strategi</b><span>Baca bagian ini</span></a>
<a class="nx-page-card" href="04-feistel-differential-05-script-lengkap.html"><b>Script lengkap</b><span>Baca bagian ini</span></a>
<a class="nx-page-card" href="04-feistel-differential-06-solver.html"><b>Solver</b><span>Langkah exploit dan solver</span></a>
<a class="nx-page-card" href="04-feistel-differential-07-flag.html"><b>Flag</b><span>Flag dan verifikasi platform</span></a>
<a class="nx-page-card" href="04-feistel-differential-08-bukti-evidence.html"><b>Bukti / Evidence</b><span>Screenshot, transkrip, dan artefak</span></a>
<a class="nx-page-card" href="04-feistel-differential-09-referensi.html"><b>Referensi</b><span>Sumber dan bacaan lanjutan</span></a>
</div>
