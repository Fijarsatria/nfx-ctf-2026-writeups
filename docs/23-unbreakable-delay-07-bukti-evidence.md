# Unbreakable Delay — Evidence / Bukti

<div class="nx-challenge-head"><span class="nx-chip">3 screenshot</span><span class="nx-chip">2 transkrip / script</span></div>


[← Overview](23-unbreakable-delay.md) · [Index](index.md)

> **Langkah 7/8 — Bukti / Evidence.** Bukti / Evidence
>
> **Titik penting:** arsip screenshot dan transkrip
>
> **Berikutnya:** [Referensi](23-unbreakable-delay-08-referensi.md)


## Arsip Evidence

> Semua file berasal dari `assets/unbreakable-delay/`. Screenshot platform dan terminal adalah bukti asli dari sesi solve; transkrip mentah tetap ditautkan di bagian bawah.

### Platform

<div class="nx-evidence-grid">
<figure><a href="assets/unbreakable-delay/00-challenge-platform.png" target="_blank" rel="noopener"><img src="assets/unbreakable-delay/00-challenge-platform.png" alt="00-challenge-platform.png" loading="lazy"></a><figcaption>00-challenge-platform.png</figcaption></figure>
</div>

*Challenge brief asli di platform NFX CTF 2026.*

<div class="nx-evidence-grid">
<figure><a href="assets/unbreakable-delay/00b-terminal-evidence.png" target="_blank" rel="noopener"><img src="assets/unbreakable-delay/00b-terminal-evidence.png" alt="Terminal evidence (real)" loading="lazy"></a><figcaption>Terminal evidence (real)</figcaption></figure>
</div>

*Terminal evidence (real).*

### Terminal (arsip sesi)

<div class="nx-evidence-grid">
<figure><a href="assets/unbreakable-delay/term-sim-output.png" target="_blank" rel="noopener"><img src="assets/unbreakable-delay/term-sim-output.png" alt="term-sim-output.png" loading="lazy"></a><figcaption>term-sim-output.png</figcaption></figure>
</div>

*Terminal evidence — `sim-output.txt` (arsip transkrip sesi solve).*

### Transkrip mentah & script

- [`sim-output.txt`](assets/unbreakable-delay/sim-output.txt)
- [`sim_vdf.py`](assets/unbreakable-delay/sim_vdf.py)

## Validasi platform (real)

![Validasi platform — CORRECT, BUT ALREADY SOLVED.](assets/unbreakable-delay/00b-platform-validation.png)

*Screenshot asli dari platform NFX CTF 2026. Platform menjawab
`CORRECT, BUT ALREADY SOLVED.` untuk flag ini.*


## Tabel Evidence

| Bukti | File | Keterangan |
|---|---|---|
| Flag tersimpan | `flags/misc/UnbreakableDelay.txt` | Flag |
| Log submit | `work/wave2_submit_parallel.jsonl` | `"Correct! +500 points."` |
| Demo solver | `assets/unbreakable-delay/sim_vdf.py` | XOR factoring + phi shortcut |
| Output demo | `assets/unbreakable-delay/sim-output.txt` | Verifikasi matematis |
| Status service | `work/ENDPOINTS.md`, `misc/SERVICES.md` | Port historis / stopped |