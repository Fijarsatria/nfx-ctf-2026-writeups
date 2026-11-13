# Cihuyyyyyyyyyyyyyyy LWE sikit ahhhh

<div class="nx-challenge-head"><span class="nx-chip">Track Mahasiswa NF · Crypto</span><span class="nx-chip">Medium</span><span class="nx-chip">200 poin</span><span class="nx-badge nx-badge-verified">VERIFIED</span></div>


| Field | Nilai |
|---|---|
| Event | `umum/mahasiswa_nf` |
| Kategori | `Crypto` |
| Difficulty | `Medium` |
| Poin | `200` |
| Author | `Illal` |
| Solves | `16` |
| Tools | curl, python3, sage, fpylll |
| Flag | `NFXCTF{l4tt1c3_sm4ll_s3cr3t_LWE_7e2a0195}` |
| Status | `VERIFIED` |
[← Kembali ke Index](index.md)

## Challenge Brief (platform)

![00-challenge-platform.png](assets/cihuyyyyyyyyyyyyyyy-lwe-sikit-ahhhh/00-challenge-platform.png)

*Challenge brief asli di platform NFX CTF 2026.*

## Cerita singkat

Jadi ceritanya gini. attachment `lwe.py` bukan kode challenge, melainkan **transkrip LWE**: `q=257`, `n=40`, `m=64`, matriks `A` 64×40, vektor `b` 64, dan `ct` 41 byte. Terus, relasinya adalah LWE standar `b = A·s + e (mod 257)` dengan **secret ternary** `s ∈ {-1,0,1}` dan error `e ∈ [-2,2]`. Lalu, karena dimensi kecil dan secret/error sama-sama pendek, instance dapat dipecahkan dengan **Kannan embedding** + LLL/BKZ. Diperoleh `s` dan `e` yang memenuhi 64/64 persamaan. Nah, dari situ kita bisa sampai ke flag dan bukti submit-nya.

## Alur & Titik Penting

| # | Langkah | Titik penting | Buka |
|---:|---|---|---|
| 1 | Recon | head -5 lwe.py | [Buka](03-cihuyyyyyyyyyyyyyyy-lwe-sikit-ahhhh-01-recon.md) |
| 2 | Analisis | Data cocok dengan LWE public key / transkrip satu sisi: | [Buka](03-cihuyyyyyyyyyyyyyyy-lwe-sikit-ahhhh-02-analisis.md) |
| 3 | Solver | Tersimpan di docs/assets/cihuyyyyyyyyyyyyyyy-lwe-sikit-ahhhh/solvelwe.py: | [Buka](03-cihuyyyyyyyyyyyyyyy-lwe-sikit-ahhhh-03-solver.md) |
| 4 | Solver | python3 docs/assets/cihuyyyyyyyyyyyyyyy-lwe-sikit-ahhhh/solve_lwe.py lwe.py | [Buka](03-cihuyyyyyyyyyyyyyyy-lwe-sikit-ahhhh-04-solver-2.md) |
| 5 | Flag | NFXCTF{l4tt1c3_sm4ll_s3cr3t_LWE_7e2a0195} | [Buka](03-cihuyyyyyyyyyyyyyyy-lwe-sikit-ahhhh-05-flag.md) |
| 6 | Bukti / Evidence | arsip screenshot dan transkrip | [Buka](03-cihuyyyyyyyyyyyyyyy-lwe-sikit-ahhhh-06-bukti-evidence.md) |
| 7 | Referensi | Cryptography (2005). | [Buka](03-cihuyyyyyyyyyyyyyyy-lwe-sikit-ahhhh-07-referensi.md) |

## TL;DR

- Attachment `lwe.py` bukan kode challenge, melainkan **transkrip LWE**:
  `q=257`, `n=40`, `m=64`, matriks `A` 64×40, vektor `b` 64, dan `ct` 41 byte.
- Relasinya adalah LWE standar `b = A·s + e (mod 257)` dengan **secret ternary**
  `s ∈ {-1,0,1}` dan error `e ∈ [-2,2]`.
- Karena dimensi kecil dan secret/error sama-sama pendek, instance dapat
  dipecahkan dengan **Kannan embedding** + LLL/BKZ. Diperoleh `s` dan `e` yang
  memenuhi 64/64 persamaan.
- `ct` panjangnya tepat 41 byte, sama dengan panjang flag. Flag diverifikasi
  di platform; KDF/skema enkripsi tidak disertakan di lampiran (lihat §3.4).
- Flag: `NFXCTF{l4tt1c3_sm4ll_s3cr3t_LWE_7e2a0195}`.

<div class="nx-evidence-preview"><a href="03-cihuyyyyyyyyyyyyyyy-lwe-sikit-ahhhh-06-bukti-evidence.html"><img src="assets/cihuyyyyyyyyyyyyyyy-lwe-sikit-ahhhh/00b-terminal-evidence.png" alt="Pratinjau evidence Cihuyyyyyyyyyyyyyyy LWE sikit ahhhh" loading="lazy"></a><span>Pratinjau evidence. Buka halaman <a href="03-cihuyyyyyyyyyyyyyyy-lwe-sikit-ahhhh-06-bukti-evidence.html">Evidence / Bukti</a> untuk semua screenshot dan transkrip.</span></div>

## Navigasi Halaman

<div class="nx-page-grid">
<a class="nx-page-card" href="03-cihuyyyyyyyyyyyyyyy-lwe-sikit-ahhhh-01-recon.html"><b>Recon</b><span>Enumerasi target dan bukti awal</span></a>
<a class="nx-page-card" href="03-cihuyyyyyyyyyyyyyyy-lwe-sikit-ahhhh-02-analisis.html"><b>Analisis</b><span>Membaca alur dan akar masalah</span></a>
<a class="nx-page-card" href="03-cihuyyyyyyyyyyyyyyy-lwe-sikit-ahhhh-03-solver.html"><b>Solver</b><span>Langkah exploit dan solver</span></a>
<a class="nx-page-card" href="03-cihuyyyyyyyyyyyyyyy-lwe-sikit-ahhhh-04-solver-2.html"><b>Solver</b><span>Langkah exploit dan solver</span></a>
<a class="nx-page-card" href="03-cihuyyyyyyyyyyyyyyy-lwe-sikit-ahhhh-05-flag.html"><b>Flag</b><span>Flag dan verifikasi platform</span></a>
<a class="nx-page-card" href="03-cihuyyyyyyyyyyyyyyy-lwe-sikit-ahhhh-06-bukti-evidence.html"><b>Bukti / Evidence</b><span>Screenshot, transkrip, dan artefak</span></a>
<a class="nx-page-card" href="03-cihuyyyyyyyyyyyyyyy-lwe-sikit-ahhhh-07-referensi.html"><b>Referensi</b><span>Sumber dan bacaan lanjutan</span></a>
</div>
