# Record Keeper (User) — Evidence / Bukti

<div class="nx-challenge-head"><span class="nx-chip">7 screenshot</span><span class="nx-chip">5 transkrip / script</span></div>


[← Overview](17-record-keeper-user.md) · [Index](index.md)


## Arsip Evidence

> Semua file berasal dari `assets/record-keeper-user/`. Screenshot platform dan terminal adalah bukti asli dari sesi solve; transkrip mentah tetap ditautkan di bagian bawah.

### Platform

<div class="nx-evidence-grid">
<figure><a href="assets/record-keeper-user/00-challenge-platform.png" target="_blank" rel="noopener"><img src="assets/record-keeper-user/00-challenge-platform.png" alt="00-challenge-platform.png" loading="lazy"></a><figcaption>00-challenge-platform.png</figcaption></figure>
</div>

*Challenge brief asli di platform NFX CTF 2026.*

<div class="nx-evidence-grid">
<figure><a href="assets/record-keeper-user/00b-submit-platform.png" target="_blank" rel="noopener"><img src="assets/record-keeper-user/00b-submit-platform.png" alt="00b-submit-platform.png" loading="lazy"></a><figcaption>00b-submit-platform.png</figcaption></figure>
</div>

*Submit flag di platform: `CORRECT, BUT ALREADY SOLVED.`*

### Terminal (arsip sesi)

<div class="nx-evidence-grid">
<figure><a href="assets/record-keeper-user/term-01-recon.png" target="_blank" rel="noopener"><img src="assets/record-keeper-user/term-01-recon.png" alt="term-01-recon.png" loading="lazy"></a><figcaption>term-01-recon.png</figcaption></figure>
</div>

*Terminal evidence — `01-recon.txt` (arsip transkrip sesi solve).*

<div class="nx-evidence-grid">
<figure><a href="assets/record-keeper-user/term-02-cve-2026-111497.png" target="_blank" rel="noopener"><img src="assets/record-keeper-user/term-02-cve-2026-111497.png" alt="term-02-cve-2026-111497.png" loading="lazy"></a><figcaption>term-02-cve-2026-111497.png</figcaption></figure>
</div>

*Terminal evidence — `02-cve-2026-111497.txt` (arsip transkrip sesi solve).*

<div class="nx-evidence-grid">
<figure><a href="assets/record-keeper-user/term-03-user-flag.png" target="_blank" rel="noopener"><img src="assets/record-keeper-user/term-03-user-flag.png" alt="term-03-user-flag.png" loading="lazy"></a><figcaption>term-03-user-flag.png</figcaption></figure>
</div>

*Terminal evidence — `03-user-flag.txt` (arsip transkrip sesi solve).*

<div class="nx-evidence-grid">
<figure><a href="assets/record-keeper-user/term-04-typo.png" target="_blank" rel="noopener"><img src="assets/record-keeper-user/term-04-typo.png" alt="term-04-typo.png" loading="lazy"></a><figcaption>term-04-typo.png</figcaption></figure>
</div>

*Terminal evidence — `04-typo.txt` (arsip transkrip sesi solve).*

<div class="nx-evidence-grid">
<figure><a href="assets/record-keeper-user/term-07-console-excerpt.png" target="_blank" rel="noopener"><img src="assets/record-keeper-user/term-07-console-excerpt.png" alt="term-07-console-excerpt.png" loading="lazy"></a><figcaption>term-07-console-excerpt.png</figcaption></figure>
</div>

*Terminal evidence — `07-console-excerpt.txt` (arsip transkrip sesi solve).*

### Transkrip mentah & script

- [`01-recon.txt`](assets/record-keeper-user/01-recon.txt)
- [`02-cve-2026-111497.txt`](assets/record-keeper-user/02-cve-2026-111497.txt)
- [`03-user-flag.txt`](assets/record-keeper-user/03-user-flag.txt)
- [`04-typo.txt`](assets/record-keeper-user/04-typo.txt)
- [`07-console-excerpt.txt`](assets/record-keeper-user/07-console-excerpt.txt)

## Tabel Evidence

| Bukti | File | Keterangan |
|---|---|---|
| Recon + protokol | `assets/record-keeper-user/01-recon.txt` | Service mesh, frame, PONG, Node 24.9.0 |
| CVE + exploit | `assets/record-keeper-user/02-cve-2026-111497.txt` | Mekanisme, profile, offset, command |
| User flag | `assets/record-keeper-user/03-user-flag.txt` | Flag, hash, base64, hex, mode |
| Typo + submit | `assets/record-keeper-user/04-typo.txt` | Nilai salah, nilai benar, submit log |
| Console | `assets/record-keeper-user/07-console-excerpt.txt` | Kutipan runtime, protokol, service mesh |
| Render CVE | `assets/record-keeper-user/05-cve.png` | Render penjelasan + flag |
| Render flag | `assets/record-keeper-user/06-flag.png` | Render flag + koreksi typo |