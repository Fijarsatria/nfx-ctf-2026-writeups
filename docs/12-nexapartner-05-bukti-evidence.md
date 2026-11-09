# NexaPartner — Evidence / Bukti

<div class="nx-challenge-head"><span class="nx-chip">2 screenshot</span><span class="nx-chip">5 transkrip / script</span></div>


[← Overview](12-nexapartner.md) · [Index](index.md)


## Arsip Evidence

> Semua file di bawah berasal dari folder `assets/nexapartner/`. Screenshot ditempel langsung; file teks/script ditautkan.

### Screenshot

<div class="nx-evidence-grid">
<figure><a href="assets/nexapartner/01-admin-audit-flag.png" target="_blank" rel="noopener"><img src="assets/nexapartner/01-admin-audit-flag.png" alt="01-admin-audit-flag.png" loading="lazy"></a><figcaption>01-admin-audit-flag.png</figcaption></figure>
<figure><a href="assets/nexapartner/98-terminal-evidence.png" target="_blank" rel="noopener"><img src="assets/nexapartner/98-terminal-evidence.png" alt="98-terminal-evidence.png" loading="lazy"></a><figcaption>98-terminal-evidence.png</figcaption></figure>
</div>

### Transkrip / file pendukung

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