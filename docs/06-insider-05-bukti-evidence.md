# insider — Evidence / Bukti

<div class="nx-challenge-head"><span class="nx-chip">3 screenshot</span><span class="nx-chip">23 transkrip / script</span></div>


[← Overview](06-insider.md) · [Index](index.md)


## Arsip Evidence

> Semua file di bawah berasal dari folder `assets/insider/`. Screenshot ditempel langsung; file teks/script ditautkan.

### Screenshot

<div class="nx-evidence-grid">
<figure><a href="assets/insider/98-terminal-evidence.png" target="_blank" rel="noopener"><img src="assets/insider/98-terminal-evidence.png" alt="98-terminal-evidence.png" loading="lazy"></a><figcaption>98-terminal-evidence.png</figcaption></figure>
<figure><a href="assets/insider/ChromeProfile/Default/Extensions/ghbmnnjooekpmoecnnnilnnbdlolhkhi/1.92.1_0/icon128.png" target="_blank" rel="noopener"><img src="assets/insider/ChromeProfile/Default/Extensions/ghbmnnjooekpmoecnnnilnnbdlolhkhi/1.92.1_0/icon128.png" alt="icon128.png" loading="lazy"></a><figcaption>icon128.png</figcaption></figure>
<figure><a href="assets/insider/ChromeProfile/Default/Extensions/mgndgikekgjfcpckkfioiaebcgkldpdb/2.7.1_0/icon128.png" target="_blank" rel="noopener"><img src="assets/insider/ChromeProfile/Default/Extensions/mgndgikekgjfcpckkfioiaebcgkldpdb/2.7.1_0/icon128.png" alt="icon128.png" loading="lazy"></a><figcaption>icon128.png</figcaption></figure>
</div>

### Transkrip / file pendukung

- [`00-acquisition-note.txt`](assets/insider/00-acquisition-note.txt)
- [`01-evidence.tar.gz`](assets/insider/01-evidence.tar.gz)
- [`02-artifact-dump.txt`](assets/insider/02-artifact-dump.txt)
- [`03-acquisition-hashes.txt`](assets/insider/03-acquisition-hashes.txt)
- [`04-extensions-bookmarks.txt`](assets/insider/04-extensions-bookmarks.txt)
- [`05-timeline-flag.txt`](assets/insider/05-timeline-flag.txt)
- [`Bookmarks`](assets/insider/ChromeProfile/Default/Bookmarks)
- [`messages.json`](assets/insider/ChromeProfile/Default/Extensions/ghbmnnjooekpmoecnnnilnnbdlolhkhi/1.92.1_0/_locales/en/messages.json)
- [`background.js`](assets/insider/ChromeProfile/Default/Extensions/ghbmnnjooekpmoecnnnilnnbdlolhkhi/1.92.1_0/background.js)
- [`manifest.json`](assets/insider/ChromeProfile/Default/Extensions/ghbmnnjooekpmoecnnnilnnbdlolhkhi/1.92.1_0/manifest.json)
- [`messages.json`](assets/insider/ChromeProfile/Default/Extensions/mgndgikekgjfcpckkfioiaebcgkldpdb/2.7.1_0/_locales/en/messages.json)
- [`background.js`](assets/insider/ChromeProfile/Default/Extensions/mgndgikekgjfcpckkfioiaebcgkldpdb/2.7.1_0/background.js)
- [`manifest.json`](assets/insider/ChromeProfile/Default/Extensions/mgndgikekgjfcpckkfioiaebcgkldpdb/2.7.1_0/manifest.json)
- [`popup.html`](assets/insider/ChromeProfile/Default/Extensions/mgndgikekgjfcpckkfioiaebcgkldpdb/2.7.1_0/popup.html)
- [`History`](assets/insider/ChromeProfile/Default/History)
- [`Login Data`](assets/insider/ChromeProfile/Default/Login Data)
- [`Cookies`](assets/insider/ChromeProfile/Default/Network/Cookies)
- [`Preferences`](assets/insider/ChromeProfile/Default/Preferences)
- [`Secure Preferences`](assets/insider/ChromeProfile/Default/Secure Preferences)
- [`Web Data`](assets/insider/ChromeProfile/Default/Web Data)
- [`First Run`](assets/insider/ChromeProfile/First Run)
- [`Local State`](assets/insider/ChromeProfile/Local State)
- [`dump_insider.py`](assets/insider/dump_insider.py)

## Tabel Evidence

| Bukti | File | Keterangan |
|---|---|---|
| Attachment | `assets/insider/01-evidence.tar.gz` | tar.gz asli |
| Acquisition note | `assets/insider/00-acquisition-note.txt` | metadata penyitaan |
| Dump artefak | `assets/insider/02-artifact-dump.txt` | History, Login Data, Cookies, Web Data |
| Hash & listing | `assets/insider/03-acquisition-hashes.txt` | sha256 + tar listing |
| Extension | `assets/insider/04-extensions-bookmarks.txt` | ZenVPN + Bookmarks |
| Timeline | `assets/insider/05-timeline-flag.txt` | konversi timestamp |
| Profil Chrome | `assets/insider/ChromeProfile/` | artefak asli |
| Script | `assets/insider/dump_insider.py` | query SQLite |