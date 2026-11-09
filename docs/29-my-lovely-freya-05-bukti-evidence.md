# My Lovely Freya — Evidence / Bukti

<div class="nx-challenge-head"><span class="nx-chip">2 screenshot</span><span class="nx-chip">5 transkrip / script</span></div>


[← Overview](29-my-lovely-freya.md) · [Index](index.md)


## Arsip Evidence

> Semua file di bawah berasal dari folder `assets/my-lovely-freya/`. Screenshot ditempel langsung; file teks/script ditautkan.

### Screenshot

<div class="nx-evidence-grid">
<figure><a href="assets/my-lovely-freya/01-hidden-rows.png" target="_blank" rel="noopener"><img src="assets/my-lovely-freya/01-hidden-rows.png" alt="01-hidden-rows.png" loading="lazy"></a><figcaption>01-hidden-rows.png</figcaption></figure>
<figure><a href="assets/my-lovely-freya/98-terminal-evidence.png" target="_blank" rel="noopener"><img src="assets/my-lovely-freya/98-terminal-evidence.png" alt="98-terminal-evidence.png" loading="lazy"></a><figcaption>98-terminal-evidence.png</figcaption></figure>
</div>

### Transkrip / file pendukung

- [`02-hidden-extraction.txt`](assets/my-lovely-freya/02-hidden-extraction.txt)
- [`03-surat-decrypted.txt`](assets/my-lovely-freya/03-surat-decrypted.txt)
- [`04-decrypt-output.txt`](assets/my-lovely-freya/04-decrypt-output.txt)
- [`decrypt_surat.sh`](assets/my-lovely-freya/decrypt_surat.sh)
- [`extract_hidden.py`](assets/my-lovely-freya/extract_hidden.py)

## Tabel Evidence

Semua bukti berada di `writeups/assets/my-lovely-freya/`.

| Bukti | File | Keterangan |
|---|---|---|
| Baris tersembunyi | `01-hidden-rows.png` | 1024x336 gambar hasil baris 1200–1535 |
| Analisis PNG | `02-hidden-extraction.txt` | IHDR, jumlah baris, hash, metadata, base64 decode |
| Surat terdekripsi | `03-surat-decrypted.txt` | Plaintext `NXCTF{...}` |
| Log dekripsi | `04-decrypt-output.txt` | `xxd`, openssl, plaintext, decoy gagal |
| Ekstraktor | `extract_hidden.py` | Decoder PNG + unfilter + render baris ekstra |
| Dekriptor | `decrypt_surat.sh` | Command openssl yang dipakai |