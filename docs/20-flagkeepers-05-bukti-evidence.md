# FlagKeepers — Evidence / Bukti

<div class="nx-challenge-head"><span class="nx-chip">1 screenshot</span><span class="nx-chip">5 transkrip / script</span></div>


[← Overview](20-flagkeepers.md) · [Index](index.md)


## Arsip Evidence

> Semua file di bawah berasal dari folder `assets/flagkeepers/`. Screenshot ditempel langsung; file teks/script ditautkan.

### Screenshot

<div class="nx-evidence-grid">
<figure><a href="assets/flagkeepers/98-terminal-evidence.png" target="_blank" rel="noopener"><img src="assets/flagkeepers/98-terminal-evidence.png" alt="98-terminal-evidence.png" loading="lazy"></a><figcaption>98-terminal-evidence.png</figcaption></figure>
</div>

### Transkrip / file pendukung

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