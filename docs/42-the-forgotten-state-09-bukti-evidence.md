# THE FORGOTTEN STATE — Evidence / Bukti

<div class="nx-challenge-head"><span class="nx-chip">9 screenshot</span><span class="nx-chip">8 transkrip / script</span></div>


[← Overview](42-the-forgotten-state.md) · [Index](index.md)

> **Langkah 9/10 — Bukti / Evidence.** Bukti / Evidence
>
> **Titik penting:** arsip screenshot dan transkrip
>
> **Berikutnya:** [Referensi](42-the-forgotten-state-10-referensi.md)


## Arsip Evidence

> Semua file berasal dari `assets/the-forgotten-state/`. Screenshot platform dan terminal adalah bukti asli dari sesi solve; transkrip mentah tetap ditautkan di bagian bawah.

### Platform

<div class="nx-evidence-grid">
<figure><a href="assets/the-forgotten-state/00-challenge-platform.png" target="_blank" rel="noopener"><img src="assets/the-forgotten-state/00-challenge-platform.png" alt="00-challenge-platform.png" loading="lazy"></a><figcaption>00-challenge-platform.png</figcaption></figure>
</div>

*Challenge brief asli di platform NFX CTF 2026.*

<div class="nx-evidence-grid">
<figure><a href="assets/the-forgotten-state/00b-terminal-evidence.png" target="_blank" rel="noopener"><img src="assets/the-forgotten-state/00b-terminal-evidence.png" alt="Terminal evidence (real)" loading="lazy"></a><figcaption>Terminal evidence (real)</figcaption></figure>
</div>

*Terminal evidence (real).*

### Terminal (arsip sesi)

<div class="nx-evidence-grid">
<figure><a href="assets/the-forgotten-state/term-01-file-hash-checksec.png" target="_blank" rel="noopener"><img src="assets/the-forgotten-state/term-01-file-hash-checksec.png" alt="term-01-file-hash-checksec.png" loading="lazy"></a><figcaption>term-01-file-hash-checksec.png</figcaption></figure>
</div>

*Terminal evidence — `01-file-hash-checksec.txt` (arsip transkrip sesi solve).*

<div class="nx-evidence-grid">
<figure><a href="assets/the-forgotten-state/term-02-disasm.png" target="_blank" rel="noopener"><img src="assets/the-forgotten-state/term-02-disasm.png" alt="term-02-disasm.png" loading="lazy"></a><figcaption>term-02-disasm.png</figcaption></figure>
</div>

*Terminal evidence — `02-disasm.txt` (arsip transkrip sesi solve).*

<div class="nx-evidence-grid">
<figure><a href="assets/the-forgotten-state/term-02b-record-layout.png" target="_blank" rel="noopener"><img src="assets/the-forgotten-state/term-02b-record-layout.png" alt="term-02b-record-layout.png" loading="lazy"></a><figcaption>term-02b-record-layout.png</figcaption></figure>
</div>

*Terminal evidence — `02b-record-layout.txt` (arsip transkrip sesi solve).*

<div class="nx-evidence-grid">
<figure><a href="assets/the-forgotten-state/term-02c-got.png" target="_blank" rel="noopener"><img src="assets/the-forgotten-state/term-02c-got.png" alt="term-02c-got.png" loading="lazy"></a><figcaption>term-02c-got.png</figcaption></figure>
</div>

*Terminal evidence — `02c-got.txt` (arsip transkrip sesi solve).*

<div class="nx-evidence-grid">
<figure><a href="assets/the-forgotten-state/term-03-exploit-run.png" target="_blank" rel="noopener"><img src="assets/the-forgotten-state/term-03-exploit-run.png" alt="term-03-exploit-run.png" loading="lazy"></a><figcaption>term-03-exploit-run.png</figcaption></figure>
</div>

*Terminal evidence — `03-exploit-run.txt` (arsip transkrip sesi solve).*

<div class="nx-evidence-grid">
<figure><a href="assets/the-forgotten-state/term-04-flag-status.png" target="_blank" rel="noopener"><img src="assets/the-forgotten-state/term-04-flag-status.png" alt="term-04-flag-status.png" loading="lazy"></a><figcaption>term-04-flag-status.png</figcaption></figure>
</div>

*Terminal evidence — `04-flag-status.txt` (arsip transkrip sesi solve).*

<div class="nx-evidence-grid">
<figure><a href="assets/the-forgotten-state/term-flag.png" target="_blank" rel="noopener"><img src="assets/the-forgotten-state/term-flag.png" alt="term-flag.png" loading="lazy"></a><figcaption>term-flag.png</figcaption></figure>
</div>

*Terminal evidence — `flag.txt` (arsip transkrip sesi solve).*

### Transkrip mentah & script

- [`01-file-hash-checksec.txt`](assets/the-forgotten-state/01-file-hash-checksec.txt)
- [`02-disasm.txt`](assets/the-forgotten-state/02-disasm.txt)
- [`02b-record-layout.txt`](assets/the-forgotten-state/02b-record-layout.txt)
- [`02c-got.txt`](assets/the-forgotten-state/02c-got.txt)
- [`03-exploit-run.txt`](assets/the-forgotten-state/03-exploit-run.txt)
- [`04-flag-status.txt`](assets/the-forgotten-state/04-flag-status.txt)
- [`exploit.py`](assets/the-forgotten-state/exploit.py)
- [`flag.txt`](assets/the-forgotten-state/flag.txt)

## Validasi platform (real)

![Validasi platform — CORRECT, BUT ALREADY SOLVED.](assets/the-forgotten-state/00b-platform-validation.png)

*Screenshot asli dari platform NFX CTF 2026. Platform menjawab
`CORRECT, BUT ALREADY SOLVED.` untuk flag ini.*


## Tabel Evidence

| Bukti | File | Keterangan |
|---|---|---|
| Identitas/hash/checksec | `writeups/assets/the-forgotten-state/01-file-hash-checksec.txt` | non-PIE, partial RELRO |
| Disassembly | `writeups/assets/the-forgotten-state/02-disasm.txt` | `op_create`, `op_release`, `op_view`, `op_edit`, `op_list` |
| Layout record/global | `writeups/assets/the-forgotten-state/02b-record-layout.txt` | `table`, `active`, field record |
| GOT | `writeups/assets/the-forgotten-state/02c-got.txt` | `free@got` |
| Exploit | `writeups/assets/the-forgotten-state/exploit.py` | Overflow + GOT hijack |
| Output | `writeups/assets/the-forgotten-state/03-exploit-run.txt` | Leak + shell + flag lokal |
| Flag/status | `writeups/assets/the-forgotten-state/04-flag-status.txt` | Flag dari `flags/pwn/` |