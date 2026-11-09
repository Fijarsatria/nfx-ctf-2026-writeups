# Heker Tersenyum - Art Evidence Secret — Evidence / Bukti

<div class="nx-challenge-head"><span class="nx-chip">4 screenshot</span><span class="nx-chip">9 transkrip / script</span></div>


[← Overview](05-heker-tersenyum-art-evidence-secret.md) · [Index](index.md)


## Arsip Evidence

> Semua file di bawah berasal dari folder `assets/heker-tersenyum-art-evidence-secret/`. Screenshot ditempel langsung; file teks/script ditautkan.

### Screenshot

<div class="nx-evidence-grid">
<figure><a href="assets/heker-tersenyum-art-evidence-secret/00-original.png" target="_blank" rel="noopener"><img src="assets/heker-tersenyum-art-evidence-secret/00-original.png" alt="00-original.png" loading="lazy"></a><figcaption>00-original.png</figcaption></figure>
<figure><a href="assets/heker-tersenyum-art-evidence-secret/04-lsb-R.png" target="_blank" rel="noopener"><img src="assets/heker-tersenyum-art-evidence-secret/04-lsb-R.png" alt="04-lsb-R.png" loading="lazy"></a><figcaption>04-lsb-R.png</figcaption></figure>
<figure><a href="assets/heker-tersenyum-art-evidence-secret/05-lsb-B.png" target="_blank" rel="noopener"><img src="assets/heker-tersenyum-art-evidence-secret/05-lsb-B.png" alt="05-lsb-B.png" loading="lazy"></a><figcaption>05-lsb-B.png</figcaption></figure>
<figure><a href="assets/heker-tersenyum-art-evidence-secret/98-terminal-evidence.png" target="_blank" rel="noopener"><img src="assets/heker-tersenyum-art-evidence-secret/98-terminal-evidence.png" alt="98-terminal-evidence.png" loading="lazy"></a><figcaption>98-terminal-evidence.png</figcaption></figure>
</div>

### Transkrip / file pendukung

- [`01-zsteg.txt`](assets/heker-tersenyum-art-evidence-secret/01-zsteg.txt)
- [`02-R-payload.bin`](assets/heker-tersenyum-art-evidence-secret/02-R-payload.bin)
- [`03-B-payload.bin`](assets/heker-tersenyum-art-evidence-secret/03-B-payload.bin)
- [`06-file-exiftool.txt`](assets/heker-tersenyum-art-evidence-secret/06-file-exiftool.txt)
- [`07-solve-output.txt`](assets/heker-tersenyum-art-evidence-secret/07-solve-output.txt)
- [`08-payload-hexdump.txt`](assets/heker-tersenyum-art-evidence-secret/08-payload-hexdump.txt)
- [`B-payload.bin`](assets/heker-tersenyum-art-evidence-secret/B-payload.bin)
- [`R-payload.bin`](assets/heker-tersenyum-art-evidence-secret/R-payload.bin)
- [`solve_heker.py`](assets/heker-tersenyum-art-evidence-secret/solve_heker.py)

## Tabel Evidence

| Bukti | File | Keterangan |
|---|---|---|
| Artefak asli | `assets/heker-tersenyum-art-evidence-secret/00-original.png` | PNG 1495×2424 |
| Metadata | `assets/heker-tersenyum-art-evidence-secret/06-file-exiftool.txt` | `file`, hash, exiftool |
| zsteg | `assets/heker-tersenyum-art-evidence-secret/01-zsteg.txt` | output `zsteg -a` |
| Payload R | `assets/heker-tersenyum-art-evidence-secret/02-R-payload.bin` | 108 byte setelah header `CTF1` |
| Payload B | `assets/heker-tersenyum-art-evidence-secret/03-B-payload.bin` | 53 byte setelah header `CTF1` |
| Hexdump | `assets/heker-tersenyum-art-evidence-secret/08-payload-hexdump.txt` | xxd kedua payload |
| Solver | `assets/heker-tersenyum-art-evidence-secret/solve_heker.py` | ekstraksi LSB R/B |
| Output solver | `assets/heker-tersenyum-art-evidence-secret/07-solve-output.txt` | log ekstraksi |
| Bitplane R/B | `assets/heker-tersenyum-art-evidence-secret/04-lsb-R.png`, `05-lsb-B.png` | visualisasi LSB |