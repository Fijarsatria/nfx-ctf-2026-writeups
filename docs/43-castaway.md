# Castaway

<div class="nx-challenge-head"><span class="nx-chip">Track Umum / Extend · Reverse</span><span class="nx-chip">Hard</span><span class="nx-chip">100 poin</span><span class="nx-badge nx-badge-verified">VERIFIED</span></div>


| Field | Nilai |
|---|---|
| Event | `umum_Extend` |
| Kategori | `Reverse` |
| Difficulty | `Hard` |
| Poin | `100` |
| Author | `Kesatria Baja Ringan` |
| Solves | `22` |
| Tools | python3, pwntools, checksec, gdb, objdump, readelf, strings |
| Flag | `NFX{c4st4w4y_0n_4n_0p4qu3_st4t3_m4ch1n3}` |
| Status | `VERIFIED` |

[← Kembali ke Index](index.md)

## Challenge Brief (platform)

![00-challenge-platform.png](assets/castaway/00-challenge-platform.png)

*Challenge brief asli di platform NFX CTF 2026.*

## Alur & Titik Penting

| # | Langkah | Titik penting | Buka |
|---:|---|---|---|
| 1 | Recon | NFX{...} | [Buka](43-castaway-01-recon.md) |
| 2 | Triage awal | file reverse/Hard_03_Castaway/castaway | [Buka](43-castaway-02-triage-awal.md) |
| 3 | Perintah akuisisi bukti | python3 -c "from pwn import *; print(ELF('$BIN').checksec())" \ | [Buka](43-castaway-03-perintah-akuisisi-bukti.md) |
| 4 | Fungsi `main` | Lalu transformasi dan perbandingan: | [Buka](43-castaway-04-fungsi-main.md) |
| 5 | Analisis | strace -f -e trace=ptrace ./reverse/Hard_03_Castaway/castaway < writeups/assets/castaway/castaway_in.txt | [Buka](43-castaway-05-analisis.md) |
| 6 | Fungsi transform `0x1282` | Fungsi ini menerima (input, len, output) dan menjalankan state machine. | [Buka](43-castaway-06-fungsi-transform-0x1282.md) |
| 7 | Transformasi per byte | Saat state 1 dan i < len: | [Buka](43-castaway-07-transformasi-per-byte.md) |
| 8 | Data di `.rodata` | Alamat yang dipakai: | [Buka](43-castaway-08-data-di-rodata.md) |
| 9 | Strategi | Karena S-box 256 byte belum tentu permutasi, brute force 256 kandidat lebih aman daripada mencoba menginversi S-box secara langsung. | [Buka](43-castaway-09-strategi.md) |
| 10 | Solver lengkap | File: writeups/assets/castaway/solvecastaway.py | [Buka](43-castaway-10-solver-lengkap.md) |
| 11 | Output asli | python3 writeups/assets/castaway/solve_castaway.py | [Buka](43-castaway-11-output-asli.md) |
| 12 | Flag | NFX{c4st4w4y_0n_4n_0p4qu3_st4t3_m4ch1n3} | [Buka](43-castaway-12-flag.md) |
| 13 | Bukti / Evidence | arsip screenshot dan transkrip | [Buka](43-castaway-13-bukti-evidence.md) |
| 14 | Referensi | — | [Buka](43-castaway-14-referensi.md) |

## TL;DR

- `castaway` membaca calon flag dari **stdin** (`fgets`), bukan dari argumen.
- Panjang harus tepat **40 byte**. Program menjalankan transformasi per byte dengan **state machine**, **rolling key**, **S-box 256 byte**, dan **S-box 16 byte**.
- Ada **opaque predicate** `(i*i) & 3 == 2` yang selalu false, sehingga state `0x32` (yang akan menulis `0xff`) adalah dead code.
- Ada **anti-debug** `ptrace(PTRACE_TRACEME)`: jika return `-1` (dijalankan di bawah debugger), byte hasil transformasi pertama di-XOR `1`, sehingga flag benar tetap ditolak.
- Inversi dilakukan per byte dengan brute force 256 kandidat; key state dipulihkan berurutan dari ciphertext.
- Flag: `NFX{c4st4w4y_0n_4n_0p4qu3_st4t3_m4ch1n3}`.

<div class="nx-evidence-preview"><a href="43-castaway-03-perintah-akuisisi-bukti.html"><img src="assets/castaway/00b-submit-platform.png" alt="Pratinjau evidence Castaway" loading="lazy"></a><span>Pratinjau evidence. Buka halaman <a href="43-castaway-03-perintah-akuisisi-bukti.html">Evidence / Bukti</a> untuk semua screenshot dan transkrip.</span></div>

## Navigasi Halaman

<div class="nx-page-grid">
<a class="nx-page-card" href="43-castaway-01-recon.html"><b>Recon</b><span>Enumerasi target dan bukti awal</span></a>
<a class="nx-page-card" href="43-castaway-02-triage-awal.html"><b>Triage awal</b><span>Baca bagian ini</span></a>
<a class="nx-page-card" href="43-castaway-03-perintah-akuisisi-bukti.html"><b>Perintah akuisisi bukti</b><span>Screenshot, transkrip, dan artefak</span></a>
<a class="nx-page-card" href="43-castaway-04-fungsi-main.html"><b>Fungsi `main`</b><span>Baca bagian ini</span></a>
<a class="nx-page-card" href="43-castaway-05-analisis.html"><b>Analisis</b><span>Membaca alur dan akar masalah</span></a>
<a class="nx-page-card" href="43-castaway-06-fungsi-transform-0x1282.html"><b>Fungsi transform `0x1282`</b><span>Baca bagian ini</span></a>
<a class="nx-page-card" href="43-castaway-07-transformasi-per-byte.html"><b>Transformasi per byte</b><span>Baca bagian ini</span></a>
<a class="nx-page-card" href="43-castaway-08-data-di-rodata.html"><b>Data di `.rodata`</b><span>Baca bagian ini</span></a>
<a class="nx-page-card" href="43-castaway-09-strategi.html"><b>Strategi</b><span>Baca bagian ini</span></a>
<a class="nx-page-card" href="43-castaway-10-solver-lengkap.html"><b>Solver lengkap</b><span>Langkah exploit dan solver</span></a>
<a class="nx-page-card" href="43-castaway-11-output-asli.html"><b>Output asli</b><span>Baca bagian ini</span></a>
<a class="nx-page-card" href="43-castaway-12-flag.html"><b>Flag</b><span>Flag dan verifikasi platform</span></a>
<a class="nx-page-card" href="43-castaway-13-bukti-evidence.html"><b>Bukti / Evidence</b><span>Screenshot, transkrip, dan artefak</span></a>
<a class="nx-page-card" href="43-castaway-14-referensi.html"><b>Referensi</b><span>Sumber dan bacaan lanjutan</span></a>
</div>
