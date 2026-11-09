# Hard Feistel

<div class="nx-challenge-head"><span class="nx-chip">Track Umum / Extend · Reverse</span><span class="nx-chip">Hard</span><span class="nx-chip">230 poin</span><span class="nx-badge nx-badge-verified">VERIFIED</span></div>


| Field | Nilai |
|---|---|
| Event | `umum_Extend` |
| Kategori | `Reverse` |
| Difficulty | `Hard` |
| Poin | `230` |
| Author | `cypera` |
| Solves | `19` |
| Tools | python3, pwntools, checksec, gdb, objdump, readelf, strings, sage |
| Flag | `NFX{f315t3l_n3tw0rk_16_r0und5_r3v3rs3d}` |
| Status | `VERIFIED` |

[← Kembali ke Index](index.md)

## Challenge Brief (platform)

![00-challenge-platform.png](assets/hard-feistel/00-challenge-platform.png)

*Challenge brief asli di platform NFX CTF 2026.*

## TL;DR

- `hard_feistel` memvalidasi flag 39 byte dari `argv[1]` dan memprosesnya sebagai 10 blok 32-bit.
- Setiap blok dipecah menjadi `L` dan `R` 16-bit, lalu melewati **16 ronde Feistel**.
- Fungsi ronde: `F(R,K) = (((R * 0x9e3779b1) mod 2^32) >> 5) XOR ((K * 257) & 0xffff)`.
- 16 round key 16-bit tertanam di `.rodata` `0x2060`; ciphertext 40 byte di `.data` `0x4020`.
- Output tiap blok adalah `big-endian(L16) || big-endian(R16)`, jadi dekripsi cukup membalik urutan ronde tanpa menginversi `F`.
- Flag: `NFX{f315t3l_n3tw0rk_16_r0und5_r3v3rs3d}`.

<div class="nx-evidence-preview"><a href="44-hard-feistel-03-perintah-akuisisi-bukti.html"><img src="assets/hard-feistel/00b-submit-platform.png" alt="Pratinjau evidence Hard Feistel" loading="lazy"></a><span>Pratinjau evidence. Buka halaman <a href="44-hard-feistel-03-perintah-akuisisi-bukti.html">Evidence / Bukti</a> untuk semua screenshot dan transkrip.</span></div>

## Navigasi Halaman

<div class="nx-page-grid">
<a class="nx-page-card" href="44-hard-feistel-01-recon.html"><b>Recon</b><span>Enumerasi target dan bukti awal</span></a>
<a class="nx-page-card" href="44-hard-feistel-02-triage-awal.html"><b>Triage awal</b><span>Baca bagian ini</span></a>
<a class="nx-page-card" href="44-hard-feistel-03-perintah-akuisisi-bukti.html"><b>Perintah akuisisi bukti</b><span>Screenshot, transkrip, dan artefak</span></a>
<a class="nx-page-card" href="44-hard-feistel-04-analisis.html"><b>Analisis</b><span>Membaca alur dan akar masalah</span></a>
<a class="nx-page-card" href="44-hard-feistel-05-analisis-2.html"><b>Analisis</b><span>Membaca alur dan akar masalah</span></a>
<a class="nx-page-card" href="44-hard-feistel-06-analisis-3.html"><b>Analisis</b><span>Membaca alur dan akar masalah</span></a>
<a class="nx-page-card" href="44-hard-feistel-07-strategi.html"><b>Strategi</b><span>Baca bagian ini</span></a>
<a class="nx-page-card" href="44-hard-feistel-08-solver-lengkap.html"><b>Solver lengkap</b><span>Langkah exploit dan solver</span></a>
<a class="nx-page-card" href="44-hard-feistel-09-output-asli.html"><b>Output asli</b><span>Baca bagian ini</span></a>
<a class="nx-page-card" href="44-hard-feistel-10-verifikasi-tambahan-dengan-gdb.html"><b>Verifikasi tambahan dengan gdb</b><span>Baca bagian ini</span></a>
<a class="nx-page-card" href="44-hard-feistel-11-flag.html"><b>Flag</b><span>Flag dan verifikasi platform</span></a>
<a class="nx-page-card" href="44-hard-feistel-12-bukti-evidence.html"><b>Bukti / Evidence</b><span>Screenshot, transkrip, dan artefak</span></a>
<a class="nx-page-card" href="44-hard-feistel-13-referensi.html"><b>Referensi</b><span>Sumber dan bacaan lanjutan</span></a>
</div>
