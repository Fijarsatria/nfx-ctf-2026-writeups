# Hard Feistel — Evidence / Bukti

<div class="nx-challenge-head"><span class="nx-chip">14 screenshot</span><span class="nx-chip">10 transkrip / script</span></div>


[← Overview](44-hard-feistel.md) · [Index](index.md)

> **Langkah 12/13 — Bukti / Evidence.** Bukti / Evidence
>
> **Titik penting:** arsip screenshot dan transkrip
>
> **Berikutnya:** [Referensi](44-hard-feistel-13-referensi.md)


## Arsip Evidence

> Semua file berasal dari `assets/hard-feistel/`. Screenshot platform dan terminal adalah bukti asli dari sesi solve; transkrip mentah tetap ditautkan di bagian bawah.

### Platform

<div class="nx-evidence-grid">
<figure><a href="assets/hard-feistel/00-challenge-platform.png" target="_blank" rel="noopener"><img src="assets/hard-feistel/00-challenge-platform.png" alt="00-challenge-platform.png" loading="lazy"></a><figcaption>00-challenge-platform.png</figcaption></figure>
</div>

*Challenge brief asli di platform NFX CTF 2026.*

<div class="nx-evidence-grid">
<figure><a href="assets/hard-feistel/00b-terminal-evidence.png" target="_blank" rel="noopener"><img src="assets/hard-feistel/00b-terminal-evidence.png" alt="Terminal evidence (real)" loading="lazy"></a><figcaption>Terminal evidence (real)</figcaption></figure>
</div>

*Terminal evidence (real).*

### Terminal (arsip sesi)

<div class="nx-evidence-grid">
<figure><a href="assets/hard-feistel/term-01-identitas.png" target="_blank" rel="noopener"><img src="assets/hard-feistel/term-01-identitas.png" alt="term-01-identitas.png" loading="lazy"></a><figcaption>term-01-identitas.png</figcaption></figure>
</div>

*Terminal evidence — `01-identitas.txt` (arsip transkrip sesi solve).*

<div class="nx-evidence-grid">
<figure><a href="assets/hard-feistel/term-02-readelf.png" target="_blank" rel="noopener"><img src="assets/hard-feistel/term-02-readelf.png" alt="term-02-readelf.png" loading="lazy"></a><figcaption>term-02-readelf.png</figcaption></figure>
</div>

*Terminal evidence — `02-readelf.txt` (arsip transkrip sesi solve).*

<div class="nx-evidence-grid">
<figure><a href="assets/hard-feistel/term-03-strings.png" target="_blank" rel="noopener"><img src="assets/hard-feistel/term-03-strings.png" alt="term-03-strings.png" loading="lazy"></a><figcaption>term-03-strings.png</figcaption></figure>
</div>

*Terminal evidence — `03-strings.txt` (arsip transkrip sesi solve).*

<div class="nx-evidence-grid">
<figure><a href="assets/hard-feistel/term-04-disasm.png" target="_blank" rel="noopener"><img src="assets/hard-feistel/term-04-disasm.png" alt="term-04-disasm.png" loading="lazy"></a><figcaption>term-04-disasm.png</figcaption></figure>
</div>

*Terminal evidence — `04-disasm.txt` (arsip transkrip sesi solve).*

<div class="nx-evidence-grid">
<figure><a href="assets/hard-feistel/term-05-rodata-data-hexdump.png" target="_blank" rel="noopener"><img src="assets/hard-feistel/term-05-rodata-data-hexdump.png" alt="term-05-rodata-data-hexdump.png" loading="lazy"></a><figcaption>term-05-rodata-data-hexdump.png</figcaption></figure>
</div>

*Terminal evidence — `05-rodata-data-hexdump.txt` (arsip transkrip sesi solve).*

<div class="nx-evidence-grid">
<figure><a href="assets/hard-feistel/term-06-solver-output.png" target="_blank" rel="noopener"><img src="assets/hard-feistel/term-06-solver-output.png" alt="term-06-solver-output.png" loading="lazy"></a><figcaption>term-06-solver-output.png</figcaption></figure>
</div>

*Terminal evidence — `06-solver-output.txt` (arsip transkrip sesi solve).*

<div class="nx-evidence-grid">
<figure><a href="assets/hard-feistel/term-07-verifikasi.png" target="_blank" rel="noopener"><img src="assets/hard-feistel/term-07-verifikasi.png" alt="term-07-verifikasi.png" loading="lazy"></a><figcaption>term-07-verifikasi.png</figcaption></figure>
</div>

*Terminal evidence — `07-verifikasi.txt` (arsip transkrip sesi solve).*

<div class="nx-evidence-grid">
<figure><a href="assets/hard-feistel/term-08-checksec.png" target="_blank" rel="noopener"><img src="assets/hard-feistel/term-08-checksec.png" alt="term-08-checksec.png" loading="lazy"></a><figcaption>term-08-checksec.png</figcaption></figure>
</div>

*Terminal evidence — `08-checksec.txt` (arsip transkrip sesi solve).*

<div class="nx-evidence-grid">
<figure><a href="assets/hard-feistel/term-08-gdb-output-buffer.png" target="_blank" rel="noopener"><img src="assets/hard-feistel/term-08-gdb-output-buffer.png" alt="term-08-gdb-output-buffer.png" loading="lazy"></a><figcaption>term-08-gdb-output-buffer.png</figcaption></figure>
</div>

*Terminal evidence — `08-gdb-output-buffer.txt` (arsip transkrip sesi solve).*

### Screenshot langkah

<div class="nx-evidence-grid">
<figure><a href="assets/hard-feistel/01-solver.png" target="_blank" rel="noopener"><img src="assets/hard-feistel/01-solver.png" alt="01-solver.png" loading="lazy"></a><figcaption>01-solver.png</figcaption></figure>
</div>

*Evidence — `01-solver.png`.*

<div class="nx-evidence-grid">
<figure><a href="assets/hard-feistel/02-verifikasi.png" target="_blank" rel="noopener"><img src="assets/hard-feistel/02-verifikasi.png" alt="02-verifikasi.png" loading="lazy"></a><figcaption>02-verifikasi.png</figcaption></figure>
</div>

*Evidence — `02-verifikasi.png`.*

<div class="nx-evidence-grid">
<figure><a href="assets/hard-feistel/03-gdb.png" target="_blank" rel="noopener"><img src="assets/hard-feistel/03-gdb.png" alt="03-gdb.png" loading="lazy"></a><figcaption>03-gdb.png</figcaption></figure>
</div>

*Evidence — `03-gdb.png`.*

### Transkrip mentah & script

- [`01-identitas.txt`](assets/hard-feistel/01-identitas.txt)
- [`02-readelf.txt`](assets/hard-feistel/02-readelf.txt)
- [`03-strings.txt`](assets/hard-feistel/03-strings.txt)
- [`04-disasm.txt`](assets/hard-feistel/04-disasm.txt)
- [`05-rodata-data-hexdump.txt`](assets/hard-feistel/05-rodata-data-hexdump.txt)
- [`06-solver-output.txt`](assets/hard-feistel/06-solver-output.txt)
- [`07-verifikasi.txt`](assets/hard-feistel/07-verifikasi.txt)
- [`08-checksec.txt`](assets/hard-feistel/08-checksec.txt)
- [`08-gdb-output-buffer.txt`](assets/hard-feistel/08-gdb-output-buffer.txt)
- [`solve_feistel.py`](assets/hard-feistel/solve_feistel.py)

## Validasi platform (real)

![Validasi platform — CORRECT, BUT ALREADY SOLVED.](assets/hard-feistel/00b-platform-validation.png)

*Screenshot asli dari platform NFX CTF 2026. Platform menjawab
`CORRECT, BUT ALREADY SOLVED.` untuk flag ini.*


## Tabel Evidence

| Bukti | File | Keterangan |
|---|---|---|
| Identitas & hash | `01-identitas.txt` | `file`, hash, permission |
| ELF metadata | `02-readelf.txt` | Header, segmen, section |
| Strings | `03-strings.txt` | `strings -n 4` |
| Disassembly | `04-disasm.txt` | Round function dan serialisasi |
| Hex dump | `05-rodata-data-hexdump.txt` | Round key `.rodata` + ciphertext `.data` |
| Solver | `solve_feistel.py` | Dekripsi Feistel |
| Output solver | `06-solver-output.txt` | Output asli |
| Verifikasi | `07-verifikasi.txt` | Salah vs benar + hash |
| Checksec | `08-checksec.txt` | Hasil `ELF.checksec()` |
| gdb buffer | `08-gdb-output-buffer.txt` | Bukti output == ciphertext |
| Screenshot solver | `01-solver.png` | Render output solver |
| Screenshot verifikasi | `02-verifikasi.png` | Render output verifikasi |
| Screenshot gdb | `03-gdb.png` | Render bukti gdb |