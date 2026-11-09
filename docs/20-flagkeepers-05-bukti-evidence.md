# FlagKeepers — Evidence / Bukti

[← Overview](20-flagkeepers.md) · [Index](index.md)


## Arsip Evidence

> Semua file di bawah berasal dari folder `assets/flagkeepers/`. Screenshot ditempel langsung; file teks/script ditautkan.

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
