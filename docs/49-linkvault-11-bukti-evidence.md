# LinkVault — Evidence / Bukti

<div class="nx-challenge-head"><span class="nx-chip">7 screenshot</span><span class="nx-chip">8 transkrip / script</span></div>


[← Overview](49-linkvault.md) · [Index](index.md)

> **Langkah 11/12 — Bukti / Evidence.** Bukti / Evidence
>
> **Titik penting:** arsip screenshot dan transkrip
>
> **Berikutnya:** [Referensi](49-linkvault-12-referensi.md)


## Arsip Evidence

> Semua file berasal dari `assets/linkvault/`. Screenshot platform dan terminal adalah bukti asli dari sesi solve; transkrip mentah tetap ditautkan di bagian bawah.

### Platform

<div class="nx-evidence-grid">
<figure><a href="assets/linkvault/00-challenge-platform.png" target="_blank" rel="noopener"><img src="assets/linkvault/00-challenge-platform.png" alt="00-challenge-platform.png" loading="lazy"></a><figcaption>00-challenge-platform.png</figcaption></figure>
</div>

*Challenge brief asli di platform NFX CTF 2026.*

<div class="nx-evidence-grid">
<figure><a href="assets/linkvault/00b-terminal-evidence.png" target="_blank" rel="noopener"><img src="assets/linkvault/00b-terminal-evidence.png" alt="Terminal evidence (real)" loading="lazy"></a><figcaption>Terminal evidence (real)</figcaption></figure>
</div>

*Terminal evidence (real).*

### Terminal (arsip sesi)

<div class="nx-evidence-grid">
<figure><a href="assets/linkvault/term-01-recon.png" target="_blank" rel="noopener"><img src="assets/linkvault/term-01-recon.png" alt="term-01-recon.png" loading="lazy"></a><figcaption>term-01-recon.png</figcaption></figure>
</div>

*Terminal evidence — `01-recon.txt` (arsip transkrip sesi solve).*

<div class="nx-evidence-grid">
<figure><a href="assets/linkvault/term-02-exploit-run.png" target="_blank" rel="noopener"><img src="assets/linkvault/term-02-exploit-run.png" alt="term-02-exploit-run.png" loading="lazy"></a><figcaption>term-02-exploit-run.png</figcaption></figure>
</div>

*Terminal evidence — `02-exploit-run.txt` (arsip transkrip sesi solve).*

<div class="nx-evidence-grid">
<figure><a href="assets/linkvault/term-03-ssrf-evidence.png" target="_blank" rel="noopener"><img src="assets/linkvault/term-03-ssrf-evidence.png" alt="term-03-ssrf-evidence.png" loading="lazy"></a><figcaption>term-03-ssrf-evidence.png</figcaption></figure>
</div>

*Terminal evidence — `03-ssrf-evidence.txt` (arsip transkrip sesi solve).*

<div class="nx-evidence-grid">
<figure><a href="assets/linkvault/term-source-notes.png" target="_blank" rel="noopener"><img src="assets/linkvault/term-source-notes.png" alt="term-source-notes.png" loading="lazy"></a><figcaption>term-source-notes.png</figcaption></figure>
</div>

*Terminal evidence — `source-notes.txt` (arsip transkrip sesi solve).*

### Screenshot langkah

<div class="nx-evidence-grid">
<figure><a href="assets/linkvault/01-reports-flag.png" target="_blank" rel="noopener"><img src="assets/linkvault/01-reports-flag.png" alt="01-reports-flag.png" loading="lazy"></a><figcaption>01-reports-flag.png</figcaption></figure>
</div>

*Evidence — `01-reports-flag.png`.*

### Transkrip mentah & script

- [`01-recon.txt`](assets/linkvault/01-recon.txt)
- [`02-exploit-run.txt`](assets/linkvault/02-exploit-run.txt)
- [`03-ssrf-evidence.py`](assets/linkvault/03-ssrf-evidence.py)
- [`03-ssrf-evidence.txt`](assets/linkvault/03-ssrf-evidence.txt)
- [`03-ssrf-submit-response.html`](assets/linkvault/03-ssrf-submit-response.html)
- [`05-reports-with-flag.html`](assets/linkvault/05-reports-with-flag.html)
- [`exploit_linkvault.py`](assets/linkvault/exploit_linkvault.py)
- [`source-notes.txt`](assets/linkvault/source-notes.txt)

## Tabel Evidence

| Bukti | File | Keterangan |
|---|---|---|
| Recon awal | `assets/linkvault/01-recon.txt` | `GET /`, `/login`, `/health` |
| Transcript exploit | `assets/linkvault/02-exploit-run.txt` | Register, SSRF, XSS, flag setelah 32s |
| Bukti SSRF | `assets/linkvault/03-ssrf-evidence.txt` | Kontrol `127.0.0.1` ditolak, `[::1]` diterima |
| Respons SSRF | `assets/linkvault/03-ssrf-submit-response.html` | `{"ok":true,"queued":true,"source":"crawler"}` |
| Inbox flag | `assets/linkvault/05-reports-with-flag.html` | `/reports` berisi flag |
| Screenshot | `assets/linkvault/01-reports-flag.png` | `/reports` menampilkan `{"flag":"NFX{...}"}` |
| Source snippet | `assets/linkvault/source-notes.txt` | `guardedFetch`, internal API, template, bot |
| Exploit | `assets/linkvault/exploit_linkvault.py` | Script lengkap |
| Hash source | lihat §1.2 | SHA-256 file source |