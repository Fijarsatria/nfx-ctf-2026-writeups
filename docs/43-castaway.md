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

## TL;DR

- `castaway` membaca calon flag dari **stdin** (`fgets`), bukan dari argumen.
- Panjang harus tepat **40 byte**. Program menjalankan transformasi per byte dengan **state machine**, **rolling key**, **S-box 256 byte**, dan **S-box 16 byte**.
- Ada **opaque predicate** `(i*i) & 3 == 2` yang selalu false, sehingga state `0x32` (yang akan menulis `0xff`) adalah dead code.
- Ada **anti-debug** `ptrace(PTRACE_TRACEME)`: jika return `-1` (dijalankan di bawah debugger), byte hasil transformasi pertama di-XOR `1`, sehingga flag benar tetap ditolak.
- Inversi dilakukan per byte dengan brute force 256 kandidat; key state dipulihkan berurutan dari ciphertext.
- Flag: `NFX{c4st4w4y_0n_4n_0p4qu3_st4t3_m4ch1n3}`.

<div class="nx-evidence-preview"><a href="43-castaway-05-bukti-evidence.html"><img src="assets/castaway/98-terminal-evidence.png" alt="Pratinjau evidence Castaway" loading="lazy"></a><span>Pratinjau evidence. Buka halaman <a href="43-castaway-05-bukti-evidence.html">Evidence / Bukti</a> untuk semua screenshot dan transkrip.</span></div>

## Navigasi Halaman

<div class="nx-page-grid">
<a class="nx-page-card" href="43-castaway-01-recon.html"><b>Recon</b><span>Enumerasi target dan bukti awal</span></a>
<a class="nx-page-card" href="43-castaway-02-analisis.html"><b>Analisis</b><span>Membaca alur dan akar masalah</span></a>
<a class="nx-page-card" href="43-castaway-03-eksploitasi-solver.html"><b>Eksploitasi / Solver</b><span>Langkah exploit dan solver</span></a>
<a class="nx-page-card" href="43-castaway-04-flag.html"><b>Flag</b><span>Flag dan verifikasi platform</span></a>
<a class="nx-page-card" href="43-castaway-05-bukti-evidence.html"><b>Bukti / Evidence</b><span>Screenshot, transkrip, dan artefak</span></a>
<a class="nx-page-card" href="43-castaway-06-referensi.html"><b>Referensi</b><span>Sumber dan bacaan lanjutan</span></a>
</div>
