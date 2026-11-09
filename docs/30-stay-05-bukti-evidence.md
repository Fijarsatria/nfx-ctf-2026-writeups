# Stay — Evidence / Bukti

<div class="nx-challenge-head"><span class="nx-chip">1 screenshot</span><span class="nx-chip">7 transkrip / script</span></div>


[← Overview](30-stay.md) · [Index](index.md)


## Arsip Evidence

> Semua file di bawah berasal dari folder `assets/stay/`. Screenshot ditempel langsung; file teks/script ditautkan.

### Screenshot

<div class="nx-evidence-grid">
<figure><a href="assets/stay/98-terminal-evidence.png" target="_blank" rel="noopener"><img src="assets/stay/98-terminal-evidence.png" alt="98-terminal-evidence.png" loading="lazy"></a><figcaption>98-terminal-evidence.png</figcaption></figure>
</div>

### Transkrip / file pendukung

- [`00-solve-output.txt`](assets/stay/00-solve-output.txt)
- [`01-zero-width-sequence.txt`](assets/stay/01-zero-width-sequence.txt)
- [`02-bitstream.txt`](assets/stay/02-bitstream.txt)
- [`03-plaintext.txt`](assets/stay/03-plaintext.txt)
- [`04-raw-zero-width.txt`](assets/stay/04-raw-zero-width.txt)
- [`05-zero-width-seq.txt`](assets/stay/05-zero-width-seq.txt)
- [`solve_stay.py`](assets/stay/solve_stay.py)

## Tabel Evidence

Semua bukti berada di `writeups/assets/stay/`.

| Bukti | File | Keterangan |
|---|---|---|
| Output solver | `00-solve-output.txt` | Hitungan karakter, bit, Base64, hex, plaintext |
| Urutan zero-width | `01-zero-width-sequence.txt` | 176 karakter asli |
| Bitstream | `02-bitstream.txt` | 352 bit (`0`/`1`) |
| Plaintext | `03-plaintext.txt` | `NXCTF{...}` |
| Zero-width mentah | `04-raw-zero-width.txt` | Salinan `stay_zw_raw.txt` (528 byte) |
| Sequence `a/b/c/d` | `05-zero-width-seq.txt` | Salinan `stay_zw_seq.txt` (176 byte) |
| Solver | `solve_stay.py` | Script yang dijalankan |