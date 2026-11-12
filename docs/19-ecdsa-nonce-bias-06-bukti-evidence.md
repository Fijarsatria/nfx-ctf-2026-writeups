# ECDSA Nonce Bias — Evidence / Bukti

<div class="nx-challenge-head"><span class="nx-chip">4 screenshot</span><span class="nx-chip">4 transkrip / script</span></div>


[← Overview](19-ecdsa-nonce-bias.md) · [Index](index.md)

> **Langkah 6/7 — Bukti / Evidence.** Bukti / Evidence
>
> **Titik penting:** arsip screenshot dan transkrip
>
> **Berikutnya:** [Referensi](19-ecdsa-nonce-bias-07-referensi.md)


## Arsip Evidence

> Semua file berasal dari `assets/ecdsa-nonce-bias/`. Screenshot platform dan terminal adalah bukti asli dari sesi solve; transkrip mentah tetap ditautkan di bagian bawah.

### Platform

<div class="nx-evidence-grid">
<figure><a href="assets/ecdsa-nonce-bias/00-challenge-platform.png" target="_blank" rel="noopener"><img src="assets/ecdsa-nonce-bias/00-challenge-platform.png" alt="00-challenge-platform.png" loading="lazy"></a><figcaption>00-challenge-platform.png</figcaption></figure>
</div>

*Challenge brief asli di platform NFX CTF 2026.*

<div class="nx-evidence-grid">
<figure><a href="assets/ecdsa-nonce-bias/00b-terminal-evidence.png" target="_blank" rel="noopener"><img src="assets/ecdsa-nonce-bias/00b-terminal-evidence.png" alt="Terminal evidence (real)" loading="lazy"></a><figcaption>Terminal evidence (real)</figcaption></figure>
</div>

*Terminal evidence (real).*

### Terminal (arsip sesi)

<div class="nx-evidence-grid">
<figure><a href="assets/ecdsa-nonce-bias/term-solver-output.png" target="_blank" rel="noopener"><img src="assets/ecdsa-nonce-bias/term-solver-output.png" alt="term-solver-output.png" loading="lazy"></a><figcaption>term-solver-output.png</figcaption></figure>
</div>

*Terminal evidence — `solver-output.txt` (arsip transkrip sesi solve).*

<div class="nx-evidence-grid">
<figure><a href="assets/ecdsa-nonce-bias/term-verify-output.png" target="_blank" rel="noopener"><img src="assets/ecdsa-nonce-bias/term-verify-output.png" alt="term-verify-output.png" loading="lazy"></a><figcaption>term-verify-output.png</figcaption></figure>
</div>

*Terminal evidence — `verify-output.txt` (arsip transkrip sesi solve).*

### Transkrip mentah & script

- [`solve.py`](assets/ecdsa-nonce-bias/solve.py)
- [`solver-output.txt`](assets/ecdsa-nonce-bias/solver-output.txt)
- [`verify-output.txt`](assets/ecdsa-nonce-bias/verify-output.txt)
- [`verify.py`](assets/ecdsa-nonce-bias/verify.py)

## Tabel Evidence

| Bukti | File | Keterangan |
|---|---|---|
| Hash input | `assets/checksums-all.txt` | SHA-256 ketiga file |
| Solver | `assets/ecdsa-nonce-bias/solve.py` | HNP lattice m=50 |
| Output solver | `assets/ecdsa-nonce-bias/solver-output.txt` | `d`, flag |
| Verifikasi | `assets/ecdsa-nonce-bias/verify.py` / `verify-output.txt` | `d·G`, 200 nonce, tag |
| Log submit | `work/wave2_submit_parallel.jsonl` | Flag diterima platform |