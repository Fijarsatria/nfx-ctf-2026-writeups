# Cihuyyyyyyyyyyyyyyy LWE sikit ahhhh — Evidence / Bukti

<div class="nx-challenge-head"><span class="nx-chip">3 screenshot</span><span class="nx-chip">2 transkrip / script</span></div>


[← Overview](03-cihuyyyyyyyyyyyyyyy-lwe-sikit-ahhhh.md) · [Index](index.md)

> **Langkah 6/7 — Bukti / Evidence.** Bukti / Evidence
>
> **Titik penting:** arsip screenshot dan transkrip
>
> **Berikutnya:** [Referensi](03-cihuyyyyyyyyyyyyyyy-lwe-sikit-ahhhh-07-referensi.md)


## Arsip Evidence

> Semua file berasal dari `assets/cihuyyyyyyyyyyyyyyy-lwe-sikit-ahhhh/`. Screenshot platform dan terminal adalah bukti asli dari sesi solve; transkrip mentah tetap ditautkan di bagian bawah.

### Platform

<div class="nx-evidence-grid">
<figure><a href="assets/cihuyyyyyyyyyyyyyyy-lwe-sikit-ahhhh/00-challenge-platform.png" target="_blank" rel="noopener"><img src="assets/cihuyyyyyyyyyyyyyyy-lwe-sikit-ahhhh/00-challenge-platform.png" alt="00-challenge-platform.png" loading="lazy"></a><figcaption>00-challenge-platform.png</figcaption></figure>
</div>

*Challenge brief asli di platform NFX CTF 2026.*

<div class="nx-evidence-grid">
<figure><a href="assets/cihuyyyyyyyyyyyyyyy-lwe-sikit-ahhhh/00b-terminal-evidence.png" target="_blank" rel="noopener"><img src="assets/cihuyyyyyyyyyyyyyyy-lwe-sikit-ahhhh/00b-terminal-evidence.png" alt="Terminal evidence (real)" loading="lazy"></a><figcaption>Terminal evidence (real)</figcaption></figure>
</div>

*Terminal evidence (real).*

### Terminal (arsip sesi)

<div class="nx-evidence-grid">
<figure><a href="assets/cihuyyyyyyyyyyyyyyy-lwe-sikit-ahhhh/term-solver-output.png" target="_blank" rel="noopener"><img src="assets/cihuyyyyyyyyyyyyyyy-lwe-sikit-ahhhh/term-solver-output.png" alt="term-solver-output.png" loading="lazy"></a><figcaption>term-solver-output.png</figcaption></figure>
</div>

*Terminal evidence — `solver-output.txt` (arsip transkrip sesi solve).*

### Transkrip mentah & script

- [`solve_lwe.py`](assets/cihuyyyyyyyyyyyyyyy-lwe-sikit-ahhhh/solve_lwe.py)
- [`solver-output.txt`](assets/cihuyyyyyyyyyyyyyyy-lwe-sikit-ahhhh/solver-output.txt)

## Validasi platform (real)

![Validasi platform — CORRECT, BUT ALREADY SOLVED.](assets/cihuyyyyyyyyyyyyyyy-lwe-sikit-ahhhh/00b-platform-validation.png)

*Screenshot asli dari platform NFX CTF 2026. Platform menjawab
`CORRECT, BUT ALREADY SOLVED.` untuk flag ini.*


## Tabel Evidence

| Bukti | File | Keterangan |
|---|---|---|
| Hash input | `assets/checksums-all.txt` | SHA-256 `lwe.py` |
| Solver | `assets/cihuyyyyyyyyyyyyyyy-lwe-sikit-ahhhh/solve_lwe.py` | Kannan embedding + LLL/BKZ |
| Output solver | `assets/cihuyyyyyyyyyyyyyyy-lwe-sikit-ahhhh/solver-output.txt` | `s`, `e`, verifikasi 64/64 |
| Log submit | `work/submit_curl_log.jsonl` | Flag diterima platform |