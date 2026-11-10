# Dokodemo Door — Evidence / Bukti

<div class="nx-challenge-head"><span class="nx-chip">5 screenshot</span><span class="nx-chip">5 transkrip / script</span></div>


[← Overview](28-dokodemo-door.md) · [Index](index.md)

> **Langkah 8/9 — Bukti / Evidence.** Semua bukti berada di writeups/assets/dokodemo-door/.
>
> **Titik penting:** arsip screenshot dan transkrip
>
> **Berikutnya:** [Referensi](28-dokodemo-door-09-referensi.md)


## Arsip Evidence

> Semua file berasal dari `assets/dokodemo-door/`. Screenshot platform dan terminal adalah bukti asli dari sesi solve; transkrip mentah tetap ditautkan di bagian bawah.

### Platform

<div class="nx-evidence-grid">
<figure><a href="assets/dokodemo-door/00-challenge-platform.png" target="_blank" rel="noopener"><img src="assets/dokodemo-door/00-challenge-platform.png" alt="00-challenge-platform.png" loading="lazy"></a><figcaption>00-challenge-platform.png</figcaption></figure>
</div>

*Challenge brief asli di platform NFX CTF 2026.*

<div class="nx-evidence-grid">
<figure><a href="assets/dokodemo-door/00b-submit-platform.png" target="_blank" rel="noopener"><img src="assets/dokodemo-door/00b-submit-platform.png" alt="00b-submit-platform.png" loading="lazy"></a><figcaption>00b-submit-platform.png</figcaption></figure>
</div>

*Submit flag di platform: `CORRECT, BUT ALREADY SOLVED.`*

### Terminal (arsip sesi)

<div class="nx-evidence-grid">
<figure><a href="assets/dokodemo-door/term-01-solve-output.png" target="_blank" rel="noopener"><img src="assets/dokodemo-door/term-01-solve-output.png" alt="term-01-solve-output.png" loading="lazy"></a><figcaption>term-01-solve-output.png</figcaption></figure>
</div>

*Terminal evidence — `01-solve-output.txt` (arsip transkrip sesi solve).*

<div class="nx-evidence-grid">
<figure><a href="assets/dokodemo-door/term-02-extracted-text.png" target="_blank" rel="noopener"><img src="assets/dokodemo-door/term-02-extracted-text.png" alt="term-02-extracted-text.png" loading="lazy"></a><figcaption>term-02-extracted-text.png</figcaption></figure>
</div>

*Terminal evidence — `02-extracted-text.txt` (arsip transkrip sesi solve).*

### Screenshot langkah

<div class="nx-evidence-grid">
<figure><a href="assets/dokodemo-door/04-page-image.jpg" target="_blank" rel="noopener"><img src="assets/dokodemo-door/04-page-image.jpg" alt="04-page-image.jpg" loading="lazy"></a><figcaption>04-page-image.jpg</figcaption></figure>
</div>

*Evidence — `04-page-image.jpg`.*

### Transkrip mentah & script

- [`01-solve-output.txt`](assets/dokodemo-door/01-solve-output.txt)
- [`02-extracted-text.txt`](assets/dokodemo-door/02-extracted-text.txt)
- [`03-decrypted.pdf`](assets/dokodemo-door/03-decrypted.pdf)
- [`extract_text.py`](assets/dokodemo-door/extract_text.py)
- [`solve_dokodemo.py`](assets/dokodemo-door/solve_dokodemo.py)

## Tabel Evidence

Semua bukti berada di `writeups/assets/dokodemo-door/`.

| Bukti | File | Keterangan |
|---|---|---|
| Output solver | `01-solve-output.txt` | Panjang key, key, header/trailer, hash |
| Teks PDF | `02-extracted-text.txt` | Hasil decode content stream, termasuk flag |
| PDF terdekripsi | `03-decrypted.pdf` | File asli setelah XOR |
| Gambar halaman | `04-page-image.jpg` | Gambar yang tertanam di PDF |
| Solver | `solve_dokodemo.py` | Script crib-drag yang dijalankan |
| Ekstraktor teks | `extract_text.py` | Decoder ASCII85 + Flate + operator `Tj` |