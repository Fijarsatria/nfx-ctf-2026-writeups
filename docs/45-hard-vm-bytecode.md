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

## TL;DR

- `hard_vm` bukan validator biasa: ia adalah **interpreter bytecode** mini dengan 498 byte program di `.rodata` `0x2080`.
- Dispatch table di `0x2060` memetakan opcode: `1=LOAD`, `2=XOR`, `3=ADD`, `4=ROL`, `5=CMP`, `0xff=OK`, `0=HALT/gagal`.
- Setiap karakter flag diproses dengan pola 5 instruksi: `LOAD`, `XOR`, `ADD`, `ROL`, `CMP`.
- Dengan membalik urutan operasi (`CMP → ROL⁻¹ → ADD⁻¹ → XOR⁻¹`), semua 33 karakter dapat dipulihkan tanpa menjalankan binary.
- Flag: `NFX{vm_byt3c0d3_1s_l1k3_4_puzzl3}`.

<div class="nx-evidence-preview"><a href="45-hard-vm-bytecode-05-bukti-evidence.html"><img src="assets/hard-vm-bytecode/98-terminal-evidence.png" alt="Pratinjau evidence Hard VM Bytecode" loading="lazy"></a><span>Pratinjau evidence. Buka halaman <a href="45-hard-vm-bytecode-05-bukti-evidence.html">Evidence / Bukti</a> untuk semua screenshot dan transkrip.</span></div>

## Navigasi Halaman

<div class="nx-page-grid">
<a class="nx-page-card" href="45-hard-vm-bytecode-01-recon.html"><b>Recon</b><span>Enumerasi target dan bukti awal</span></a>
<a class="nx-page-card" href="45-hard-vm-bytecode-02-analisis.html"><b>Analisis</b><span>Membaca alur dan akar masalah</span></a>
<a class="nx-page-card" href="45-hard-vm-bytecode-03-eksploitasi-solver.html"><b>Eksploitasi / Solver</b><span>Langkah exploit dan solver</span></a>
<a class="nx-page-card" href="45-hard-vm-bytecode-04-flag.html"><b>Flag</b><span>Flag dan verifikasi platform</span></a>
<a class="nx-page-card" href="45-hard-vm-bytecode-05-bukti-evidence.html"><b>Bukti / Evidence</b><span>Screenshot, transkrip, dan artefak</span></a>
<a class="nx-page-card" href="45-hard-vm-bytecode-06-referensi.html"><b>Referensi</b><span>Sumber dan bacaan lanjutan</span></a>
</div>
