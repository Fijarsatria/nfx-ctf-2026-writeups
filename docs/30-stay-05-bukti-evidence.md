# Stay — Evidence / Bukti

<div class="nx-challenge-head"><span class="nx-chip">8 screenshot</span><span class="nx-chip">7 transkrip / script</span></div>


[← Overview](30-stay.md) · [Index](index.md)

> **Langkah 5/6 — Bukti / Evidence.** Semua bukti berada di writeups/assets/stay/.
>
> **Titik penting:** arsip screenshot dan transkrip
>
> **Berikutnya:** [Referensi](30-stay-06-referensi.md)


## Arsip Evidence

> Semua file berasal dari `assets/stay/`. Screenshot platform dan terminal adalah bukti asli dari sesi solve; transkrip mentah tetap ditautkan di bagian bawah.

### Platform

<div class="nx-evidence-grid">
<figure><a href="assets/stay/00-challenge-platform.png" target="_blank" rel="noopener"><img src="assets/stay/00-challenge-platform.png" alt="00-challenge-platform.png" loading="lazy"></a><figcaption>00-challenge-platform.png</figcaption></figure>
</div>

*Challenge brief asli di platform NFX CTF 2026.*

<div class="nx-evidence-grid">
<figure><a href="assets/stay/00b-terminal-evidence.png" target="_blank" rel="noopener"><img src="assets/stay/00b-terminal-evidence.png" alt="Terminal evidence (real)" loading="lazy"></a><figcaption>Terminal evidence (real)</figcaption></figure>
</div>

*Terminal evidence (real).*

### Terminal (arsip sesi)

<div class="nx-evidence-grid">
<figure><a href="assets/stay/term-00-solve-output.png" target="_blank" rel="noopener"><img src="assets/stay/term-00-solve-output.png" alt="term-00-solve-output.png" loading="lazy"></a><figcaption>term-00-solve-output.png</figcaption></figure>
</div>

*Terminal evidence — `00-solve-output.txt` (arsip transkrip sesi solve).*

<div class="nx-evidence-grid">
<figure><a href="assets/stay/term-01-zero-width-sequence.png" target="_blank" rel="noopener"><img src="assets/stay/term-01-zero-width-sequence.png" alt="term-01-zero-width-sequence.png" loading="lazy"></a><figcaption>term-01-zero-width-sequence.png</figcaption></figure>
</div>

*Terminal evidence — `01-zero-width-sequence.txt` (arsip transkrip sesi solve).*

<div class="nx-evidence-grid">
<figure><a href="assets/stay/term-02-bitstream.png" target="_blank" rel="noopener"><img src="assets/stay/term-02-bitstream.png" alt="term-02-bitstream.png" loading="lazy"></a><figcaption>term-02-bitstream.png</figcaption></figure>
</div>

*Terminal evidence — `02-bitstream.txt` (arsip transkrip sesi solve).*

<div class="nx-evidence-grid">
<figure><a href="assets/stay/term-03-plaintext.png" target="_blank" rel="noopener"><img src="assets/stay/term-03-plaintext.png" alt="term-03-plaintext.png" loading="lazy"></a><figcaption>term-03-plaintext.png</figcaption></figure>
</div>

*Terminal evidence — `03-plaintext.txt` (arsip transkrip sesi solve).*

<div class="nx-evidence-grid">
<figure><a href="assets/stay/term-04-raw-zero-width.png" target="_blank" rel="noopener"><img src="assets/stay/term-04-raw-zero-width.png" alt="term-04-raw-zero-width.png" loading="lazy"></a><figcaption>term-04-raw-zero-width.png</figcaption></figure>
</div>

*Terminal evidence — `04-raw-zero-width.txt` (arsip transkrip sesi solve).*

<div class="nx-evidence-grid">
<figure><a href="assets/stay/term-05-zero-width-seq.png" target="_blank" rel="noopener"><img src="assets/stay/term-05-zero-width-seq.png" alt="term-05-zero-width-seq.png" loading="lazy"></a><figcaption>term-05-zero-width-seq.png</figcaption></figure>
</div>

*Terminal evidence — `05-zero-width-seq.txt` (arsip transkrip sesi solve).*

### Transkrip mentah & script

- [`00-solve-output.txt`](assets/stay/00-solve-output.txt)
- [`01-zero-width-sequence.txt`](assets/stay/01-zero-width-sequence.txt)
- [`02-bitstream.txt`](assets/stay/02-bitstream.txt)
- [`03-plaintext.txt`](assets/stay/03-plaintext.txt)
- [`04-raw-zero-width.txt`](assets/stay/04-raw-zero-width.txt)
- [`05-zero-width-seq.txt`](assets/stay/05-zero-width-seq.txt)
- [`solve_stay.py`](assets/stay/solve_stay.py)

## Validasi platform (real)

![Validasi platform — CORRECT, BUT ALREADY SOLVED.](assets/stay/00b-platform-validation.png)

*Screenshot asli dari platform NFX CTF 2026. Platform menjawab
`CORRECT, BUT ALREADY SOLVED.` untuk flag ini.*


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