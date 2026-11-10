# Career Tempat Belajar — Evidence / Bukti

<div class="nx-challenge-head"><span class="nx-chip">7 screenshot</span><span class="nx-chip">4 transkrip / script</span></div>


[← Overview](09-career-tempat-belajar.md) · [Index](index.md)

> **Langkah 7/8 — Bukti / Evidence.** Semua bukti berada di writeups/assets/career-tempat-belajar/.
>
> **Titik penting:** arsip screenshot dan transkrip
>
> **Berikutnya:** [Referensi](09-career-tempat-belajar-08-referensi.md)


## Arsip Evidence

> Semua file berasal dari `assets/career-tempat-belajar/`. Screenshot platform dan terminal adalah bukti asli dari sesi solve; transkrip mentah tetap ditautkan di bagian bawah.

### Platform

<div class="nx-evidence-grid">
<figure><a href="assets/career-tempat-belajar/00-challenge-platform.png" target="_blank" rel="noopener"><img src="assets/career-tempat-belajar/00-challenge-platform.png" alt="00-challenge-platform.png" loading="lazy"></a><figcaption>00-challenge-platform.png</figcaption></figure>
</div>

*Challenge brief asli di platform NFX CTF 2026.*

<div class="nx-evidence-grid">
<figure><a href="assets/career-tempat-belajar/00b-submit-platform.png" target="_blank" rel="noopener"><img src="assets/career-tempat-belajar/00b-submit-platform.png" alt="00b-submit-platform.png" loading="lazy"></a><figcaption>00b-submit-platform.png</figcaption></figure>
</div>

*Submit flag di platform: `CORRECT, BUT ALREADY SOLVED.`*

### Terminal (arsip sesi)

<div class="nx-evidence-grid">
<figure><a href="assets/career-tempat-belajar/term-02-office-metadata.png" target="_blank" rel="noopener"><img src="assets/career-tempat-belajar/term-02-office-metadata.png" alt="term-02-office-metadata.png" loading="lazy"></a><figcaption>term-02-office-metadata.png</figcaption></figure>
</div>

*Terminal evidence — `02-office-metadata.txt` (arsip transkrip sesi solve).*

<div class="nx-evidence-grid">
<figure><a href="assets/career-tempat-belajar/term-05-md5-derivation.png" target="_blank" rel="noopener"><img src="assets/career-tempat-belajar/term-05-md5-derivation.png" alt="term-05-md5-derivation.png" loading="lazy"></a><figcaption>term-05-md5-derivation.png</figcaption></figure>
</div>

*Terminal evidence — `05-md5-derivation.txt` (arsip transkrip sesi solve).*

<div class="nx-evidence-grid">
<figure><a href="assets/career-tempat-belajar/term-06-gravatar-http.png" target="_blank" rel="noopener"><img src="assets/career-tempat-belajar/term-06-gravatar-http.png" alt="term-06-gravatar-http.png" loading="lazy"></a><figcaption>term-06-gravatar-http.png</figcaption></figure>
</div>

*Terminal evidence — `06-gravatar-http.txt` (arsip transkrip sesi solve).*

### Screenshot langkah

<div class="nx-evidence-grid">
<figure><a href="assets/career-tempat-belajar/01-office.png" target="_blank" rel="noopener"><img src="assets/career-tempat-belajar/01-office.png" alt="01-office.png" loading="lazy"></a><figcaption>01-office.png</figcaption></figure>
</div>

*Evidence — `01-office.png`.*

<div class="nx-evidence-grid">
<figure><a href="assets/career-tempat-belajar/04-gravatar-avatar.png" target="_blank" rel="noopener"><img src="assets/career-tempat-belajar/04-gravatar-avatar.png" alt="04-gravatar-avatar.png" loading="lazy"></a><figcaption>04-gravatar-avatar.png</figcaption></figure>
</div>

*Evidence — `04-gravatar-avatar.png`.*

### Transkrip mentah & script

- [`02-office-metadata.txt`](assets/career-tempat-belajar/02-office-metadata.txt)
- [`03-gravatar-profile.json`](assets/career-tempat-belajar/03-gravatar-profile.json)
- [`05-md5-derivation.txt`](assets/career-tempat-belajar/05-md5-derivation.txt)
- [`06-gravatar-http.txt`](assets/career-tempat-belajar/06-gravatar-http.txt)

## Tabel Evidence

Semua bukti berada di `writeups/assets/career-tempat-belajar/`.

| Bukti | File | Keterangan |
|---|---|---|
| Poster asli | `01-office.png` | Gambar challenge, 1824×2346 |
| Metadata PNG | `02-office-metadata.txt` | `Author: Kada`, `Title: Dih Office`, `Comment` decoy |
| Profil Gravatar | `03-gravatar-profile.json` | Respons JSON live, berisi flag |
| Avatar Gravatar | `04-gravatar-avatar.png` | Avatar publik dari hash yang sama |
| Derivasi MD5 | `05-md5-derivation.txt` | Email → hash |
| HTTP Gravatar | `06-gravatar-http.txt` | Header + body respons |