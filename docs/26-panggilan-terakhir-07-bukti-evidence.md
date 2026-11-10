# Panggilan Terakhir — Evidence / Bukti

<div class="nx-challenge-head"><span class="nx-chip">8 screenshot</span><span class="nx-chip">10 transkrip / script</span></div>


[← Overview](26-panggilan-terakhir.md) · [Index](index.md)

> **Langkah 7/8 — Bukti / Evidence.** Bukti / Evidence
>
> **Titik penting:** arsip screenshot dan transkrip
>
> **Berikutnya:** [Referensi](26-panggilan-terakhir-08-referensi.md)


## Arsip Evidence

> Semua file berasal dari `assets/panggilan-terakhir/`. Screenshot platform dan terminal adalah bukti asli dari sesi solve; transkrip mentah tetap ditautkan di bagian bawah.

### Platform

<div class="nx-evidence-grid">
<figure><a href="assets/panggilan-terakhir/00-challenge-platform.png" target="_blank" rel="noopener"><img src="assets/panggilan-terakhir/00-challenge-platform.png" alt="00-challenge-platform.png" loading="lazy"></a><figcaption>00-challenge-platform.png</figcaption></figure>
</div>

*Challenge brief asli di platform NFX CTF 2026.*

<div class="nx-evidence-grid">
<figure><a href="assets/panggilan-terakhir/00b-submit-platform.png" target="_blank" rel="noopener"><img src="assets/panggilan-terakhir/00b-submit-platform.png" alt="00b-submit-platform.png" loading="lazy"></a><figcaption>00b-submit-platform.png</figcaption></figure>
</div>

*Submit flag di platform: `CORRECT, BUT ALREADY SOLVED.`*

### Terminal (arsip sesi)

<div class="nx-evidence-grid">
<figure><a href="assets/panggilan-terakhir/term-00-pcap-summary.png" target="_blank" rel="noopener"><img src="assets/panggilan-terakhir/term-00-pcap-summary.png" alt="term-00-pcap-summary.png" loading="lazy"></a><figcaption>term-00-pcap-summary.png</figcaption></figure>
</div>

*Terminal evidence — `00-pcap-summary.txt` (arsip transkrip sesi solve).*

<div class="nx-evidence-grid">
<figure><a href="assets/panggilan-terakhir/term-01-sip-dialog.png" target="_blank" rel="noopener"><img src="assets/panggilan-terakhir/term-01-sip-dialog.png" alt="term-01-sip-dialog.png" loading="lazy"></a><figcaption>term-01-sip-dialog.png</figcaption></figure>
</div>

*Terminal evidence — `01-sip-dialog.txt` (arsip transkrip sesi solve).*

<div class="nx-evidence-grid">
<figure><a href="assets/panggilan-terakhir/term-05-rtp-extract.png" target="_blank" rel="noopener"><img src="assets/panggilan-terakhir/term-05-rtp-extract.png" alt="term-05-rtp-extract.png" loading="lazy"></a><figcaption>term-05-rtp-extract.png</figcaption></figure>
</div>

*Terminal evidence — `05-rtp-extract.txt` (arsip transkrip sesi solve).*

<div class="nx-evidence-grid">
<figure><a href="assets/panggilan-terakhir/term-06-transcript.png" target="_blank" rel="noopener"><img src="assets/panggilan-terakhir/term-06-transcript.png" alt="term-06-transcript.png" loading="lazy"></a><figcaption>term-06-transcript.png</figcaption></figure>
</div>

*Terminal evidence — `06-transcript.txt` (arsip transkrip sesi solve).*

### Screenshot langkah

<div class="nx-evidence-grid">
<figure><a href="assets/panggilan-terakhir/03-spectrogram-Dina.png" target="_blank" rel="noopener"><img src="assets/panggilan-terakhir/03-spectrogram-Dina.png" alt="03-spectrogram-Dina.png" loading="lazy"></a><figcaption>03-spectrogram-Dina.png</figcaption></figure>
</div>

*Evidence — `03-spectrogram-Dina.png`.*

<div class="nx-evidence-grid">
<figure><a href="assets/panggilan-terakhir/04-spectrogram-Raka.png" target="_blank" rel="noopener"><img src="assets/panggilan-terakhir/04-spectrogram-Raka.png" alt="04-spectrogram-Raka.png" loading="lazy"></a><figcaption>04-spectrogram-Raka.png</figcaption></figure>
</div>

*Evidence — `04-spectrogram-Raka.png`.*

### Transkrip mentah & script

- [`00-pcap-summary.txt`](assets/panggilan-terakhir/00-pcap-summary.txt)
- [`01-Raka-204.wav`](assets/panggilan-terakhir/01-Raka-204.wav)
- [`01-sip-dialog.txt`](assets/panggilan-terakhir/01-sip-dialog.txt)
- [`02-Dina-231.wav`](assets/panggilan-terakhir/02-Dina-231.wav)
- [`05-rtp-extract.txt`](assets/panggilan-terakhir/05-rtp-extract.txt)
- [`06-transcript.txt`](assets/panggilan-terakhir/06-transcript.txt)
- [`korban.pcap`](assets/panggilan-terakhir/korban.pcap)
- [`pt_4000_4002_a2040001.wav`](assets/panggilan-terakhir/pt_4000_4002_a2040001.wav)
- [`pt_4002_4000_b2310001.wav`](assets/panggilan-terakhir/pt_4002_4000_b2310001.wav)
- [`solve_panggilan.py`](assets/panggilan-terakhir/solve_panggilan.py)

## Tabel Evidence

| Bukti | File | Keterangan |
|---|---|---|
| PCAP | `assets/panggilan-terakhir/korban.pcap` | capture asli |
| Ringkasan | `assets/panggilan-terakhir/00-pcap-summary.txt` | file/hash/tcpdump/flow |
| SIP | `assets/panggilan-terakhir/01-sip-dialog.txt` | INVITE/200/ACK/BYE + SDP |
| RTP extract | `assets/panggilan-terakhir/05-rtp-extract.txt` | output script |
| Audio Raka | `assets/panggilan-terakhir/01-Raka-204.wav` | 21,02 detik |
| Audio Dina | `assets/panggilan-terakhir/02-Dina-231.wav` | 47,48 detik |
| Spectrogram Dina | `assets/panggilan-terakhir/03-spectrogram-Dina.png` | visual audio |
| Spectrogram Raka | `assets/panggilan-terakhir/04-spectrogram-Raka.png` | visual audio |
| Transkrip | `assets/panggilan-terakhir/06-transcript.txt` | ASR + interpretasi |
| Script | `assets/panggilan-terakhir/solve_panggilan.py` | ekstraksi RTP |