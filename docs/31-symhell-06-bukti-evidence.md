# SymHell — Evidence / Bukti

<div class="nx-challenge-head"><span class="nx-chip">5 screenshot</span><span class="nx-chip">4 transkrip / script</span></div>


[← Overview](31-symhell.md) · [Index](index.md)

> **Langkah 6/7 — Bukti / Evidence.** Semua bukti berada di writeups/assets/symhell/.
>
> **Titik penting:** arsip screenshot dan transkrip
>
> **Berikutnya:** [Referensi](31-symhell-07-referensi.md)


## Arsip Evidence

> Semua file berasal dari `assets/symhell/`. Screenshot platform dan terminal adalah bukti asli dari sesi solve; transkrip mentah tetap ditautkan di bagian bawah.

### Platform

<div class="nx-evidence-grid">
<figure><a href="assets/symhell/00-challenge-platform.png" target="_blank" rel="noopener"><img src="assets/symhell/00-challenge-platform.png" alt="00-challenge-platform.png" loading="lazy"></a><figcaption>00-challenge-platform.png</figcaption></figure>
</div>

*Challenge brief asli di platform NFX CTF 2026.*

<div class="nx-evidence-grid">
<figure><a href="assets/symhell/00b-terminal-evidence.png" target="_blank" rel="noopener"><img src="assets/symhell/00b-terminal-evidence.png" alt="Terminal evidence (real)" loading="lazy"></a><figcaption>Terminal evidence (real)</figcaption></figure>
</div>

*Terminal evidence (real).*

### Terminal (arsip sesi)

<div class="nx-evidence-grid">
<figure><a href="assets/symhell/term-02-hashes.png" target="_blank" rel="noopener"><img src="assets/symhell/term-02-hashes.png" alt="term-02-hashes.png" loading="lazy"></a><figcaption>term-02-hashes.png</figcaption></figure>
</div>

*Terminal evidence — `02-hashes.txt` (arsip transkrip sesi solve).*

<div class="nx-evidence-grid">
<figure><a href="assets/symhell/term-03-exploit-transcript.png" target="_blank" rel="noopener"><img src="assets/symhell/term-03-exploit-transcript.png" alt="term-03-exploit-transcript.png" loading="lazy"></a><figcaption>term-03-exploit-transcript.png</figcaption></figure>
</div>

*Terminal evidence — `03-exploit-transcript.txt` (arsip transkrip sesi solve).*

<div class="nx-evidence-grid">
<figure><a href="assets/symhell/term-exploit_local.png" target="_blank" rel="noopener"><img src="assets/symhell/term-exploit_local.png" alt="term-exploit_local.png" loading="lazy"></a><figcaption>term-exploit_local.png</figcaption></figure>
</div>

*Terminal evidence — `exploit_local.txt` (arsip transkrip sesi solve).*

### Transkrip mentah & script

- [`02-hashes.txt`](assets/symhell/02-hashes.txt)
- [`03-exploit-transcript.txt`](assets/symhell/03-exploit-transcript.txt)
- [`app.py`](assets/symhell/app.py)
- [`exploit_local.txt`](assets/symhell/exploit_local.txt)

## Tabel Evidence

Semua bukti berada di `writeups/assets/symhell/`.

| Bukti | File | Keterangan |
|---|---|---|
| Transcript exploit | `03-exploit-transcript.txt` | Payload, cek filter, respons service (ANSI dibersihkan) |
| Transcript mentah | `exploit_local.txt` | Output asli termasuk escape ANSI |
| Hash source | `02-hashes.txt` | SHA-256 `app.py` |
| Source service | `app.py` | Salinan `forensics/symhell/app.py` |