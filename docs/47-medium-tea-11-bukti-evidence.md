# Medium TEA — Evidence / Bukti

<div class="nx-challenge-head"><span class="nx-chip">12 screenshot</span><span class="nx-chip">9 transkrip / script</span></div>


[← Overview](47-medium-tea.md) · [Index](index.md)

> **Langkah 11/12 — Bukti / Evidence.** Bukti / Evidence
>
> **Titik penting:** arsip screenshot dan transkrip
>
> **Berikutnya:** [Referensi](47-medium-tea-12-referensi.md)


## Arsip Evidence

> Semua file berasal dari `assets/medium-tea/`. Screenshot platform dan terminal adalah bukti asli dari sesi solve; transkrip mentah tetap ditautkan di bagian bawah.

### Platform

<div class="nx-evidence-grid">
<figure><a href="assets/medium-tea/00-challenge-platform.png" target="_blank" rel="noopener"><img src="assets/medium-tea/00-challenge-platform.png" alt="00-challenge-platform.png" loading="lazy"></a><figcaption>00-challenge-platform.png</figcaption></figure>
</div>

*Challenge brief asli di platform NFX CTF 2026.*

<div class="nx-evidence-grid">
<figure><a href="assets/medium-tea/00b-submit-platform.png" target="_blank" rel="noopener"><img src="assets/medium-tea/00b-submit-platform.png" alt="00b-submit-platform.png" loading="lazy"></a><figcaption>00b-submit-platform.png</figcaption></figure>
</div>

*Submit flag di platform: `CORRECT, BUT ALREADY SOLVED.`*

### Terminal (arsip sesi)

<div class="nx-evidence-grid">
<figure><a href="assets/medium-tea/term-01-identitas.png" target="_blank" rel="noopener"><img src="assets/medium-tea/term-01-identitas.png" alt="term-01-identitas.png" loading="lazy"></a><figcaption>term-01-identitas.png</figcaption></figure>
</div>

*Terminal evidence — `01-identitas.txt` (arsip transkrip sesi solve).*

<div class="nx-evidence-grid">
<figure><a href="assets/medium-tea/term-02-readelf.png" target="_blank" rel="noopener"><img src="assets/medium-tea/term-02-readelf.png" alt="term-02-readelf.png" loading="lazy"></a><figcaption>term-02-readelf.png</figcaption></figure>
</div>

*Terminal evidence — `02-readelf.txt` (arsip transkrip sesi solve).*

<div class="nx-evidence-grid">
<figure><a href="assets/medium-tea/term-03-strings.png" target="_blank" rel="noopener"><img src="assets/medium-tea/term-03-strings.png" alt="term-03-strings.png" loading="lazy"></a><figcaption>term-03-strings.png</figcaption></figure>
</div>

*Terminal evidence — `03-strings.txt` (arsip transkrip sesi solve).*

<div class="nx-evidence-grid">
<figure><a href="assets/medium-tea/term-04-disasm.png" target="_blank" rel="noopener"><img src="assets/medium-tea/term-04-disasm.png" alt="term-04-disasm.png" loading="lazy"></a><figcaption>term-04-disasm.png</figcaption></figure>
</div>

*Terminal evidence — `04-disasm.txt` (arsip transkrip sesi solve).*

<div class="nx-evidence-grid">
<figure><a href="assets/medium-tea/term-05-rodata-data-hexdump.png" target="_blank" rel="noopener"><img src="assets/medium-tea/term-05-rodata-data-hexdump.png" alt="term-05-rodata-data-hexdump.png" loading="lazy"></a><figcaption>term-05-rodata-data-hexdump.png</figcaption></figure>
</div>

*Terminal evidence — `05-rodata-data-hexdump.txt` (arsip transkrip sesi solve).*

<div class="nx-evidence-grid">
<figure><a href="assets/medium-tea/term-06-solver-output.png" target="_blank" rel="noopener"><img src="assets/medium-tea/term-06-solver-output.png" alt="term-06-solver-output.png" loading="lazy"></a><figcaption>term-06-solver-output.png</figcaption></figure>
</div>

*Terminal evidence — `06-solver-output.txt` (arsip transkrip sesi solve).*

<div class="nx-evidence-grid">
<figure><a href="assets/medium-tea/term-07-verifikasi.png" target="_blank" rel="noopener"><img src="assets/medium-tea/term-07-verifikasi.png" alt="term-07-verifikasi.png" loading="lazy"></a><figcaption>term-07-verifikasi.png</figcaption></figure>
</div>

*Terminal evidence — `07-verifikasi.txt` (arsip transkrip sesi solve).*

<div class="nx-evidence-grid">
<figure><a href="assets/medium-tea/term-08-checksec.png" target="_blank" rel="noopener"><img src="assets/medium-tea/term-08-checksec.png" alt="term-08-checksec.png" loading="lazy"></a><figcaption>term-08-checksec.png</figcaption></figure>
</div>

*Terminal evidence — `08-checksec.txt` (arsip transkrip sesi solve).*

### Screenshot langkah

<div class="nx-evidence-grid">
<figure><a href="assets/medium-tea/01-solver.png" target="_blank" rel="noopener"><img src="assets/medium-tea/01-solver.png" alt="01-solver.png" loading="lazy"></a><figcaption>01-solver.png</figcaption></figure>
</div>

*Evidence — `01-solver.png`.*

<div class="nx-evidence-grid">
<figure><a href="assets/medium-tea/02-verifikasi.png" target="_blank" rel="noopener"><img src="assets/medium-tea/02-verifikasi.png" alt="02-verifikasi.png" loading="lazy"></a><figcaption>02-verifikasi.png</figcaption></figure>
</div>

*Evidence — `02-verifikasi.png`.*

### Transkrip mentah & script

- [`01-identitas.txt`](assets/medium-tea/01-identitas.txt)
- [`02-readelf.txt`](assets/medium-tea/02-readelf.txt)
- [`03-strings.txt`](assets/medium-tea/03-strings.txt)
- [`04-disasm.txt`](assets/medium-tea/04-disasm.txt)
- [`05-rodata-data-hexdump.txt`](assets/medium-tea/05-rodata-data-hexdump.txt)
- [`06-solver-output.txt`](assets/medium-tea/06-solver-output.txt)
- [`07-verifikasi.txt`](assets/medium-tea/07-verifikasi.txt)
- [`08-checksec.txt`](assets/medium-tea/08-checksec.txt)
- [`solve_tea.py`](assets/medium-tea/solve_tea.py)

## Tabel Evidence

| Bukti | File | Keterangan |
|---|---|---|
| Identitas & hash | `01-identitas.txt` | `file`, `stat`, hash |
| ELF metadata | `02-readelf.txt` | Header, segmen, section, dynamic |
| Strings | `03-strings.txt` | `strings -n 4` |
| Disassembly | `04-disasm.txt` | Seluruh `.text`, termasuk round function |
| Hex dump | `05-rodata-data-hexdump.txt` | `.rodata` berisi ciphertext |
| Solver | `solve_tea.py` | Script dekripsi TEA |
| Output solver | `06-solver-output.txt` | Output asli |
| Verifikasi | `07-verifikasi.txt` | Salah vs benar + hash |
| Checksec | `08-checksec.txt` | Hasil `ELF.checksec()` |
| Screenshot solver | `01-solver.png` | Render output solver |
| Screenshot verifikasi | `02-verifikasi.png` | Render output verifikasi |