# Hard VM Bytecode

<div class="nx-challenge-head"><span class="nx-chip">Track Umum / Extend · Reverse</span><span class="nx-chip">Hard</span><span class="nx-chip">100 poin</span><span class="nx-badge nx-badge-verified">VERIFIED</span></div>


| Field | Nilai |
|---|---|
| Event | `umum_Extend` |
| Kategori | `Reverse` |
| Difficulty | `Hard` |
| Poin | `100` |
| Author | `cypera` |
| Solves | `21` |
| Tools | python3, pwntools, checksec, gdb, objdump, readelf, strings, sage |
| Flag | `NFX{vm_byt3c0d3_1s_l1k3_4_puzzl3}` |
| Status | `VERIFIED` |

[← Kembali ke Index](index.md)

## Challenge Brief (platform)

![00-challenge-platform.png](assets/hard-vm-bytecode/00-challenge-platform.png)

*Challenge brief asli di platform NFX CTF 2026.*

## TL;DR

- `hard_vm` bukan validator biasa: ia adalah **interpreter bytecode** mini dengan 498 byte program di `.rodata` `0x2080`.
- Dispatch table di `0x2060` memetakan opcode: `1=LOAD`, `2=XOR`, `3=ADD`, `4=ROL`, `5=CMP`, `0xff=OK`, `0=HALT/gagal`.
- Setiap karakter flag diproses dengan pola 5 instruksi: `LOAD`, `XOR`, `ADD`, `ROL`, `CMP`.
- Dengan membalik urutan operasi (`CMP → ROL⁻¹ → ADD⁻¹ → XOR⁻¹`), semua 33 karakter dapat dipulihkan tanpa menjalankan binary.
- Flag: `NFX{vm_byt3c0d3_1s_l1k3_4_puzzl3}`.

<div class="nx-evidence-preview"><a href="45-hard-vm-bytecode-03-perintah-akuisisi-bukti.html"><img src="assets/hard-vm-bytecode/00b-submit-platform.png" alt="Pratinjau evidence Hard VM Bytecode" loading="lazy"></a><span>Pratinjau evidence. Buka halaman <a href="45-hard-vm-bytecode-03-perintah-akuisisi-bukti.html">Evidence / Bukti</a> untuk semua screenshot dan transkrip.</span></div>

## Navigasi Halaman

<div class="nx-page-grid">
<a class="nx-page-card" href="45-hard-vm-bytecode-01-recon.html"><b>Recon</b><span>Enumerasi target dan bukti awal</span></a>
<a class="nx-page-card" href="45-hard-vm-bytecode-02-triage-awal.html"><b>Triage awal</b><span>Baca bagian ini</span></a>
<a class="nx-page-card" href="45-hard-vm-bytecode-03-perintah-akuisisi-bukti.html"><b>Perintah akuisisi bukti</b><span>Screenshot, transkrip, dan artefak</span></a>
<a class="nx-page-card" href="45-hard-vm-bytecode-04-main-dan-layout.html"><b>Main dan layout</b><span>Baca bagian ini</span></a>
<a class="nx-page-card" href="45-hard-vm-bytecode-05-format-instruksi.html"><b>Format instruksi</b><span>Baca bagian ini</span></a>
<a class="nx-page-card" href="45-hard-vm-bytecode-06-analisis.html"><b>Analisis</b><span>Membaca alur dan akar masalah</span></a>
<a class="nx-page-card" href="45-hard-vm-bytecode-07-membalik-transformasi.html"><b>Membalik transformasi</b><span>Baca bagian ini</span></a>
<a class="nx-page-card" href="45-hard-vm-bytecode-08-strategi.html"><b>Strategi</b><span>Baca bagian ini</span></a>
<a class="nx-page-card" href="45-hard-vm-bytecode-09-solver-lengkap.html"><b>Solver lengkap</b><span>Langkah exploit dan solver</span></a>
<a class="nx-page-card" href="45-hard-vm-bytecode-10-output-asli.html"><b>Output asli</b><span>Baca bagian ini</span></a>
<a class="nx-page-card" href="45-hard-vm-bytecode-11-flag.html"><b>Flag</b><span>Flag dan verifikasi platform</span></a>
<a class="nx-page-card" href="45-hard-vm-bytecode-12-bukti-evidence.html"><b>Bukti / Evidence</b><span>Screenshot, transkrip, dan artefak</span></a>
<a class="nx-page-card" href="45-hard-vm-bytecode-13-referensi.html"><b>Referensi</b><span>Sumber dan bacaan lanjutan</span></a>
</div>
