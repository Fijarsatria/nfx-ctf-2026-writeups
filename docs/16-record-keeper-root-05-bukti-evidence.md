# Record Keeper (Root) — Evidence / Bukti

<div class="nx-challenge-head"><span class="nx-chip">3 screenshot</span><span class="nx-chip">5 transkrip / script</span></div>


[← Overview](16-record-keeper-root.md) · [Index](index.md)


## Arsip Evidence

> Semua file di bawah berasal dari folder `assets/record-keeper-root/`. Screenshot ditempel langsung; file teks/script ditautkan.

### Screenshot

<div class="nx-evidence-grid">
<figure><a href="assets/record-keeper-root/05-tar-checkpoint.png" target="_blank" rel="noopener"><img src="assets/record-keeper-root/05-tar-checkpoint.png" alt="05-tar-checkpoint.png" loading="lazy"></a><figcaption>05-tar-checkpoint.png</figcaption></figure>
<figure><a href="assets/record-keeper-root/06-flag.png" target="_blank" rel="noopener"><img src="assets/record-keeper-root/06-flag.png" alt="06-flag.png" loading="lazy"></a><figcaption>06-flag.png</figcaption></figure>
<figure><a href="assets/record-keeper-root/98-terminal-evidence.png" target="_blank" rel="noopener"><img src="assets/record-keeper-root/98-terminal-evidence.png" alt="98-terminal-evidence.png" loading="lazy"></a><figcaption>98-terminal-evidence.png</figcaption></figure>
</div>

### Transkrip / file pendukung

- [`01-recon.txt`](assets/record-keeper-root/01-recon.txt)
- [`02-enum-ops.txt`](assets/record-keeper-root/02-enum-ops.txt)
- [`03-tar-checkpoint.txt`](assets/record-keeper-root/03-tar-checkpoint.txt)
- [`04-root-flag.txt`](assets/record-keeper-root/04-root-flag.txt)
- [`07-spool-excerpt.txt`](assets/record-keeper-root/07-spool-excerpt.txt)

## Tabel Evidence

| Bukti | File | Keterangan |
|---|---|---|
| Recon + spool | `assets/record-keeper-root/01-recon.txt` | Service mesh, job format, akses model |
| Enumerasi ops | `assets/record-keeper-root/02-enum-ops.txt` | `sudo -l`, wrapper, permission, spooler |
| Tar injection | `assets/record-keeper-root/03-tar-checkpoint.txt` | Script, file opsi, trigger, ekstraksi |
| Root flag | `assets/record-keeper-root/04-root-flag.txt` | Flag, hash, kredensial ops, submit log |
| Spool docs | `assets/record-keeper-root/07-spool-excerpt.txt` | Kutipan arsitektur spool dari console |
| Render exploit | `assets/record-keeper-root/05-tar-checkpoint.png` | Render enumerasi + injection |
| Render flag | `assets/record-keeper-root/06-flag.png` | Render root flag + submit log |