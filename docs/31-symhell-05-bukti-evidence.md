# SymHell — Evidence / Bukti

<div class="nx-challenge-head"><span class="nx-chip">1 screenshot</span><span class="nx-chip">4 transkrip / script</span></div>


[← Overview](31-symhell.md) · [Index](index.md)


## Arsip Evidence

> Semua file di bawah berasal dari folder `assets/symhell/`. Screenshot ditempel langsung; file teks/script ditautkan.

### Screenshot

<div class="nx-evidence-grid">
<figure><a href="assets/symhell/98-terminal-evidence.png" target="_blank" rel="noopener"><img src="assets/symhell/98-terminal-evidence.png" alt="98-terminal-evidence.png" loading="lazy"></a><figcaption>98-terminal-evidence.png</figcaption></figure>
</div>

### Transkrip / file pendukung

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