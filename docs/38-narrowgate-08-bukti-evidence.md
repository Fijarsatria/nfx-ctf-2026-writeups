# NarrowGate — Evidence / Bukti

<div class="nx-challenge-head"><span class="nx-chip">11 screenshot</span><span class="nx-chip">11 transkrip / script</span></div>


[← Overview](38-narrowgate.md) · [Index](index.md)

> **Langkah 8/9 — Bukti / Evidence.** Bukti / Evidence
>
> **Titik penting:** arsip screenshot dan transkrip
>
> **Berikutnya:** [Referensi](38-narrowgate-09-referensi.md)


## Arsip Evidence

> Semua file berasal dari `assets/narrowgate/`. Screenshot platform dan terminal adalah bukti asli dari sesi solve; transkrip mentah tetap ditautkan di bagian bawah.

### Platform

<div class="nx-evidence-grid">
<figure><a href="assets/narrowgate/00-challenge-platform.png" target="_blank" rel="noopener"><img src="assets/narrowgate/00-challenge-platform.png" alt="00-challenge-platform.png" loading="lazy"></a><figcaption>00-challenge-platform.png</figcaption></figure>
</div>

*Challenge brief asli di platform NFX CTF 2026.*

<div class="nx-evidence-grid">
<figure><a href="assets/narrowgate/00b-terminal-evidence.png" target="_blank" rel="noopener"><img src="assets/narrowgate/00b-terminal-evidence.png" alt="Terminal evidence (real)" loading="lazy"></a><figcaption>Terminal evidence (real)</figcaption></figure>
</div>

*Terminal evidence (real).*

### Terminal (arsip sesi)

<div class="nx-evidence-grid">
<figure><a href="assets/narrowgate/term-01-file-hash-checksec.png" target="_blank" rel="noopener"><img src="assets/narrowgate/term-01-file-hash-checksec.png" alt="term-01-file-hash-checksec.png" loading="lazy"></a><figcaption>term-01-file-hash-checksec.png</figcaption></figure>
</div>

*Terminal evidence — `01-file-hash-checksec.txt` (arsip transkrip sesi solve).*

<div class="nx-evidence-grid">
<figure><a href="assets/narrowgate/term-02-disasm.png" target="_blank" rel="noopener"><img src="assets/narrowgate/term-02-disasm.png" alt="term-02-disasm.png" loading="lazy"></a><figcaption>term-02-disasm.png</figcaption></figure>
</div>

*Terminal evidence — `02-disasm.txt` (arsip transkrip sesi solve).*

<div class="nx-evidence-grid">
<figure><a href="assets/narrowgate/term-02b-seccomp.png" target="_blank" rel="noopener"><img src="assets/narrowgate/term-02b-seccomp.png" alt="term-02b-seccomp.png" loading="lazy"></a><figcaption>term-02b-seccomp.png</figcaption></figure>
</div>

*Terminal evidence — `02b-seccomp.txt` (arsip transkrip sesi solve).*

<div class="nx-evidence-grid">
<figure><a href="assets/narrowgate/term-03-exploit-run.png" target="_blank" rel="noopener"><img src="assets/narrowgate/term-03-exploit-run.png" alt="term-03-exploit-run.png" loading="lazy"></a><figcaption>term-03-exploit-run.png</figcaption></figure>
</div>

*Terminal evidence — `03-exploit-run.txt` (arsip transkrip sesi solve).*

<div class="nx-evidence-grid">
<figure><a href="assets/narrowgate/term-03b-leak-probe.png" target="_blank" rel="noopener"><img src="assets/narrowgate/term-03b-leak-probe.png" alt="term-03b-leak-probe.png" loading="lazy"></a><figcaption>term-03b-leak-probe.png</figcaption></figure>
</div>

*Terminal evidence — `03b-leak-probe.txt` (arsip transkrip sesi solve).*

<div class="nx-evidence-grid">
<figure><a href="assets/narrowgate/term-03c-maps-rw-path.png" target="_blank" rel="noopener"><img src="assets/narrowgate/term-03c-maps-rw-path.png" alt="term-03c-maps-rw-path.png" loading="lazy"></a><figcaption>term-03c-maps-rw-path.png</figcaption></figure>
</div>

*Terminal evidence — `03c-maps-rw-path.txt` (arsip transkrip sesi solve).*

<div class="nx-evidence-grid">
<figure><a href="assets/narrowgate/term-03c-run-printable.png" target="_blank" rel="noopener"><img src="assets/narrowgate/term-03c-run-printable.png" alt="term-03c-run-printable.png" loading="lazy"></a><figcaption>term-03c-run-printable.png</figcaption></figure>
</div>

*Terminal evidence — `03c-run-printable.txt` (arsip transkrip sesi solve).*

<div class="nx-evidence-grid">
<figure><a href="assets/narrowgate/term-04-flag-status.png" target="_blank" rel="noopener"><img src="assets/narrowgate/term-04-flag-status.png" alt="term-04-flag-status.png" loading="lazy"></a><figcaption>term-04-flag-status.png</figcaption></figure>
</div>

*Terminal evidence — `04-flag-status.txt` (arsip transkrip sesi solve).*

<div class="nx-evidence-grid">
<figure><a href="assets/narrowgate/term-flag.png" target="_blank" rel="noopener"><img src="assets/narrowgate/term-flag.png" alt="term-flag.png" loading="lazy"></a><figcaption>term-flag.png</figcaption></figure>
</div>

*Terminal evidence — `flag.txt` (arsip transkrip sesi solve).*

### Transkrip mentah & script

- [`01-file-hash-checksec.txt`](assets/narrowgate/01-file-hash-checksec.txt)
- [`02-disasm.txt`](assets/narrowgate/02-disasm.txt)
- [`02b-seccomp.txt`](assets/narrowgate/02b-seccomp.txt)
- [`03-exploit-run.txt`](assets/narrowgate/03-exploit-run.txt)
- [`03b-leak-probe.py`](assets/narrowgate/03b-leak-probe.py)
- [`03b-leak-probe.txt`](assets/narrowgate/03b-leak-probe.txt)
- [`03c-maps-rw-path.txt`](assets/narrowgate/03c-maps-rw-path.txt)
- [`03c-run-printable.txt`](assets/narrowgate/03c-run-printable.txt)
- [`04-flag-status.txt`](assets/narrowgate/04-flag-status.txt)
- [`exploit.py`](assets/narrowgate/exploit.py)
- [`flag.txt`](assets/narrowgate/flag.txt)

## Tabel Evidence

| Bukti | File | Keterangan |
|---|---|---|
| Identitas/hash/checksec | `writeups/assets/narrowgate/01-file-hash-checksec.txt` | PIE, canary, Full RELRO |
| Disassembly | `writeups/assets/narrowgate/02-disasm.txt` | `leaker`, `main`, `setup_seccomp` |
| Seccomp decode | `writeups/assets/narrowgate/02b-seccomp.txt` | Allow-list BPF |
| Leak probe | `writeups/assets/narrowgate/03b-leak-probe.txt` | `%27`, `%29`, `%43` |
| Exploit | `writeups/assets/narrowgate/exploit.py` | ORW ROP |
| Output | `writeups/assets/narrowgate/03-exploit-run.txt`, `03c-run-printable.txt` | Flag lokal + padding |
| Flag/status | `writeups/assets/narrowgate/04-flag-status.txt` | Flag dari `flags/pwn/` |