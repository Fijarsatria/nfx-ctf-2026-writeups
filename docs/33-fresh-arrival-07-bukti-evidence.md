# Fresh Arrival — Evidence / Bukti

<div class="nx-challenge-head"><span class="nx-chip">9 screenshot</span><span class="nx-chip">4 transkrip / script</span></div>


[← Overview](33-fresh-arrival.md) · [Index](index.md)

> **Langkah 7/8 — Bukti / Evidence.** Semua bukti berada di writeups/assets/fresh-arrival/.
>
> **Titik penting:** arsip screenshot dan transkrip
>
> **Berikutnya:** [Referensi](33-fresh-arrival-08-referensi.md)


## Arsip Evidence

> Semua file berasal dari `assets/fresh-arrival/`. Screenshot platform dan terminal adalah bukti asli dari sesi solve; transkrip mentah tetap ditautkan di bagian bawah.

### Platform

<div class="nx-evidence-grid">
<figure><a href="assets/fresh-arrival/00-challenge-platform.png" target="_blank" rel="noopener"><img src="assets/fresh-arrival/00-challenge-platform.png" alt="00-challenge-platform.png" loading="lazy"></a><figcaption>00-challenge-platform.png</figcaption></figure>
</div>

*Challenge brief asli di platform NFX CTF 2026.*

<div class="nx-evidence-grid">
<figure><a href="assets/fresh-arrival/00b-submit-platform.png" target="_blank" rel="noopener"><img src="assets/fresh-arrival/00b-submit-platform.png" alt="00b-submit-platform.png" loading="lazy"></a><figcaption>00b-submit-platform.png</figcaption></figure>
</div>

*Submit flag di platform: `CORRECT, BUT ALREADY SOLVED.`*

### Terminal (arsip sesi)

<div class="nx-evidence-grid">
<figure><a href="assets/fresh-arrival/term-04-image-compare.png" target="_blank" rel="noopener"><img src="assets/fresh-arrival/term-04-image-compare.png" alt="term-04-image-compare.png" loading="lazy"></a><figcaption>term-04-image-compare.png</figcaption></figure>
</div>

*Terminal evidence — `04-image-compare.txt` (arsip transkrip sesi solve).*

<div class="nx-evidence-grid">
<figure><a href="assets/fresh-arrival/term-05-wikidata-xinhua.png" target="_blank" rel="noopener"><img src="assets/fresh-arrival/term-05-wikidata-xinhua.png" alt="term-05-wikidata-xinhua.png" loading="lazy"></a><figcaption>term-05-wikidata-xinhua.png</figcaption></figure>
</div>

*Terminal evidence — `05-wikidata-xinhua.txt` (arsip transkrip sesi solve).*

<div class="nx-evidence-grid">
<figure><a href="assets/fresh-arrival/term-06-jetphotos-page.png" target="_blank" rel="noopener"><img src="assets/fresh-arrival/term-06-jetphotos-page.png" alt="term-06-jetphotos-page.png" loading="lazy"></a><figcaption>term-06-jetphotos-page.png</figcaption></figure>
</div>

*Terminal evidence — `06-jetphotos-page.txt` (arsip transkrip sesi solve).*

<div class="nx-evidence-grid">
<figure><a href="assets/fresh-arrival/term-07-hashes.png" target="_blank" rel="noopener"><img src="assets/fresh-arrival/term-07-hashes.png" alt="term-07-hashes.png" loading="lazy"></a><figcaption>term-07-hashes.png</figcaption></figure>
</div>

*Terminal evidence — `07-hashes.txt` (arsip transkrip sesi solve).*

### Screenshot langkah

<div class="nx-evidence-grid">
<figure><a href="assets/fresh-arrival/01-spotted.jpg" target="_blank" rel="noopener"><img src="assets/fresh-arrival/01-spotted.jpg" alt="01-spotted.jpg" loading="lazy"></a><figcaption>01-spotted.jpg</figcaption></figure>
</div>

*Evidence — `01-spotted.jpg`.*

<div class="nx-evidence-grid">
<figure><a href="assets/fresh-arrival/02-jetphotos-11925184-thumb.jpg" target="_blank" rel="noopener"><img src="assets/fresh-arrival/02-jetphotos-11925184-thumb.jpg" alt="02-jetphotos-11925184-thumb.jpg" loading="lazy"></a><figcaption>02-jetphotos-11925184-thumb.jpg</figcaption></figure>
</div>

*Evidence — `02-jetphotos-11925184-thumb.jpg`.*

<div class="nx-evidence-grid">
<figure><a href="assets/fresh-arrival/03-pixel-diff-x8.png" target="_blank" rel="noopener"><img src="assets/fresh-arrival/03-pixel-diff-x8.png" alt="03-pixel-diff-x8.png" loading="lazy"></a><figcaption>03-pixel-diff-x8.png</figcaption></figure>
</div>

*Evidence — `03-pixel-diff-x8.png`.*

### Transkrip mentah & script

- [`04-image-compare.txt`](assets/fresh-arrival/04-image-compare.txt)
- [`05-wikidata-xinhua.txt`](assets/fresh-arrival/05-wikidata-xinhua.txt)
- [`06-jetphotos-page.txt`](assets/fresh-arrival/06-jetphotos-page.txt)
- [`07-hashes.txt`](assets/fresh-arrival/07-hashes.txt)

## Tabel Evidence

Semua bukti berada di `writeups/assets/fresh-arrival/`.

| Bukti | File | Keterangan |
|---|---|---|
| Foto challenge | `01-spotted.jpg` | 400×225, hash `1b74fef0...` |
| Thumbnail JetPhotos | `02-jetphotos-11925184-thumb.jpg` | Foto yang sama, CDN JetPhotos |
| Diff piksel | `03-pixel-diff-x8.png` | Selisih piksel diperbesar 8× |
| Perbandingan | `04-image-compare.txt` | Ukuran, hash, MAE, jumlah piksel identik |
| Wikidata Xinhua | `05-wikidata-xinhua.txt` | IATA `XW`, ICAO `CXH`, HQ Beijing |
| Halaman JetPhotos | `06-jetphotos-page.txt` | Metadata fotografer, tanggal, lokasi, MSN |
| Hash | `07-hashes.txt` | SHA-256 kedua gambar |