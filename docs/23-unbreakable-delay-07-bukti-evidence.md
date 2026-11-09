# Unbreakable Delay — Evidence / Bukti

<div class="nx-challenge-head"><span class="nx-chip">3 screenshot</span><span class="nx-chip">2 transkrip / script</span></div>


[← Overview](23-unbreakable-delay.md) · [Index](index.md)


## Arsip Evidence

> Semua file berasal dari `assets/unbreakable-delay/`. Screenshot platform dan terminal adalah bukti asli dari sesi solve; transkrip mentah tetap ditautkan di bagian bawah.

### Platform

<div class="nx-evidence-grid">
<figure><a href="assets/unbreakable-delay/00-challenge-platform.png" target="_blank" rel="noopener"><img src="assets/unbreakable-delay/00-challenge-platform.png" alt="00-challenge-platform.png" loading="lazy"></a><figcaption>00-challenge-platform.png</figcaption></figure>
</div>

*Challenge brief asli di platform NFX CTF 2026.*

<div class="nx-evidence-grid">
<figure><a href="assets/unbreakable-delay/00b-submit-platform.png" target="_blank" rel="noopener"><img src="assets/unbreakable-delay/00b-submit-platform.png" alt="00b-submit-platform.png" loading="lazy"></a><figcaption>00b-submit-platform.png</figcaption></figure>
</div>

*Submit flag di platform: `CORRECT, BUT ALREADY SOLVED.`*

### Terminal (arsip sesi)

<div class="nx-evidence-grid">
<figure><a href="assets/unbreakable-delay/term-sim-output.png" target="_blank" rel="noopener"><img src="assets/unbreakable-delay/term-sim-output.png" alt="term-sim-output.png" loading="lazy"></a><figcaption>term-sim-output.png</figcaption></figure>
</div>

*Terminal evidence — `sim-output.txt` (arsip transkrip sesi solve).*

### Transkrip mentah & script

- [`sim-output.txt`](assets/unbreakable-delay/sim-output.txt)
- [`sim_vdf.py`](assets/unbreakable-delay/sim_vdf.py)

## Tabel Evidence

| Bukti | File | Keterangan |
|---|---|---|
| Flag tersimpan | `flags/misc/UnbreakableDelay.txt` | Flag |
| Log submit | `work/wave2_submit_parallel.jsonl` | `"Correct! +500 points."` |
| Demo solver | `assets/unbreakable-delay/sim_vdf.py` | XOR factoring + phi shortcut |
| Output demo | `assets/unbreakable-delay/sim-output.txt` | Verifikasi matematis |
| Status service | `work/ENDPOINTS.md`, `misc/SERVICES.md` | Port historis / stopped |