# NexaPartner — Evidence / Bukti

<div class="nx-challenge-head"><span class="nx-chip">6 screenshot</span><span class="nx-chip">5 transkrip / script</span></div>


[← Overview](12-nexapartner.md) · [Index](index.md)


## Arsip Evidence

> Semua file berasal dari `assets/nexapartner/`. Screenshot platform dan terminal adalah bukti asli dari sesi solve; transkrip mentah tetap ditautkan di bagian bawah.

### Platform

<div class="nx-evidence-grid">
<figure><a href="assets/nexapartner/00-challenge-platform.png" target="_blank" rel="noopener"><img src="assets/nexapartner/00-challenge-platform.png" alt="00-challenge-platform.png" loading="lazy"></a><figcaption>00-challenge-platform.png</figcaption></figure>
</div>

*Challenge brief asli di platform NFX CTF 2026.*

<div class="nx-evidence-grid">
<figure><a href="assets/nexapartner/00b-submit-platform.png" target="_blank" rel="noopener"><img src="assets/nexapartner/00b-submit-platform.png" alt="00b-submit-platform.png" loading="lazy"></a><figcaption>00b-submit-platform.png</figcaption></figure>
</div>

*Submit flag di platform: `CORRECT, BUT ALREADY SOLVED.`*

### Terminal (arsip sesi)

<div class="nx-evidence-grid">
<figure><a href="assets/nexapartner/term-01-recon.png" target="_blank" rel="noopener"><img src="assets/nexapartner/term-01-recon.png" alt="term-01-recon.png" loading="lazy"></a><figcaption>term-01-recon.png</figcaption></figure>
</div>

*Terminal evidence — `01-recon.txt` (arsip transkrip sesi solve).*

<div class="nx-evidence-grid">
<figure><a href="assets/nexapartner/term-02-authed-crawl.png" target="_blank" rel="noopener"><img src="assets/nexapartner/term-02-authed-crawl.png" alt="term-02-authed-crawl.png" loading="lazy"></a><figcaption>term-02-authed-crawl.png</figcaption></figure>
</div>

*Terminal evidence — `02-authed-crawl.txt` (arsip transkrip sesi solve).*

<div class="nx-evidence-grid">
<figure><a href="assets/nexapartner/term-03-exploit-evidence.png" target="_blank" rel="noopener"><img src="assets/nexapartner/term-03-exploit-evidence.png" alt="term-03-exploit-evidence.png" loading="lazy"></a><figcaption>term-03-exploit-evidence.png</figcaption></figure>
</div>

*Terminal evidence — `03-exploit-evidence.txt` (arsip transkrip sesi solve).*

### Screenshot langkah

<div class="nx-evidence-grid">
<figure><a href="assets/nexapartner/01-admin-audit-flag.png" target="_blank" rel="noopener"><img src="assets/nexapartner/01-admin-audit-flag.png" alt="01-admin-audit-flag.png" loading="lazy"></a><figcaption>01-admin-audit-flag.png</figcaption></figure>
</div>

*Evidence — `01-admin-audit-flag.png`.*

### Transkrip mentah & script

- [`01-recon.txt`](assets/nexapartner/01-recon.txt)
- [`02-authed-crawl.txt`](assets/nexapartner/02-authed-crawl.txt)
- [`03-exploit-evidence.txt`](assets/nexapartner/03-exploit-evidence.txt)
- [`admin-audit.html`](assets/nexapartner/admin-audit.html)
- [`exploit_nexapartner.py`](assets/nexapartner/exploit_nexapartner.py)

## Tabel Evidence

| Bukti | File | Keterangan |
|---|---|---|
| Recon | `assets/nexapartner/01-recon.txt` | Landing, login, demo account |
| Crawl auth | `assets/nexapartner/02-authed-crawl.txt` | Dashboard, settings, api-docs, `/admin` 403 |
| Exploit evidence | `assets/nexapartner/03-exploit-evidence.txt` | `/admin` 302, audit + flag, payload |
| Admin audit HTML | `assets/nexapartner/admin-audit.html` | Flag di tabel dan recovery token |
| Screenshot | `assets/nexapartner/01-admin-audit-flag.png` | `/admin/audit` menampilkan recovery token |
| Exploit | `assets/nexapartner/exploit_nexapartner.py` | Script reproduksi |
| Hash/flag | `flags/web/07_nexapartner.txt` | Sumber flag |