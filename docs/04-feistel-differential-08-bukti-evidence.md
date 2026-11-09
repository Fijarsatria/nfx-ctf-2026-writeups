# Feistel Differential — Evidence / Bukti

<div class="nx-challenge-head"><span class="nx-chip">3 screenshot</span><span class="nx-chip">3 transkrip / script</span></div>


[← Overview](04-feistel-differential.md) · [Index](index.md)


## Arsip Evidence

> Semua file berasal dari `assets/feistel-differential/`. Screenshot platform dan terminal adalah bukti asli dari sesi solve; transkrip mentah tetap ditautkan di bagian bawah.

### Platform

<div class="nx-evidence-grid">
<figure><a href="assets/feistel-differential/00-challenge-platform.png" target="_blank" rel="noopener"><img src="assets/feistel-differential/00-challenge-platform.png" alt="00-challenge-platform.png" loading="lazy"></a><figcaption>00-challenge-platform.png</figcaption></figure>
</div>

*Challenge brief asli di platform NFX CTF 2026.*

<div class="nx-evidence-grid">
<figure><a href="assets/feistel-differential/00b-submit-platform.png" target="_blank" rel="noopener"><img src="assets/feistel-differential/00b-submit-platform.png" alt="00b-submit-platform.png" loading="lazy"></a><figcaption>00b-submit-platform.png</figcaption></figure>
</div>

*Submit flag di platform: `CORRECT, BUT ALREADY SOLVED.`*

### Terminal (arsip sesi)

<div class="nx-evidence-grid">
<figure><a href="assets/feistel-differential/term-solver-output.png" target="_blank" rel="noopener"><img src="assets/feistel-differential/term-solver-output.png" alt="term-solver-output.png" loading="lazy"></a><figcaption>term-solver-output.png</figcaption></figure>
</div>

*Terminal evidence — `solver-output.txt` (arsip transkrip sesi solve).*

### Transkrip mentah & script

- [`solve.py`](assets/feistel-differential/solve.py)
- [`solve_original_firstmodel.py`](assets/feistel-differential/solve_original_firstmodel.py)
- [`solver-output.txt`](assets/feistel-differential/solver-output.txt)

## Tabel Evidence

| Bukti | File | Keterangan |
|---|---|---|
| Hash input | `assets/checksums-all.txt` | SHA-256 ketiga file |
| Solver | `assets/feistel-differential/solve.py` | z3 + verifikasi penuh |
| Output solver | `assets/feistel-differential/solver-output.txt` | Key, 280000/280000, flag |
| Log submit | `work/verify_extra.jsonl` | Flag diterima platform |