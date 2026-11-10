# Frekuensi Sunyi — Evidence / Bukti

<div class="nx-challenge-head"><span class="nx-chip">6 screenshot</span><span class="nx-chip">2 transkrip / script</span></div>


[← Overview](08-frekuensi-sunyi.md) · [Index](index.md)

> **Langkah 8/9 — Bukti / Evidence.** Semua bukti berada di writeups/assets/frekuensi-sunyi/.
>
> **Titik penting:** arsip screenshot dan transkrip
>
> **Berikutnya:** [Referensi](08-frekuensi-sunyi-09-referensi.md)


## Arsip Evidence

> Semua file berasal dari `assets/frekuensi-sunyi/`. Screenshot platform dan terminal adalah bukti asli dari sesi solve; transkrip mentah tetap ditautkan di bagian bawah.

### Platform

<div class="nx-evidence-grid">
<figure><a href="assets/frekuensi-sunyi/00-challenge-platform.png" target="_blank" rel="noopener"><img src="assets/frekuensi-sunyi/00-challenge-platform.png" alt="00-challenge-platform.png" loading="lazy"></a><figcaption>00-challenge-platform.png</figcaption></figure>
</div>

*Challenge brief asli di platform NFX CTF 2026.*

<div class="nx-evidence-grid">
<figure><a href="assets/frekuensi-sunyi/00-provided-spectrogram.png" target="_blank" rel="noopener"><img src="assets/frekuensi-sunyi/00-provided-spectrogram.png" alt="00-provided-spectrogram.png" loading="lazy"></a><figcaption>00-provided-spectrogram.png</figcaption></figure>
</div>

*Evidence — `00-provided-spectrogram.png`.*

<div class="nx-evidence-grid">
<figure><a href="assets/frekuensi-sunyi/00b-submit-platform.png" target="_blank" rel="noopener"><img src="assets/frekuensi-sunyi/00b-submit-platform.png" alt="00b-submit-platform.png" loading="lazy"></a><figcaption>00b-submit-platform.png</figcaption></figure>
</div>

*Submit flag di platform: `CORRECT, BUT ALREADY SOLVED.`*

### Terminal (arsip sesi)

<div class="nx-evidence-grid">
<figure><a href="assets/frekuensi-sunyi/term-05-audio-analysis.png" target="_blank" rel="noopener"><img src="assets/frekuensi-sunyi/term-05-audio-analysis.png" alt="term-05-audio-analysis.png" loading="lazy"></a><figcaption>term-05-audio-analysis.png</figcaption></figure>
</div>

*Terminal evidence — `05-audio-analysis.txt` (arsip transkrip sesi solve).*

### Screenshot langkah

<div class="nx-evidence-grid">
<figure><a href="assets/frekuensi-sunyi/01-spectrogram-repro.png" target="_blank" rel="noopener"><img src="assets/frekuensi-sunyi/01-spectrogram-repro.png" alt="01-spectrogram-repro.png" loading="lazy"></a><figcaption>01-spectrogram-repro.png</figcaption></figure>
</div>

*Evidence — `01-spectrogram-repro.png`.*

<div class="nx-evidence-grid">
<figure><a href="assets/frekuensi-sunyi/04-text-crop.png" target="_blank" rel="noopener"><img src="assets/frekuensi-sunyi/04-text-crop.png" alt="04-text-crop.png" loading="lazy"></a><figcaption>04-text-crop.png</figcaption></figure>
</div>

*Evidence — `04-text-crop.png`.*

### Transkrip mentah & script

- [`05-audio-analysis.txt`](assets/frekuensi-sunyi/05-audio-analysis.txt)
- [`solve_frekuensi.py`](assets/frekuensi-sunyi/solve_frekuensi.py)

## Tabel Evidence

Semua bukti berada di `writeups/assets/frekuensi-sunyi/`.

| Bukti | File | Keterangan |
|---|---|---|
| Spektrogram bersih (referensi) | `00-provided-spectrogram.png` | Salinan `flags/misc/Frekuensi_Sunyi_spectrogram.png`; glyph terbaca jelas |
| Reproduksi spektrogram | `01-spectrogram-repro.png` | Hasil STFT + median filter lokal |
| Crop teks | `04-text-crop.png` | Perbesaran area glyph `ASK{o0fP4_Pr01Y}` |
| Analisis audio | `05-audio-analysis.txt` | Metadata WAV, hash, channel identik, parameter STFT, transkripsi, ROT13 |
| Solver | `solve_frekuensi.py` | Script yang dijalankan ulang |
| Report asli | `flags/misc/Frekuensi_Sunyi.report.txt` | Catatan + submit log +460 |