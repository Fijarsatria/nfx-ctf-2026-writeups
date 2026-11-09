# Frekuensi Sunyi — Evidence / Bukti

<div class="nx-challenge-head"><span class="nx-chip">4 screenshot</span><span class="nx-chip">2 transkrip / script</span></div>


[← Overview](08-frekuensi-sunyi.md) · [Index](index.md)


## Arsip Evidence

> Semua file di bawah berasal dari folder `assets/frekuensi-sunyi/`. Screenshot ditempel langsung; file teks/script ditautkan.

### Screenshot

<div class="nx-evidence-grid">
<figure><a href="assets/frekuensi-sunyi/00-provided-spectrogram.png" target="_blank" rel="noopener"><img src="assets/frekuensi-sunyi/00-provided-spectrogram.png" alt="00-provided-spectrogram.png" loading="lazy"></a><figcaption>00-provided-spectrogram.png</figcaption></figure>
<figure><a href="assets/frekuensi-sunyi/01-spectrogram-repro.png" target="_blank" rel="noopener"><img src="assets/frekuensi-sunyi/01-spectrogram-repro.png" alt="01-spectrogram-repro.png" loading="lazy"></a><figcaption>01-spectrogram-repro.png</figcaption></figure>
<figure><a href="assets/frekuensi-sunyi/04-text-crop.png" target="_blank" rel="noopener"><img src="assets/frekuensi-sunyi/04-text-crop.png" alt="04-text-crop.png" loading="lazy"></a><figcaption>04-text-crop.png</figcaption></figure>
<figure><a href="assets/frekuensi-sunyi/98-terminal-evidence.png" target="_blank" rel="noopener"><img src="assets/frekuensi-sunyi/98-terminal-evidence.png" alt="98-terminal-evidence.png" loading="lazy"></a><figcaption>98-terminal-evidence.png</figcaption></figure>
</div>

### Transkrip / file pendukung

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