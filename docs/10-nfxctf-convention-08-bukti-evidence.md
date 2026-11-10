# NFXCTF Convention — Evidence / Bukti

<div class="nx-challenge-head"><span class="nx-chip">9 screenshot</span><span class="nx-chip">9 transkrip / script</span></div>


[← Overview](10-nfxctf-convention.md) · [Index](index.md)

> **Langkah 8/9 — Bukti / Evidence.** Semua file ada di writeups/assets/nfxctf-convention/:
>
> **Titik penting:** arsip screenshot dan transkrip
>
> **Berikutnya:** [Referensi](10-nfxctf-convention-09-referensi.md)


## Arsip Evidence

> Semua file berasal dari `assets/nfxctf-convention/`. Screenshot platform dan terminal adalah bukti asli dari sesi solve; transkrip mentah tetap ditautkan di bagian bawah.

### Platform

<div class="nx-evidence-grid">
<figure><a href="assets/nfxctf-convention/00-challenge-platform.png" target="_blank" rel="noopener"><img src="assets/nfxctf-convention/00-challenge-platform.png" alt="00-challenge-platform.png" loading="lazy"></a><figcaption>00-challenge-platform.png</figcaption></figure>
</div>

*Challenge brief asli di platform NFX CTF 2026.*

<div class="nx-evidence-grid">
<figure><a href="assets/nfxctf-convention/00b-submit-platform.png" target="_blank" rel="noopener"><img src="assets/nfxctf-convention/00b-submit-platform.png" alt="00b-submit-platform.png" loading="lazy"></a><figcaption>00b-submit-platform.png</figcaption></figure>
</div>

*Submit flag di platform: `CORRECT, BUT ALREADY SOLVED.`*

### Terminal (arsip sesi)

<div class="nx-evidence-grid">
<figure><a href="assets/nfxctf-convention/term-01-file-hash-checksec.png" target="_blank" rel="noopener"><img src="assets/nfxctf-convention/term-01-file-hash-checksec.png" alt="term-01-file-hash-checksec.png" loading="lazy"></a><figcaption>term-01-file-hash-checksec.png</figcaption></figure>
</div>

*Terminal evidence — `01-file-hash-checksec.txt` (arsip transkrip sesi solve).*

<div class="nx-evidence-grid">
<figure><a href="assets/nfxctf-convention/term-02-disasm.png" target="_blank" rel="noopener"><img src="assets/nfxctf-convention/term-02-disasm.png" alt="term-02-disasm.png" loading="lazy"></a><figcaption>term-02-disasm.png</figcaption></figure>
</div>

*Terminal evidence — `02-disasm.txt` (arsip transkrip sesi solve).*

<div class="nx-evidence-grid">
<figure><a href="assets/nfxctf-convention/term-02b-layout.png" target="_blank" rel="noopener"><img src="assets/nfxctf-convention/term-02b-layout.png" alt="term-02b-layout.png" loading="lazy"></a><figcaption>term-02b-layout.png</figcaption></figure>
</div>

*Terminal evidence — `02b-layout.txt` (arsip transkrip sesi solve).*

<div class="nx-evidence-grid">
<figure><a href="assets/nfxctf-convention/term-03-exploit-run.png" target="_blank" rel="noopener"><img src="assets/nfxctf-convention/term-03-exploit-run.png" alt="term-03-exploit-run.png" loading="lazy"></a><figcaption>term-03-exploit-run.png</figcaption></figure>
</div>

*Terminal evidence — `03-exploit-run.txt` (arsip transkrip sesi solve).*

<div class="nx-evidence-grid">
<figure><a href="assets/nfxctf-convention/term-03b-leak-probe.png" target="_blank" rel="noopener"><img src="assets/nfxctf-convention/term-03b-leak-probe.png" alt="term-03b-leak-probe.png" loading="lazy"></a><figcaption>term-03b-leak-probe.png</figcaption></figure>
</div>

*Terminal evidence — `03b-leak-probe.txt` (arsip transkrip sesi solve).*

<div class="nx-evidence-grid">
<figure><a href="assets/nfxctf-convention/term-04-flag-status.png" target="_blank" rel="noopener"><img src="assets/nfxctf-convention/term-04-flag-status.png" alt="term-04-flag-status.png" loading="lazy"></a><figcaption>term-04-flag-status.png</figcaption></figure>
</div>

*Terminal evidence — `04-flag-status.txt` (arsip transkrip sesi solve).*

<div class="nx-evidence-grid">
<figure><a href="assets/nfxctf-convention/term-flag.png" target="_blank" rel="noopener"><img src="assets/nfxctf-convention/term-flag.png" alt="term-flag.png" loading="lazy"></a><figcaption>term-flag.png</figcaption></figure>
</div>

*Terminal evidence — `flag.txt` (arsip transkrip sesi solve).*

### Transkrip mentah & script

- [`01-file-hash-checksec.txt`](assets/nfxctf-convention/01-file-hash-checksec.txt)
- [`02-disasm.txt`](assets/nfxctf-convention/02-disasm.txt)
- [`02b-layout.txt`](assets/nfxctf-convention/02b-layout.txt)
- [`03-exploit-run.txt`](assets/nfxctf-convention/03-exploit-run.txt)
- [`03b-leak-probe.py`](assets/nfxctf-convention/03b-leak-probe.py)
- [`03b-leak-probe.txt`](assets/nfxctf-convention/03b-leak-probe.txt)
- [`04-flag-status.txt`](assets/nfxctf-convention/04-flag-status.txt)
- [`exploit.py`](assets/nfxctf-convention/exploit.py)
- [`flag.txt`](assets/nfxctf-convention/flag.txt)

## Tabel Evidence

Semua file ada di `writeups/assets/nfxctf-convention/`:

| Bukti | File | Keterangan |
|---|---|---|
| Identitas, hash, checksec | `01-file-hash-checksec.txt` | `file`, `sha256sum`, `ELF.checksec()` |
| Disassembly | `02-disasm.txt` | `register_user`, `edit_name`, `view_profile`, `leave_feedback`, `main` |
| Layout data | `02b-layout.txt` | `player`, `log_buf`, offset field |
| Leak probe | `03b-leak-probe.py`, `03b-leak-probe.txt` | `%7$p` canary, `%17$p` libc |
| Exploit | `exploit.py` | Script pwntools lengkap |
| Output exploit | `03-exploit-run.txt` | Output asli (canary/libc/flag lokal) |
| Flag & status | `04-flag-status.txt` | Flag dari `flags/pwn/`, sha256, status VERIFIED |
| Fixture lokal | `flag.txt` | `NFX{LOCAL_TEST_FLAG_CONVENTION}` (bukan flag kompetisi) |