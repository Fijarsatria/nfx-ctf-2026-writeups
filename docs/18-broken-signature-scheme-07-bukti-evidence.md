# Broken Signature Scheme — Evidence / Bukti

<div class="nx-challenge-head"><span class="nx-chip">4 screenshot</span><span class="nx-chip">4 transkrip / script</span></div>


[← Overview](18-broken-signature-scheme.md) · [Index](index.md)


## Arsip Evidence

> Semua file berasal dari `assets/broken-signature-scheme/`. Screenshot platform dan terminal adalah bukti asli dari sesi solve; transkrip mentah tetap ditautkan di bagian bawah.

### Platform

<div class="nx-evidence-grid">
<figure><a href="assets/broken-signature-scheme/00-challenge-platform.png" target="_blank" rel="noopener"><img src="assets/broken-signature-scheme/00-challenge-platform.png" alt="00-challenge-platform.png" loading="lazy"></a><figcaption>00-challenge-platform.png</figcaption></figure>
</div>

*Challenge brief asli di platform NFX CTF 2026.*

<div class="nx-evidence-grid">
<figure><a href="assets/broken-signature-scheme/00b-submit-platform.png" target="_blank" rel="noopener"><img src="assets/broken-signature-scheme/00b-submit-platform.png" alt="00b-submit-platform.png" loading="lazy"></a><figcaption>00b-submit-platform.png</figcaption></figure>
</div>

*Submit flag di platform: `CORRECT, BUT ALREADY SOLVED.`*

### Terminal (arsip sesi)

<div class="nx-evidence-grid">
<figure><a href="assets/broken-signature-scheme/term-solver-output.png" target="_blank" rel="noopener"><img src="assets/broken-signature-scheme/term-solver-output.png" alt="term-solver-output.png" loading="lazy"></a><figcaption>term-solver-output.png</figcaption></figure>
</div>

*Terminal evidence — `solver-output.txt` (arsip transkrip sesi solve).*

<div class="nx-evidence-grid">
<figure><a href="assets/broken-signature-scheme/term-verify-output.png" target="_blank" rel="noopener"><img src="assets/broken-signature-scheme/term-verify-output.png" alt="term-verify-output.png" loading="lazy"></a><figcaption>term-verify-output.png</figcaption></figure>
</div>

*Terminal evidence — `verify-output.txt` (arsip transkrip sesi solve).*

### Transkrip mentah & script

- [`solve.py`](assets/broken-signature-scheme/solve.py)
- [`solver-output.txt`](assets/broken-signature-scheme/solver-output.txt)
- [`verify-output.txt`](assets/broken-signature-scheme/verify-output.txt)
- [`verify.py`](assets/broken-signature-scheme/verify.py)

## Tabel Evidence

| Bukti | File | Keterangan |
|---|---|---|
| Hash input | `assets/checksums-all.txt` | SHA-256 `challenge.py`, `output.txt` |
| Solver | `assets/broken-signature-scheme/solve.py` | Faktorisasi + AES-GCM |
| Output solver | `assets/broken-signature-scheme/solver-output.txt` | `p`, `q`, flag |
| Verifikasi 3 layer | `assets/broken-signature-scheme/verify.py` / `verify-output.txt` | L1/L2/L3 |
| Log submit | `work/wave2_submit_parallel.jsonl` | Flag diterima platform |