# RSA Coppersmith cihuy — Evidence / Bukti

<div class="nx-challenge-head"><span class="nx-chip">4 screenshot</span><span class="nx-chip">4 transkrip / script</span></div>


[← Overview](21-rsa-coppersmith-cihuy.md) · [Index](index.md)

> **Langkah 6/7 — Bukti / Evidence.** Bukti / Evidence
>
> **Titik penting:** arsip screenshot dan transkrip
>
> **Berikutnya:** [Referensi](21-rsa-coppersmith-cihuy-07-referensi.md)


## Arsip Evidence

> Semua file berasal dari `assets/rsa-coppersmith-cihuy/`. Screenshot platform dan terminal adalah bukti asli dari sesi solve; transkrip mentah tetap ditautkan di bagian bawah.

### Platform

<div class="nx-evidence-grid">
<figure><a href="assets/rsa-coppersmith-cihuy/00-challenge-platform.png" target="_blank" rel="noopener"><img src="assets/rsa-coppersmith-cihuy/00-challenge-platform.png" alt="00-challenge-platform.png" loading="lazy"></a><figcaption>00-challenge-platform.png</figcaption></figure>
</div>

*Challenge brief asli di platform NFX CTF 2026.*

<div class="nx-evidence-grid">
<figure><a href="assets/rsa-coppersmith-cihuy/00b-terminal-evidence.png" target="_blank" rel="noopener"><img src="assets/rsa-coppersmith-cihuy/00b-terminal-evidence.png" alt="Terminal evidence (real)" loading="lazy"></a><figcaption>Terminal evidence (real)</figcaption></figure>
</div>

*Terminal evidence (real).*

### Terminal (arsip sesi)

<div class="nx-evidence-grid">
<figure><a href="assets/rsa-coppersmith-cihuy/term-solver-output.png" target="_blank" rel="noopener"><img src="assets/rsa-coppersmith-cihuy/term-solver-output.png" alt="term-solver-output.png" loading="lazy"></a><figcaption>term-solver-output.png</figcaption></figure>
</div>

*Terminal evidence — `solver-output.txt` (arsip transkrip sesi solve).*

<div class="nx-evidence-grid">
<figure><a href="assets/rsa-coppersmith-cihuy/term-verify-output.png" target="_blank" rel="noopener"><img src="assets/rsa-coppersmith-cihuy/term-verify-output.png" alt="term-verify-output.png" loading="lazy"></a><figcaption>term-verify-output.png</figcaption></figure>
</div>

*Terminal evidence — `verify-output.txt` (arsip transkrip sesi solve).*

### Transkrip mentah & script

- [`solve.py`](assets/rsa-coppersmith-cihuy/solve.py)
- [`solver-output.txt`](assets/rsa-coppersmith-cihuy/solver-output.txt)
- [`verify-output.txt`](assets/rsa-coppersmith-cihuy/verify-output.txt)
- [`verify.py`](assets/rsa-coppersmith-cihuy/verify.py)

## Validasi platform (real)

![Validasi platform — CORRECT, BUT ALREADY SOLVED.](assets/rsa-coppersmith-cihuy/00b-platform-validation.png)

*Screenshot asli dari platform NFX CTF 2026. Platform menjawab
`CORRECT, BUT ALREADY SOLVED.` untuk flag ini.*


## Tabel Evidence

| Bukti | File | Keterangan |
|---|---|---|
| Hash input | `assets/checksums-all.txt` | SHA-256 `chall.py` |
| Solver | `assets/rsa-coppersmith-cihuy/solve.py` | Coppersmith m=4 |
| Output solver | `assets/rsa-coppersmith-cihuy/solver-output.txt` | `p`, plaintext |
| Verifikasi | `assets/rsa-coppersmith-cihuy/verify.py` / `verify-output.txt` | `N % p == 0`, flag |
| Log submit | `work/wave2_submit_parallel.jsonl` | Flag diterima platform |