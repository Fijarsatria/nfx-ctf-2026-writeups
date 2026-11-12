# 13 Is Not Enough — Evidence / Bukti

<div class="nx-challenge-head"><span class="nx-chip">3 screenshot</span><span class="nx-chip">2 transkrip / script</span></div>

[← Overview](77-13-is-not-enough.md) · [Index](index.md)

> **Langkah 4/5 — Bukti / Evidence.** Screenshot platform, output solver, dan
> file mentah.
>
> **Titik penting:** `CORRECT, BUT ALREADY SOLVED.` + solver empat layer.
>
> **Berikutnya:** [Referensi](77-13-is-not-enough-05-referensi.md)

## Arsip Evidence

> Semua file berasal dari `assets/13-is-not-enough/`. Screenshot platform dan
> terminal adalah bukti asli dari sesi solve; transkrip mentah dan solver
> tetap ditautkan di bagian bawah.

### Platform

<div class="nx-evidence-grid">
<figure><a href="assets/13-is-not-enough/00-challenge-platform.png" target="_blank" rel="noopener"><img src="assets/13-is-not-enough/00-challenge-platform.png" alt="00-challenge-platform.png" loading="lazy"></a><figcaption>00-challenge-platform.png</figcaption></figure>
</div>

*Challenge brief asli di platform NFX CTF 2026.*

<div class="nx-evidence-grid">
<figure><a href="assets/13-is-not-enough/00b-platform-validation.png" target="_blank" rel="noopener"><img src="assets/13-is-not-enough/00b-platform-validation.png" alt="Validasi platform — CORRECT, BUT ALREADY SOLVED." loading="lazy"></a><figcaption>00b-platform-validation.png</figcaption></figure>
</div>

*Screenshot submit web: platform menjawab `CORRECT, BUT ALREADY SOLVED.`*

### Terminal (arsip sesi)

<div class="nx-evidence-grid">
<figure><a href="assets/13-is-not-enough/term-11-solver.png" target="_blank" rel="noopener"><img src="assets/13-is-not-enough/term-11-solver.png" alt="term-11-solver.png" loading="lazy"></a><figcaption>term-11-solver.png</figcaption></figure>
</div>

*Output solver asli — ciphertext, XOR 13, reverse, ROT13, digit -3.*

## Tabel Evidence

- Challenge brief: `assets/13-is-not-enough/00-challenge-platform.png`
- Validasi platform: `assets/13-is-not-enough/00b-platform-validation.png`
- Output solver: `assets/13-is-not-enough/term-11-solver.png`
- Transkrip solver: `assets/13-is-not-enough/11-solver.txt`
- Solver: `assets/13-is-not-enough/11-solver.py`
- Analisis: `assets/13-is-not-enough/10-ANALYSIS.md`
- Ciphertext + intermediate: `assets/13-is-not-enough/10-ciphertext.txt`

## Ringkasan

- Panjang ciphertext dan flag sama-sama 47 karakter.
- ROT13+ROT5 langsung **tidak** cocok.
- Urutan yang benar: XOR 13 → reverse → ROT13 → digit -3.
- Flag final diterima platform: `CORRECT, BUT ALREADY SOLVED.`

**Berkas mentah:** [ANALYSIS.md](assets/13-is-not-enough/10-ANALYSIS.md) ·
[11-solver.py](assets/13-is-not-enough/11-solver.py) ·
[11-solver.txt](assets/13-is-not-enough/11-solver.txt) ·
[10-ciphertext.txt](assets/13-is-not-enough/10-ciphertext.txt)
