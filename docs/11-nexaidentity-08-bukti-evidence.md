# NexaIdentity — Evidence / Bukti

<div class="nx-challenge-head"><span class="nx-chip">8 screenshot</span><span class="nx-chip">10 transkrip / script</span></div>


[← Overview](11-nexaidentity.md) · [Index](index.md)

> **Langkah 8/9 — Bukti / Evidence.** Bukti / Evidence
>
> **Titik penting:** arsip screenshot dan transkrip
>
> **Berikutnya:** [Referensi](11-nexaidentity-09-referensi.md)


## Arsip Evidence

> Semua file berasal dari `assets/nexaidentity/`. Screenshot platform dan terminal adalah bukti asli dari sesi solve; transkrip mentah tetap ditautkan di bagian bawah.

### Platform

<div class="nx-evidence-grid">
<figure><a href="assets/nexaidentity/00-challenge-platform.png" target="_blank" rel="noopener"><img src="assets/nexaidentity/00-challenge-platform.png" alt="00-challenge-platform.png" loading="lazy"></a><figcaption>00-challenge-platform.png</figcaption></figure>
</div>

*Challenge brief asli di platform NFX CTF 2026.*

<div class="nx-evidence-grid">
<figure><a href="assets/nexaidentity/00b-submit-platform.png" target="_blank" rel="noopener"><img src="assets/nexaidentity/00b-submit-platform.png" alt="00b-submit-platform.png" loading="lazy"></a><figcaption>00b-submit-platform.png</figcaption></figure>
</div>

*Submit flag di platform: `CORRECT, BUT ALREADY SOLVED.`*

### Terminal (arsip sesi)

<div class="nx-evidence-grid">
<figure><a href="assets/nexaidentity/term-01-recon.png" target="_blank" rel="noopener"><img src="assets/nexaidentity/term-01-recon.png" alt="term-01-recon.png" loading="lazy"></a><figcaption>term-01-recon.png</figcaption></figure>
</div>

*Terminal evidence — `01-recon.txt` (arsip transkrip sesi solve).*

<div class="nx-evidence-grid">
<figure><a href="assets/nexaidentity/term-02-endpoints.png" target="_blank" rel="noopener"><img src="assets/nexaidentity/term-02-endpoints.png" alt="term-02-endpoints.png" loading="lazy"></a><figcaption>term-02-endpoints.png</figcaption></figure>
</div>

*Terminal evidence — `02-endpoints.txt` (arsip transkrip sesi solve).*

<div class="nx-evidence-grid">
<figure><a href="assets/nexaidentity/term-03-login-normal.png" target="_blank" rel="noopener"><img src="assets/nexaidentity/term-03-login-normal.png" alt="term-03-login-normal.png" loading="lazy"></a><figcaption>term-03-login-normal.png</figcaption></figure>
</div>

*Terminal evidence — `03-login-normal.txt` (arsip transkrip sesi solve).*

<div class="nx-evidence-grid">
<figure><a href="assets/nexaidentity/term-04-authed-pages.png" target="_blank" rel="noopener"><img src="assets/nexaidentity/term-04-authed-pages.png" alt="term-04-authed-pages.png" loading="lazy"></a><figcaption>term-04-authed-pages.png</figcaption></figure>
</div>

*Terminal evidence — `04-authed-pages.txt` (arsip transkrip sesi solve).*

<div class="nx-evidence-grid">
<figure><a href="assets/nexaidentity/term-05-nosql-form-tests.png" target="_blank" rel="noopener"><img src="assets/nexaidentity/term-05-nosql-form-tests.png" alt="term-05-nosql-form-tests.png" loading="lazy"></a><figcaption>term-05-nosql-form-tests.png</figcaption></figure>
</div>

*Terminal evidence — `05-nosql-form-tests.txt` (arsip transkrip sesi solve).*

### Screenshot langkah

<div class="nx-evidence-grid">
<figure><a href="assets/nexaidentity/01-admin-flag.png" target="_blank" rel="noopener"><img src="assets/nexaidentity/01-admin-flag.png" alt="01-admin-flag.png" loading="lazy"></a><figcaption>01-admin-flag.png</figcaption></figure>
</div>

*Evidence — `01-admin-flag.png`.*

### Transkrip mentah & script

- [`01-recon.txt`](assets/nexaidentity/01-recon.txt)
- [`02-endpoints.txt`](assets/nexaidentity/02-endpoints.txt)
- [`03-login-normal.txt`](assets/nexaidentity/03-login-normal.txt)
- [`04-authed-pages.txt`](assets/nexaidentity/04-authed-pages.txt)
- [`05-nosql-form-tests.txt`](assets/nexaidentity/05-nosql-form-tests.txt)
- [`admin-c_admin_regex.txt.html`](assets/nexaidentity/admin-c_admin_regex.txt.html)
- [`admin-c_json_ne.txt.html`](assets/nexaidentity/admin-c_json_ne.txt.html)
- [`admin-c_ne_both.txt.html`](assets/nexaidentity/admin-c_ne_both.txt.html)
- [`admin-flag.html`](assets/nexaidentity/admin-flag.html)
- [`exploit_nexaidentity.py`](assets/nexaidentity/exploit_nexaidentity.py)

## Tabel Evidence

| Bukti | File | Keterangan |
|---|---|---|
| Recon awal | `assets/nexaidentity/01-recon.txt` | Landing, login, demo account |
| Enumerasi endpoint | `assets/nexaidentity/02-endpoints.txt` | `/directory`, `/admin`, dll. |
| Login normal | `assets/nexaidentity/03-login-normal.txt` | Employee session |
| Halaman auth | `assets/nexaidentity/04-authed-pages.txt` | `/admin` 403, profil admin |
| Matriks NoSQL | `assets/nexaidentity/05-nosql-form-tests.txt` | Semua varian `$ne`/`$gt`/`$regex` |
| Admin + flag | `assets/nexaidentity/admin-flag.html` | Recovery token |
| Screenshot | `assets/nexaidentity/01-admin-flag.png` | Console admin sebagai Nadia Kusuma |
| Exploit | `assets/nexaidentity/exploit_nexaidentity.py` | Script reproduksi |
| Hash/flag | `flags/web/05_nexaidentity.txt` | Sumber flag |