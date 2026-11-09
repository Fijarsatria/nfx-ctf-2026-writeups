# Black Box Protocol N4T0 — Evidence / Bukti

<div class="nx-challenge-head"><span class="nx-chip">5 screenshot</span><span class="nx-chip">4 transkrip / script</span></div>


[← Overview](02-black-box-protocol-n4t0.md) · [Index](index.md)


## Arsip Evidence

> Semua file berasal dari `assets/black-box-protocol-n4t0/`. Screenshot platform dan terminal adalah bukti asli dari sesi solve; transkrip mentah tetap ditautkan di bagian bawah.

### Platform

<div class="nx-evidence-grid">
<figure><a href="assets/black-box-protocol-n4t0/00-challenge-platform.png" target="_blank" rel="noopener"><img src="assets/black-box-protocol-n4t0/00-challenge-platform.png" alt="00-challenge-platform.png" loading="lazy"></a><figcaption>00-challenge-platform.png</figcaption></figure>
</div>

*Challenge brief asli di platform NFX CTF 2026.*

<div class="nx-evidence-grid">
<figure><a href="assets/black-box-protocol-n4t0/00b-submit-platform.png" target="_blank" rel="noopener"><img src="assets/black-box-protocol-n4t0/00b-submit-platform.png" alt="00b-submit-platform.png" loading="lazy"></a><figcaption>00b-submit-platform.png</figcaption></figure>
</div>

*Submit flag di platform: `CORRECT, BUT ALREADY SOLVED.`*

### Terminal (arsip sesi)

<div class="nx-evidence-grid">
<figure><a href="assets/black-box-protocol-n4t0/term-06-recheck-submit.png" target="_blank" rel="noopener"><img src="assets/black-box-protocol-n4t0/term-06-recheck-submit.png" alt="term-06-recheck-submit.png" loading="lazy"></a><figcaption>term-06-recheck-submit.png</figcaption></figure>
</div>

*Terminal evidence — `06-recheck-submit.txt` (arsip transkrip sesi solve).*

<div class="nx-evidence-grid">
<figure><a href="assets/black-box-protocol-n4t0/term-decode-output.png" target="_blank" rel="noopener"><img src="assets/black-box-protocol-n4t0/term-decode-output.png" alt="term-decode-output.png" loading="lazy"></a><figcaption>term-decode-output.png</figcaption></figure>
</div>

*Terminal evidence — `decode-output.txt` (arsip transkrip sesi solve).*

<div class="nx-evidence-grid">
<figure><a href="assets/black-box-protocol-n4t0/term-sha256.png" target="_blank" rel="noopener"><img src="assets/black-box-protocol-n4t0/term-sha256.png" alt="term-sha256.png" loading="lazy"></a><figcaption>term-sha256.png</figcaption></figure>
</div>

*Terminal evidence — `sha256.txt` (arsip transkrip sesi solve).*

### Transkrip mentah & script

- [`06-recheck-submit.txt`](assets/black-box-protocol-n4t0/06-recheck-submit.txt)
- [`decode-output.txt`](assets/black-box-protocol-n4t0/decode-output.txt)
- [`decode_xlsx.py`](assets/black-box-protocol-n4t0/decode_xlsx.py)
- [`sha256.txt`](assets/black-box-protocol-n4t0/sha256.txt)

## Tabel Evidence

| Bukti | File | Keterangan |
|---|---|---|
| Hash attachment | `assets/black-box-protocol-n4t0/sha256.txt` | SHA-256 XLSX |
| Decoder | `assets/black-box-protocol-n4t0/decode_xlsx.py` | Script decode tiga kolom |
| Output decoder | `assets/black-box-protocol-n4t0/decode-output.txt` | Output asli |
| Log submit lama | `work/bb_submit_agent.jsonl` | 53 percobaan di backend lama |
| Recheck submit | `assets/black-box-protocol-n4t0/06-recheck-submit.txt` | `Correct, but already solved.` |
| Release map | `work/release_map.json` | Kandidat alternatif |