# Static IV Offline — Evidence / Bukti

<div class="nx-challenge-head"><span class="nx-chip">1 screenshot</span><span class="nx-chip">4 transkrip / script</span></div>


[← Overview](22-static-iv-offline.md) · [Index](index.md)


## Arsip Evidence

> Semua file di bawah berasal dari folder `assets/static-iv-offline/`. Screenshot ditempel langsung; file teks/script ditautkan.

### Screenshot

<div class="nx-evidence-grid">
<figure><a href="assets/static-iv-offline/98-terminal-evidence.png" target="_blank" rel="noopener"><img src="assets/static-iv-offline/98-terminal-evidence.png" alt="98-terminal-evidence.png" loading="lazy"></a><figcaption>98-terminal-evidence.png</figcaption></figure>
</div>

### Transkrip / file pendukung

- [`solve.py`](assets/static-iv-offline/solve.py)
- [`solver-output.txt`](assets/static-iv-offline/solver-output.txt)
- [`verify-output.txt`](assets/static-iv-offline/verify-output.txt)
- [`verify.py`](assets/static-iv-offline/verify.py)

## Tabel Evidence

| Bukti | File | Keterangan |
|---|---|---|
| Hash input | `assets/checksums-all.txt` | SHA-256 `challenge.py`, `output.txt` |
| Solver | `assets/static-iv-offline/solve.py` | AES-CBC decrypt + unpad |
| Output solver | `assets/static-iv-offline/solver-output.txt` | Flag |
| Verifikasi | `assets/static-iv-offline/verify-output.txt` | Key, plaintext, prefix |
| Log submit | `work/wave2_submit_parallel.jsonl` | Flag diterima platform |