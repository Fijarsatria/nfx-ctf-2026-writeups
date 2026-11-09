# FlagKeepers — Evidence / Bukti

<div class="nx-challenge-head"><span class="nx-chip">3 screenshot</span><span class="nx-chip">5 transkrip / script</span></div>


[← Overview](20-flagkeepers.md) · [Index](index.md)


## Arsip Evidence

> Semua file berasal dari `assets/flagkeepers/`. Screenshot platform dan terminal adalah bukti asli dari sesi solve; transkrip mentah tetap ditautkan di bagian bawah.

### Platform

<div class="nx-evidence-grid">
<figure><a href="assets/flagkeepers/00-challenge-platform.png" target="_blank" rel="noopener"><img src="assets/flagkeepers/00-challenge-platform.png" alt="00-challenge-platform.png" loading="lazy"></a><figcaption>00-challenge-platform.png</figcaption></figure>
</div>

*Challenge brief asli di platform NFX CTF 2026.*

<div class="nx-evidence-grid">
<figure><a href="assets/flagkeepers/00b-submit-platform.png" target="_blank" rel="noopener"><img src="assets/flagkeepers/00b-submit-platform.png" alt="00b-submit-platform.png" loading="lazy"></a><figcaption>00b-submit-platform.png</figcaption></figure>
</div>

*Submit flag di platform: `CORRECT, BUT ALREADY SOLVED.`*

### Terminal (arsip sesi)

<div class="nx-evidence-grid">
<figure><a href="assets/flagkeepers/term-offline-sim-output.png" target="_blank" rel="noopener"><img src="assets/flagkeepers/term-offline-sim-output.png" alt="term-offline-sim-output.png" loading="lazy"></a><figcaption>term-offline-sim-output.png</figcaption></figure>
</div>

*Terminal evidence — `offline-sim-output.txt` (arsip transkrip sesi solve).*

### Transkrip mentah & script

- [`exploit_live.py`](assets/flagkeepers/exploit_live.py)
- [`gcmtool.py`](assets/flagkeepers/gcmtool.py)
- [`live_run.log`](assets/flagkeepers/live_run.log)
- [`offline-sim-output.txt`](assets/flagkeepers/offline-sim-output.txt)
- [`offline_sim.py`](assets/flagkeepers/offline_sim.py)

## Tabel Evidence

| Bukti | File | Keterangan |
|---|---|---|
| Hash input | `assets/checksums-all.txt` | SHA-256 `app.py` |
| Source | `crypto/FlagKeepers/app.py` | Nonce global, logika flag |
| Helper GHASH | `assets/flagkeepers/gcmtool.py` | GF(2^128), recover H |
| Exploit live | `assets/flagkeepers/exploit_live.py` | 14 sampel + forge |
| Log live | `assets/flagkeepers/live_run.log` | H, CT/TAG forged, flag |
| Simulasi offline | `assets/flagkeepers/offline_sim.py` / `offline-sim-output.txt` | Reproduksi + verifikasi tag |
| Log submit | `work/wave2_submit_parallel.jsonl` | Flag diterima platform |