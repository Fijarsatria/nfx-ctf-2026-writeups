# Medium TEA

<div class="nx-challenge-head"><span class="nx-chip">Track Umum / Extend · Reverse</span><span class="nx-chip">Medium</span><span class="nx-chip">100 poin</span><span class="nx-badge nx-badge-verified">VERIFIED</span></div>


| Field | Nilai |
|---|---|
| Event | `umum_Extend` |
| Kategori | `Reverse` |
| Difficulty | `Medium` |
| Poin | `100` |
| Author | `cypera` |
| Solves | `25` |
| Tools | python3, pwntools, checksec, gdb, objdump, readelf, strings, sage |
| Flag | `NFX{t1ny_3ncrypt10n_4lg0r1thm_32_r0und5}` |
| Status | `VERIFIED` |

[← Kembali ke Index](index.md)

## TL;DR

- Binary `medium_tea` memvalidasi flag 40 byte dari `argv[1]`.
- Algoritmanya **TEA 32 ronde**, tetapi empat round key-nya diganti konstanta “lucu”: `0x1337beef`, `0xcafebabe`, `0xdeadc0de`, `0x0badf00d`.
- Flag diproses per blok 64-bit (little-endian), dienkripsi, lalu dibandingkan dengan 5 blok ciphertext di `.rodata` `0x2040`.
- Karena TEA invertibel, dekripsi dilakukan dengan urutan ronde terbalik, `sum` dimulai dari `0xc6ef3720` dan dikurangi `delta` setiap ronde.
- Flag: `NFX{t1ny_3ncrypt10n_4lg0r1thm_32_r0und5}`.

<div class="nx-evidence-preview"><a href="47-medium-tea-05-bukti-evidence.html"><img src="assets/medium-tea/98-terminal-evidence.png" alt="Pratinjau evidence Medium TEA" loading="lazy"></a><span>Pratinjau evidence. Buka halaman <a href="47-medium-tea-05-bukti-evidence.html">Evidence / Bukti</a> untuk semua screenshot dan transkrip.</span></div>

## Navigasi Halaman

<div class="nx-page-grid">
<a class="nx-page-card" href="47-medium-tea-01-recon.html"><b>Recon</b><span>Enumerasi target dan bukti awal</span></a>
<a class="nx-page-card" href="47-medium-tea-02-analisis.html"><b>Analisis</b><span>Membaca alur dan akar masalah</span></a>
<a class="nx-page-card" href="47-medium-tea-03-eksploitasi-solver.html"><b>Eksploitasi / Solver</b><span>Langkah exploit dan solver</span></a>
<a class="nx-page-card" href="47-medium-tea-04-flag.html"><b>Flag</b><span>Flag dan verifikasi platform</span></a>
<a class="nx-page-card" href="47-medium-tea-05-bukti-evidence.html"><b>Bukti / Evidence</b><span>Screenshot, transkrip, dan artefak</span></a>
<a class="nx-page-card" href="47-medium-tea-06-referensi.html"><b>Referensi</b><span>Sumber dan bacaan lanjutan</span></a>
</div>
