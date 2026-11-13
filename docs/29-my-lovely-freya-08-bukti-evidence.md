# My Lovely Freya — Evidence / Bukti

<div class="nx-challenge-head"><span class="nx-chip">6 screenshot</span><span class="nx-chip">5 transkrip / script</span></div>


[← Overview](29-my-lovely-freya.md) · [Index](index.md)

> **Langkah 8/9 — Bukti / Evidence.** Semua bukti berada di docs/assets/my-lovely-freya/.
>
> **Titik penting:** arsip screenshot dan transkrip
>
> **Berikutnya:** [Referensi](29-my-lovely-freya-09-referensi.md)


## Arsip Evidence

> Semua file berasal dari `assets/my-lovely-freya/`. Screenshot platform dan terminal adalah bukti asli dari sesi solve; transkrip mentah tetap ditautkan di bagian bawah.

### Platform

<div class="nx-evidence-grid">
<figure><a href="assets/my-lovely-freya/00-challenge-platform.png" target="_blank" rel="noopener"><img src="assets/my-lovely-freya/00-challenge-platform.png" alt="00-challenge-platform.png" loading="lazy"></a><figcaption>00-challenge-platform.png</figcaption></figure>
</div>

*Challenge brief asli di platform NFX CTF 2026.*

<div class="nx-evidence-grid">
<figure><a href="assets/my-lovely-freya/00b-terminal-evidence.png" target="_blank" rel="noopener"><img src="assets/my-lovely-freya/00b-terminal-evidence.png" alt="Terminal evidence (real)" loading="lazy"></a><figcaption>Terminal evidence (real)</figcaption></figure>
</div>

*Terminal evidence (real).*

### Terminal (arsip sesi)

<div class="nx-evidence-grid">
<figure><a href="assets/my-lovely-freya/term-02-hidden-extraction.png" target="_blank" rel="noopener"><img src="assets/my-lovely-freya/term-02-hidden-extraction.png" alt="term-02-hidden-extraction.png" loading="lazy"></a><figcaption>term-02-hidden-extraction.png</figcaption></figure>
</div>

*Terminal evidence — `02-hidden-extraction.txt` (arsip transkrip sesi solve).*

<div class="nx-evidence-grid">
<figure><a href="assets/my-lovely-freya/term-03-surat-decrypted.png" target="_blank" rel="noopener"><img src="assets/my-lovely-freya/term-03-surat-decrypted.png" alt="term-03-surat-decrypted.png" loading="lazy"></a><figcaption>term-03-surat-decrypted.png</figcaption></figure>
</div>

*Terminal evidence — `03-surat-decrypted.txt` (arsip transkrip sesi solve).*

<div class="nx-evidence-grid">
<figure><a href="assets/my-lovely-freya/term-04-decrypt-output.png" target="_blank" rel="noopener"><img src="assets/my-lovely-freya/term-04-decrypt-output.png" alt="term-04-decrypt-output.png" loading="lazy"></a><figcaption>term-04-decrypt-output.png</figcaption></figure>
</div>

*Terminal evidence — `04-decrypt-output.txt` (arsip transkrip sesi solve).*

### Screenshot langkah

<div class="nx-evidence-grid">
<figure><a href="assets/my-lovely-freya/01-hidden-rows.png" target="_blank" rel="noopener"><img src="assets/my-lovely-freya/01-hidden-rows.png" alt="01-hidden-rows.png" loading="lazy"></a><figcaption>01-hidden-rows.png</figcaption></figure>
</div>

*Evidence — `01-hidden-rows.png`.*

### Transkrip mentah & script

- [`02-hidden-extraction.txt`](assets/my-lovely-freya/02-hidden-extraction.txt)
- [`03-surat-decrypted.txt`](assets/my-lovely-freya/03-surat-decrypted.txt)
- [`04-decrypt-output.txt`](assets/my-lovely-freya/04-decrypt-output.txt)
- [`decrypt_surat.sh`](assets/my-lovely-freya/decrypt_surat.sh)
- [`extract_hidden.py`](assets/my-lovely-freya/extract_hidden.py)

## Validasi platform (real)

![Validasi platform — CORRECT, BUT ALREADY SOLVED.](assets/my-lovely-freya/00b-platform-validation.png)

*Screenshot asli dari platform NFX CTF 2026. Platform menjawab
`CORRECT, BUT ALREADY SOLVED.` untuk flag ini.*


## Tabel Evidence

Semua bukti berada di `docs/assets/my-lovely-freya/`.

| Bukti | File | Keterangan |
|---|---|---|
| Baris tersembunyi | `01-hidden-rows.png` | 1024x336 gambar hasil baris 1200–1535 |
| Analisis PNG | `02-hidden-extraction.txt` | IHDR, jumlah baris, hash, metadata, base64 decode |
| Surat terdekripsi | `03-surat-decrypted.txt` | Plaintext `NXCTF{...}` |
| Log dekripsi | `04-decrypt-output.txt` | `xxd`, openssl, plaintext, decoy gagal |
| Ekstraktor | `extract_hidden.py` | Decoder PNG + unfilter + render baris ekstra |
| Dekriptor | `decrypt_surat.sh` | Command openssl yang dipakai |