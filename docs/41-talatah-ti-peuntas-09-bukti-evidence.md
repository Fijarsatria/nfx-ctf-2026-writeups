# Talatah Ti Peuntas — Evidence / Bukti

<div class="nx-challenge-head"><span class="nx-chip">9 screenshot</span><span class="nx-chip">8 transkrip / script</span></div>


[← Overview](41-talatah-ti-peuntas.md) · [Index](index.md)

> **Langkah 9/10 — Bukti / Evidence.** Bukti / Evidence
>
> **Titik penting:** arsip screenshot dan transkrip
>
> **Berikutnya:** [Referensi](41-talatah-ti-peuntas-10-referensi.md)


## Arsip Evidence

> Semua file berasal dari `assets/talatah-ti-peuntas/`. Screenshot platform dan terminal adalah bukti asli dari sesi solve; transkrip mentah tetap ditautkan di bagian bawah.

### Platform

<div class="nx-evidence-grid">
<figure><a href="assets/talatah-ti-peuntas/00-challenge-platform.png" target="_blank" rel="noopener"><img src="assets/talatah-ti-peuntas/00-challenge-platform.png" alt="00-challenge-platform.png" loading="lazy"></a><figcaption>00-challenge-platform.png</figcaption></figure>
</div>

*Challenge brief asli di platform NFX CTF 2026.*

<div class="nx-evidence-grid">
<figure><a href="assets/talatah-ti-peuntas/00b-terminal-evidence.png" target="_blank" rel="noopener"><img src="assets/talatah-ti-peuntas/00b-terminal-evidence.png" alt="Terminal evidence (real)" loading="lazy"></a><figcaption>Terminal evidence (real)</figcaption></figure>
</div>

*Terminal evidence (real).*

### Terminal (arsip sesi)

<div class="nx-evidence-grid">
<figure><a href="assets/talatah-ti-peuntas/term-01-file-hash-checksec.png" target="_blank" rel="noopener"><img src="assets/talatah-ti-peuntas/term-01-file-hash-checksec.png" alt="term-01-file-hash-checksec.png" loading="lazy"></a><figcaption>term-01-file-hash-checksec.png</figcaption></figure>
</div>

*Terminal evidence — `01-file-hash-checksec.txt` (arsip transkrip sesi solve).*

<div class="nx-evidence-grid">
<figure><a href="assets/talatah-ti-peuntas/term-02-disasm.png" target="_blank" rel="noopener"><img src="assets/talatah-ti-peuntas/term-02-disasm.png" alt="term-02-disasm.png" loading="lazy"></a><figcaption>term-02-disasm.png</figcaption></figure>
</div>

*Terminal evidence — `02-disasm.txt` (arsip transkrip sesi solve).*

<div class="nx-evidence-grid">
<figure><a href="assets/talatah-ti-peuntas/term-02b-record-layout.png" target="_blank" rel="noopener"><img src="assets/talatah-ti-peuntas/term-02b-record-layout.png" alt="term-02b-record-layout.png" loading="lazy"></a><figcaption>term-02b-record-layout.png</figcaption></figure>
</div>

*Terminal evidence — `02b-record-layout.txt` (arsip transkrip sesi solve).*

<div class="nx-evidence-grid">
<figure><a href="assets/talatah-ti-peuntas/term-02c-got.png" target="_blank" rel="noopener"><img src="assets/talatah-ti-peuntas/term-02c-got.png" alt="term-02c-got.png" loading="lazy"></a><figcaption>term-02c-got.png</figcaption></figure>
</div>

*Terminal evidence — `02c-got.txt` (arsip transkrip sesi solve).*

<div class="nx-evidence-grid">
<figure><a href="assets/talatah-ti-peuntas/term-03-exploit-run.png" target="_blank" rel="noopener"><img src="assets/talatah-ti-peuntas/term-03-exploit-run.png" alt="term-03-exploit-run.png" loading="lazy"></a><figcaption>term-03-exploit-run.png</figcaption></figure>
</div>

*Terminal evidence — `03-exploit-run.txt` (arsip transkrip sesi solve).*

<div class="nx-evidence-grid">
<figure><a href="assets/talatah-ti-peuntas/term-04-flag-status.png" target="_blank" rel="noopener"><img src="assets/talatah-ti-peuntas/term-04-flag-status.png" alt="term-04-flag-status.png" loading="lazy"></a><figcaption>term-04-flag-status.png</figcaption></figure>
</div>

*Terminal evidence — `04-flag-status.txt` (arsip transkrip sesi solve).*

<div class="nx-evidence-grid">
<figure><a href="assets/talatah-ti-peuntas/term-flag.png" target="_blank" rel="noopener"><img src="assets/talatah-ti-peuntas/term-flag.png" alt="term-flag.png" loading="lazy"></a><figcaption>term-flag.png</figcaption></figure>
</div>

*Terminal evidence — `flag.txt` (arsip transkrip sesi solve).*

### Transkrip mentah & script

- [`01-file-hash-checksec.txt`](assets/talatah-ti-peuntas/01-file-hash-checksec.txt)
- [`02-disasm.txt`](assets/talatah-ti-peuntas/02-disasm.txt)
- [`02b-record-layout.txt`](assets/talatah-ti-peuntas/02b-record-layout.txt)
- [`02c-got.txt`](assets/talatah-ti-peuntas/02c-got.txt)
- [`03-exploit-run.txt`](assets/talatah-ti-peuntas/03-exploit-run.txt)
- [`04-flag-status.txt`](assets/talatah-ti-peuntas/04-flag-status.txt)
- [`exploit.py`](assets/talatah-ti-peuntas/exploit.py)
- [`flag.txt`](assets/talatah-ti-peuntas/flag.txt)

## Validasi platform (real)

![Validasi platform — CORRECT, BUT ALREADY SOLVED.](assets/talatah-ti-peuntas/00b-platform-validation.png)

*Screenshot asli dari platform NFX CTF 2026. Platform menjawab
`CORRECT, BUT ALREADY SOLVED.` untuk flag ini.*


## Tabel Evidence

| Bukti | File | Keterangan |
|---|---|---|
| Identitas/hash/checksec | `docs/assets/talatah-ti-peuntas/01-file-hash-checksec.txt` | non-PIE, partial RELRO |
| Disassembly | `docs/assets/talatah-ti-peuntas/02-disasm.txt` | `op_parse`, `op_view`, `op_edit`, `op_delete` |
| Layout node/chunk | `docs/assets/talatah-ti-peuntas/02b-record-layout.txt` | Offset overflow |
| GOT | `docs/assets/talatah-ti-peuntas/02c-got.txt` | `free@got`, `printf@got` |
| Exploit | `docs/assets/talatah-ti-peuntas/exploit.py` | Full chain |
| Output | `docs/assets/talatah-ti-peuntas/03-exploit-run.txt` | Leak + shell + flag lokal |
| Flag/status | `docs/assets/talatah-ti-peuntas/04-flag-status.txt` | Flag dari `flags/pwn/` |